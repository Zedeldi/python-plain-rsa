"""
Plain RSA cryptography, without any padding or additional security features.

Key generation follows the process described in this Wikipedia article:
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""
from dataclasses import dataclass

from plain_rsa import utils


@dataclass
class PublicKey:
	"""Store n and e to be used as a public key."""

	n: int
	e: int


@dataclass
class PrivateKey:
	"""Store n and d to be used as a private key."""

	n: int
	d: int


def gen_keys(p: int, q: int, e: int) -> tuple[PublicKey, PrivateKey]:
	"""
	Generate keys given p, q and e.

	p and q must be distinct prime integers.
	e must be less than lcm(p - 1, q - 1) and a prime integer.

	Return a public and private key-pair as a tuple.
	"""
	if p == q:
		raise ValueError("p and q must be distinct values.")
	if not utils.is_prime(p) or not utils.is_prime(q):
		raise ValueError("Prime numbers required.")
	n = utils.calc_n(p, q)
	lcm = utils.calc_lcm(p - 1, q - 1)
	if e > lcm or not utils.is_prime(e):
		raise ValueError("Invalid exponent.")
	d = utils.calc_d(e, lcm)
	return (
		PublicKey(n, e),
		PrivateKey(n, d)
	)


def encrypt(m: int, public_key: PublicKey) -> int:
	"""
	Encrypt m (int) using public_key.

	m must be less than the modulus (n) of public_key.
	"""
	n, e = public_key.n, public_key.e
	if m >= n:
		raise ValueError("Message is too large to encrypt.")
	return (m ** e) % n


def decrypt(c: int, private_key: PrivateKey) -> int:
	"""Decrypt c (int) using private_key."""
	n, d = private_key.n, private_key.d
	return (c ** d) % n
