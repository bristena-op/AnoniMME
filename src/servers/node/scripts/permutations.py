from itertools import permutations
from ..constants import DATABASE_SIZE
from random import randint

perm_list = list(permutations(range(DATABASE_SIZE)))


def permute_vector(vector):
    chosen_perm = randint(0, len(perm_list))
    output = []

    for v, pos in zip(vector, perm_list[chosen_perm]):
        output[pos] = v

    return output

