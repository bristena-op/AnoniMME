import random


def _gen_random_vector(nb_vectors, lower_bound, upper_bound):
    return [
        random.randint(lower_bound, upper_bound)
        for _ in range(nb_vectors)
    ]


def gen_vectors(nb_nodes, nb_vectors, lower_bound, upper_bounds):
    output_vectors = [
        _gen_random_vector(nb_vectors, lower_bound, upper_bounds)
        for _ in range(nb_nodes - 1)
    ]
    normalizing_vector = [
        -sum(x[i] for x in output_vectors)
        for i in range(len(output_vectors[0]))
    ]

    output_vectors.append(normalizing_vector)

    return output_vectors
