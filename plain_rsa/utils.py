"""Helper functions for generating RSA keys and encryption."""
import math
import sys


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


def bytes_to_int(b: bytes, byteorder=sys.byteorder) -> int:
	"""Convert bytes to integer represented by byteorder."""
	return int.from_bytes(b, byteorder)


def int_to_bytes(x: int, byteorder=sys.byteorder) -> bytes:
	"""Convert integer to bytes represented by byteorder."""
	return x.to_bytes((x.bit_length() + 7) // 8, byteorder)