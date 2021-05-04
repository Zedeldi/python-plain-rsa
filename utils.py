"""Helper functions for generating RSA keys."""
import math


def is_prime(x: int) -> bool:
	"""Return whether x is a prime number."""
	if x <= 1:
		return False
	for n in range(2, x):
		if (x % n) == 0:
			return False
	else:
		return True


def calc_n(p: int, q: int) -> int:
	"""Return the product of p and q."""
	return p * q


def calc_lcm(p: int, q: int) -> int:
	"""Return the lowest common multiple of p and q."""
	return math.lcm(p, q)


def calc_d(e: int, lcm: int) -> int:
	"""Return the modular multiplicative inverse of e and lcm."""
	for x in range(1, lcm):
		if ((e % lcm) * (x % lcm)) % lcm == 1:
			return x
	return None
