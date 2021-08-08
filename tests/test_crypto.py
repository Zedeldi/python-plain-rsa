import math
import random

import pytest

from plain_rsa.crypto import _decrypt, _encrypt, decrypt, encrypt


def test_encrypt(public_key):
    m = random.randint(3, public_key.n)
    c = _encrypt(m, public_key)
    assert isinstance(c, int)


def test_encrypt_and_decrypt(public_key, private_key):
    m = random.randint(3, public_key.n)
    c = _encrypt(m, public_key)
    assert _decrypt(c, private_key) == m


def test_encrypt_bytes(public_key):
    m = random.randbytes(2)
    c = encrypt(m, public_key)
    assert isinstance(c, bytes)


def test_encrypt_and_decrypt_bytes(public_key, private_key):
    m = random.randbytes(2)
    c = encrypt(m, public_key)
    assert decrypt(c, private_key) == m


def test_message_too_large(public_key):
    m = public_key.n + 1
    with pytest.raises(ValueError, match="Message is too large to encrypt."):
        _encrypt(m, public_key)


def test_homomorphism(public_key, private_key):
    sqrt = int(math.sqrt(public_key.n))
    m1, m2 = [random.randint(3, sqrt) for _ in range(2)]
    c1 = _encrypt(m1, public_key) * _encrypt(m2, public_key)
    c2 = _encrypt(m1 * m2, public_key)
    assert _decrypt(c1, private_key) == _decrypt(c2, private_key)
