"""Encryption and type conversion handlers."""
from functools import wraps
from typing import Union

from plain_rsa.keys import PrivateKey, PublicKey
from plain_rsa.utils import bytes_to_int, int_to_bytes


def bytes_handler(func):
    """Convert to/from bytes when processing data."""

    @wraps(func)
    def inner(b: bytes, key: Union[PublicKey, PrivateKey]) -> bytes:
        n = bytes_to_int(b)
        x = func(n, key)
        return int_to_bytes(x)

    return inner


def _encrypt(m: int, public_key: PublicKey) -> int:
    """
    Encrypt m (int) using public_key.

    m must be less than the modulus (n) of public_key.
    """
    n, e = public_key.n, public_key.e
    if m >= n:
        raise ValueError("Message is too large to encrypt.")
    return pow(m, e, n)


def _decrypt(c: int, private_key: PrivateKey) -> int:
    """Decrypt c (int) using private_key."""
    n, d = private_key.n, private_key.d
    return pow(c, d, n)


@bytes_handler
def encrypt(plaintext: bytes, public_key: PublicKey) -> bytes:
    """
    Encrypt plaintext (bytes) using public_key.

    Bytes are converted to int, encrypted, then converted back.
    """
    return _encrypt(plaintext, public_key)


@bytes_handler
def decrypt(ciphertext: bytes, private_key: PrivateKey) -> bytes:
    """Decrypt ciphertext (bytes) using private_key."""
    return _decrypt(ciphertext, private_key)
