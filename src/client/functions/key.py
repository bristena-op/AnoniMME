from petlib.ec import EcGroup


def generate_parameters(nid):
    """ Generates the Cryptosystem Parameters. """
    G = EcGroup(nid)
    g = G.hash_to_point(b"g")
    o = G.order()
    return (g, o)


def generate_keys(g, o):
    """ Generate a private / public key pair. """
    priv = o.random()
    pub = priv * g

    return (priv, pub)