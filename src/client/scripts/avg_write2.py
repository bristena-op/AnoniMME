import timeit
from unittest.mock import patch
import random
from commands import send

import random


def random_line(afile):
    lines = list(open(afile, 'r').read().splitlines())

    r = random.randint(0, len(lines))
    if len(lines) > 0:
        line = lines[r]

    else:
        line = ''
    return line


def profile_vector_generation(db_size, rounds=1000):
    """
    Estimate the amount of time it takes to generate the vectors on the client machine.

    There is also a small overhead for the lambda invocation and passing in the different
    parameters.

    We have patched the database size to be able to run multiple tests and also we have
    patched the connection to the master server since that depends on a users network
    connection.
    """
    times = []
    with patch.object(send, 'DATABASE_SIZE', db_size):
        for i in range(rounds):
            gene = random_line('gene_symbols.txt')
            time = timeit.timeit(
                lambda: send.gen_all_vectors(random.randint(1, db_size), str(i), gene),
                number=1
            )
            times.append(time)

    return sum(times) / rounds


if __name__ == '__main__':
    print("DB_SIZE 135", profile_vector_generation(135))
    print("DB_SIZE 675", profile_vector_generation(675))
    print("DB_SIZE 1350", profile_vector_generation(1350))