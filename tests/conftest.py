import pytest

from plain_rsa import PrivateKey, PublicKey, gen_keys

p = 2017
q = 2221
e = 157
public_key_, private_key_ = gen_keys(p, q, e)


@pytest.fixture
def public_key() -> PublicKey:
    return public_key_


@pytest.fixture
def private_key() -> PrivateKey:
    return private_key_
