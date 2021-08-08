import pytest

from plain_rsa.keys import gen_keys


def test_equal_p_q():
    p = q = 2017
    e = 157
    with pytest.raises(ValueError, match="p and q must be distinct values."):
        public_key, private_key = gen_keys(p, q, e)


def test_non_prime():
    p = 2000
    q = 2017
    e = 157
    with pytest.raises(ValueError, match="p and q must be prime integers."):
        public_key, private_key = gen_keys(p, q, e)


def test_invalid_e():
    p = 2017
    q = 2221
    e = p * q
    with pytest.raises(
        ValueError,
        match=r"e must be less than lcm\(p - 1, q - 1\) and a prime integer.",
    ):
        public_key, private_key = gen_keys(p, q, e)


def test_no_inverse():
    p = 2017
    q = 2221
    e = 2
    with pytest.raises(
        ValueError,
        match="Cannot find a suitable value for d. Try increasing e.",
    ):
        public_key, private_key = gen_keys(p, q, e)
