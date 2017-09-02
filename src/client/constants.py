PROTOCOL = 'http'

MASTER_URL = '{}://localhost:3000'.format(PROTOCOL)
MASTER_PARAMETERS_PATH = 'parameters'

NODES = [
    '{}://localhost:8000'.format(PROTOCOL),
    '{}://localhost:8001'.format(PROTOCOL),
]

NODE_QUERY_PATH = 'query'

SMALL_INT = 2 ** 512
LARGE_INT = 2 ** 1024

NODE_NUMBERS = 2

DATABASE_SIZE = 2000

ENCODING_MAX_LENGTH = 256