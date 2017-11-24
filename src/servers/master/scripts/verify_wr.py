from collections import Counter


def verify_wr(write_requests):
    check_vector = [0] * len(write_requests[0])

    for wr in write_requests:
        check_vector += wr

    if Counter(check_vector).most_common(1)[0][1] == len(check_vector) - 1:
        return 1
    else:
        return 0
