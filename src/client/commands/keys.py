from binascii import hexlify

from connections.master import get_parameters
from constants import MASTER_URL, MASTER_PARAMETERS_PATH
from functions.key import generate_parameters, generate_keys


def generate_keys_command(filename):
    params = get_parameters(MASTER_URL, MASTER_PARAMETERS_PATH)
    nid = params["nid"]
    g, o = generate_parameters(nid)

    priv, pub = generate_keys(g, o)

    with open(filename, 'w') as file:
        file.write(str(nid) + '\n')
        file.write(str(hexlify(pub.export()).decode("utf8")) + '\n')
        file.write(str(priv) + '\n')