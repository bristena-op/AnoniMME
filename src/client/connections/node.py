import requests

import urllib.parse


def send_query(url, path, payload):
    query_path = urllib.parse.urljoin(url, path)
    r = requests.post(query_path, json=payload)

    if r.status_code == 200:
        return r
    else:
        raise Exception("Issues sending query to {}.", query_path)