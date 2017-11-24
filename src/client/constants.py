PROTOCOL = 'http'

MASTER_URL = '{}://localhost:3000'.format(PROTOCOL)
MASTER_PARAMETERS_PATH = 'parameters'

NODES = [
    '{}://localhost:8000'.format(PROTOCOL),
    '{}://localhost:8001'.format(PROTOCOL),
]
NODE_VERIFY_QUERY_PATH = 'verifyquery'
NODE_QUERY_PATH = 'query'
NODE_RESPONSE_PATH = 'response'


SMALL_INT = 2 ** 512
LARGE_INT = 2 ** 1024

NODE_NUMBERS = 6

DATABASE_SIZE = 200

ENCODING_MAX_LENGTH = 256

COLLISIONS = 10
