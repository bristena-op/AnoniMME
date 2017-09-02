import timeit
from unittest.mock import patch

from commands import send


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

    with patch.object(send, 'DATABASE_SIZE', db_size),\
         patch('commands.send.get_parameters', return_value={'nid': 713}):
        for i in range(rounds):
            time = timeit.timeit(lambda: send.gen_all_vectors(0, str(i)), number=1)
            times.append(time)

    return sum(times) / rounds


if __name__ == '__main__':
    print("DB_SIZE 2000", profile_vector_generation(2000))
    print("DB_SIZE 10000", profile_vector_generation(10000))
    print("DB_SIZE 20000", profile_vector_generation(20000))