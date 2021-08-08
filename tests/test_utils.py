from plain_rsa.utils import bytes_to_int, int_to_bytes, is_prime


def test_is_prime():
    nonprimes = [-3, 0, 1, 6, 25]
    primes = [2, 105199]
    for n in nonprimes:
        assert not is_prime(n)
    for n in primes:
        assert is_prime(n)


def test_int_to_bytes():
    n_little = 4281170
    n_big = 5395265
    b_little = int_to_bytes(n_little, "little")
    b_big = int_to_bytes(n_big, "big")
    assert isinstance(b_little, bytes)
    assert isinstance(b_big, bytes)
    assert b_little == b_big == b"RSA"


def test_bytes_to_int():
    b = b"RSA"
    n_little = bytes_to_int(b, "little")
    n_big = bytes_to_int(b, "big")
    assert isinstance(n_little, int)
    assert isinstance(n_big, int)
    assert n_little == 4281170
    assert n_big == 5395265
