from connections.node import send_query
from constants import NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT, NODES, NODE_QUERY_PATH
from functions.transform import string_to_number
from functions.vector import gen_vectors


def gen_gene_vectors(row, gene):
    vectors = gen_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT)
    vectors[0][row - 1] += string_to_number(gene)

    return vectors


def gen_key_vectors(row, key):
    vectors = gen_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT)
    vectors[0][row - 1] += string_to_number(key)

    return vectors


def send_vectors(row, gene, pub_key):
    key_vectors = gen_key_vectors(row, pub_key)
    gene_vectors = gen_gene_vectors(row, gene)

    for node_url, gene, key in zip(NODES, gene_vectors, key_vectors):
        payload = {
            "gene": gene,
            "key": key
        }

        send_query(node_url, NODE_QUERY_PATH, payload)
