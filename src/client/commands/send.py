from connections.node import send_query
from constants import NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT, NODES, NODE_QUERY_PATH,\
    NODE_VERIFY_QUERY_PATH, COLLISIONS, NODE_RESPONSE_PATH
from functions.transform import string_to_number
from functions.vector import gen_vectors, gen_response_vectors
from functions.encryption import encrypt, encrypt_string, keyGen, setup
from petlib.ec import EcGroup, EcPt


def gen_gene_vectors(row, gene):
    vectors = gen_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT)
    vectors[0][row - 1] += string_to_number(gene)

    return vectors


def gen_key_vectors(row, key):
    vectors = gen_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT)
    vectors[0][row - 1] += string_to_number(key)

    return vectors


def gen_resp_vectors(row, contact):
    vectors = gen_response_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT, COLLISIONS)
    params = setup()
    priv, pub = keyGen(params)
    # enc_contact = [encrypt_string(params, pub, contact)]
    # print(enc_contact)
    for i in range(1, COLLISIONS + 1):
        vectors[0][row * i - 1] += string_to_number(contact)**(i)
        # vectors[0][row * i - 1][1] += string_to_number(enc_contact[1])

    return vectors


def send_vectors(row, gene, pub_key, v):
    key_vectors = gen_key_vectors(row, pub_key)
    gene_vectors = gen_gene_vectors(row, gene)
    # id = randint(0,10**10)

    for node_url, gene, key in zip(NODES, gene_vectors, key_vectors):
        payload = {
           # "id": id,
            "gene": gene,
            "key": key
        }

        if v:
            send_query(node_url, NODE_VERIFY_QUERY_PATH, payload)
        else:
            send_query(node_url, NODE_QUERY_PATH, payload)


def gen_all_vectors(row, key, gene):
    vector1 = gen_gene_vectors(row,gene)
    vector2 = gen_key_vectors(row,key)

    return vector1, vector2


def send_reponse_vectors(row, contact):
    vector = gen_resp_vectors(row, contact)
    vectors = []

    for node_url, contact in zip(NODES, vector):
        for i in range(1, COLLISIONS + 1):
            payload = {
                i: vector[i*(DATABASE_SIZE - 1)-1: i*DATABASE_SIZE]
            }

    send_query(node_url, NODE_RESPONSE_PATH, payload)

def gen_gene_vectors2(row, gene):
    vectors = gen_response_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT, COLLISIONS)
    for i in range(1, COLLISIONS + 1):
        vectors[0][row * i - 1] += string_to_number(gene)**i

    return vectors


def gen_key_vectors2(row, key):
    vectors = gen_response_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT, COLLISIONS)
    for i in range(1, COLLISIONS + 1):
        vectors[0][row * i - 1] += string_to_number(key)**i

    return vectors
def gen_all_vectors2(row, key, gene):
    vector1 = gen_gene_vectors2(row,gene)
    vector2 = gen_key_vectors2(row,key)

    return vector1, vector2