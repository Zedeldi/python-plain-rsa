"""Helper functions for generating RSA keys and encryption."""
import math
import sys


def is_prime(n: int) -> bool:
    """
    Primality test using 6k+-1 optimisation.

    https://en.wikipedia.org/wiki/Primality_test#Python_code
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calc_n(p: int, q: int) -> int:
    """Return the product of p and q."""
    return p * q


def calc_lcm(p: int, q: int) -> int:
    """Return the lowest common multiple of p and q."""
    return math.lcm(p, q)


def calc_d(e: int, lcm: int) -> int:
    """
    Return the modular multiplicative inverse of e (mod lcm).

    Raise ValueError if e is not invertible with respect to the modulus lcm.
    """
    return pow(e, -1, lcm)


def bytes_to_int(b: bytes, byteorder=sys.byteorder) -> int:
    """Convert bytes to integer represented by byteorder."""
    return int.from_bytes(b, byteorder)


def int_to_bytes(x: int, byteorder=sys.byteorder) -> bytes:
    """Convert integer to bytes represented by byteorder."""
    return x.to_bytes((x.bit_length() + 7) // 8, byteorder)
