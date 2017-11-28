import urllib
import requests
from unittest.mock import patch

from constants import NODES, NODE_QUERY_PATH
from commands import send


def header_size(headers):
    return sum(len(key) + len(value) + 4 for key, value in headers.items()) + 2


def estimated_bandwidth(r):
    request_line_size = len(r.request.method) + len(r.request.path_url) + 12
    request_size = request_line_size + header_size(r.request.headers) + int(r.request.headers.get('content-length', 0))
    print('Request  : {} bytes'.format(request_size))

    response_line_size = len(r.reason) + 15
    response_size = response_line_size + header_size(r.headers) + int(r.headers.get('content-length', 0))
    print('Response : {} bytes'.format(response_size))

    return request_size + response_size


def generate(row, gene):
    key_vectors, gene_vectors = send.gen_all_vectors2(row, '21312312', gene)

    payload = {
        "gene": gene_vectors[0],
        "key": key_vectors[0]
    }

    query_path = urllib.parse.urljoin(NODES[0], NODE_QUERY_PATH)
    r = requests.post(query_path, json=payload)

    return estimated_bandwidth(r)


def run_bandwidth_estimation(db_size, rounds=10):
    """
    Estimate bandwidth roundtrip to a node server at the request level.

    This can be further optimised by using gzip compression.
    """
    bandwidth = 0

    with patch.object(send, 'DATABASE_SIZE', db_size):
        for i in range(rounds):
            bandwidth += generate(i, str(i))

    return '{} bytes, {} mb'.format(bandwidth/rounds, bandwidth/rounds/10**6)


if __name__ == '__main__':
    print("DB_SIZE 135:", run_bandwidth_estimation(135 , 1))
    print("DB_SIZE 675:", run_bandwidth_estimation(675, 1))
    print("DB_SIZE 1350:", run_bandwidth_estimation(1350, 1))