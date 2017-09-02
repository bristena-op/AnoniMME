import random
import string
import timeit
from petlib.ec import EcGroup, EcPt


def setup():
    """Generates the Cryptosystem Parameters."""
    G = EcGroup(nid=713)
    g = G.hash_to_point(b"g")
    h = G.hash_to_point(b"h")
    o = G.order()
    return (G, g, h, o)


def keyGen(params):
    """ Generate a private / public key pair """
    (G, g, h, o) = params

    priv = o.random()
    pub = priv * g

    return (priv, pub)


def encrypt(params, pub, m):
    """ Encrypt a message under the public key """
    (G, g, h, o) = params
    k = o.random()

    return k * g, k * pub + m * h


_logh = None
def logh(params, hm):
    """ Compute a discrete log, for small number only """
    global _logh
    (G, g, h, o) = params

    # Initialize the map of logh
    if _logh == None:
        _logh = {}
        for m in range (-1000, 1000):
            _logh[(m * h)] = m

    if hm not in _logh:
        raise Exception("No decryption found.")

    return _logh[hm]


def decrypt(params, priv, ciphertext):
    """ Decrypt a message using the private key """
    a, b = ciphertext
    hm = b - priv * a

    return logh(params, hm)


def encrypt_string(params, pub, message):
    return [encrypt(params, pub, ord(m)) for m in message]


def decrypt_cipher(params, priv, cipher):
    return ''.join(chr(decrypt(params, priv, c)) for c in cipher)


def test_encrypt_decrip():
    initial_string = 'supercalifragilisticexpialidocious'
    params = setup()
    keys = keyGen(params)
    cipher = encrypt_string(params, keys[1], initial_string)
    deciphered_text = decrypt_cipher(params, keys[0], cipher)

    assert initial_string == deciphered_text


def check_encrypt_performance(messages):
    params = setup()
    keys = keyGen(params)

    return [
        encrypt_string(params, keys[1], msg)
        for msg in messages
    ]


def generate_messages(x):
    output = []

    for _ in range(x):
        message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
        output.append(message)

    return output


def time_encryption(messages, rounds=1000):
    times = []
    for _ in range(rounds):
        generated_messages = generate_messages(messages)
        time = timeit.timeit(lambda: check_encrypt_performance(generated_messages), number=1)
        times.append(time)

    return sum(times) / rounds


if __name__ == '__main__':
    # print('9 queries', time_encryption(9, 100))
    # print('100 queries', time_encryption(100, 100))
    # print('200 queries', time_encryption(200, 100))
    # print('500 queries', time_encryption(500, 100))
    print('1000 queries', time_encryption(1000, 100))

