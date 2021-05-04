"""Key classes and generation algorithm."""
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
