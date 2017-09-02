import pytest

from functions.vector import gen_vectors
from constants import NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT


@pytest.mark.parametrize('execution_number', range(5))
def test_generate_vector(execution_number):
    vectors = gen_vectors(NODE_NUMBERS, DATABASE_SIZE, SMALL_INT, LARGE_INT)

    output = [
        sum(number[i] for number in vectors)
        for i in range(len(vectors))
    ]

    for number in output:
        assert number == 0