PROTOCOL = 'http'

MASTER_URL = '{}://localhost:3000'.format(PROTOCOL)
MASTER_PARAMETERS_PATH = 'parameters'

NODES = [
    '{}://localhost:8000'.format(PROTOCOL),
    '{}://localhost:8001'.format(PROTOCOL),
]

NODE_QUERY_PATH = 'query'

SMALL_INT = 2 ** 256
LARGE_INT = 2 ** 512

NODE_NUMBERS = 2

DATBASE_SIZE = 10

ENCODING_MAX_LENGTH = 256