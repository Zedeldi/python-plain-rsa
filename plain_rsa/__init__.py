"""
Plain RSA cryptography, without any padding or additional security features.

Key generation follows the process described in this Wikipedia article:
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""
from plain_rsa.crypto import decrypt, encrypt
from plain_rsa.keys import PrivateKey, PublicKey, gen_keys

__all__ = [
    "encrypt",
    "decrypt",
    "PublicKey",
    "PrivateKey",
    "gen_keys",
]
