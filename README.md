# python-plain-rsa

[![GitHub license](https://img.shields.io/github/license/Zedeldi/python-plain-rsa?style=flat-square)](https://github.com/Zedeldi/python-plain-rsa/blob/master/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/python-plain-rsa?style=flat-square)](https://github.com/Zedeldi/python-plain-rsa/commits) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Plain RSA cryptography written in pure-Python, without any padding or additional security features.

## Description

> :exclamation: python-plain-rsa is intended for educational purposes and is *not* secure! Use [python-rsa](https://pypi.org/project/rsa/) instead, if you require secure RSA encryption.

Without padding, RSA is not semantically secure, as it is a deterministic encryption algorithm; `encrypt(m, public_key)` will always yield the same results. This makes plaintext attacks possible.

Furthermore, by including padding, the ciphertext cannot be changed without producing invalid data, thus reducing its malleability -- a property which can be maliciously abused, even if the content of the message is still hidden.

### Implementation

Key generation follows the process described in this [Wikipedia article](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). The algorithm can be found in `plain_rsa.keys.gen_keys`. `PublicKey` and `PrivateKey` are dataclasses used solely to store `(n, e)` and `(n, d)`, respectively.

Values for `p`, `q` and `e` are not generated and must be passed to `gen_keys`. Large prime numbers should be used for encrypting bytes. `rsa.newkeys` can be used to generate larger keys automatically, as the data classes used are cross-compatible.

`gen_keys` will not check if the returned value of `e` and `d` are equal -- effectively making the public and private key the same -- as this is mathematically correct. The primality of inputs will be tested.

`plain_rsa.utils` contains various mathematical functions used for key generation, with the aim to separate and clarify each stage in the generation process.

`plain_rsa.crypto` defines encryption and decryption methods. These accept `bytes` as input and return them after processing, by converting to/from `int` when necessary. Use `_encrypt` and `_decrypt` to work with integers.

### Performance

Python's built-in function `pow` is used for exponential functions, such as `encrypt`, `decrypt` and `calc_d`. Using arithmetic operators, the following expressions are equivalent, but perform poorly with large numbers.

Encrypt: `(m ** e) % n`

Decrypt: `(c ** d) % n`

Modular multiplicative inverse:

```py
for x in range(1, lcm):
    if (e * x) % lcm == 1:
        return x
```

The primality test uses 6k+-1 optimisation, sourced from [Wikipedia](https://en.wikipedia.org/wiki/Primality_test#Python_code).

## Installation

1. Clone: `git clone https://github.com/Zedeldi/python-plain-rsa.git`
2. Install build: `pip3 install build`
3. Build: `python3 -m build`
4. Install wheel: `pip3 install dist/plain_rsa-*-py3-none-any.whl`

## Usage

This example uses comparatively small numbers for the initial components. In the real-world, much larger prime numbers would be used.

```py
import plain_rsa

p = 2017
q = 2221
e = 157
public_key, private_key = plain_rsa.gen_keys(p, q, e)

plaintext = b"RSA"
ciphertext = plain_rsa.encrypt(plaintext, public_key)
assert plain_rsa.decrypt(ciphertext, private_key) == plaintext
```

### Homomorphic Encryption

> [Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) is a form of encryption that permits users to perform computations on its encrypted data without first decrypting it. These resulting computations are left in an encrypted form which, when decrypted, result in an identical output to that produced had the operations been performed on the unencrypted data.

RSA (without padding) is partially homomorphic, due to the following property:

![RSA Homomorphic Property](https://wikimedia.org/api/rest_v1/media/math/render/svg/b479619754ae20442f010bf9e92d87fddbe4a1f2)

To demonstrate this, the `_encrypt` and `_decrypt` functions must be used to multiply integers. Byte-int conversion methods from `plain_rsa.utils` can be used manually, if the input or output is required in bytes.

```py
from plain_rsa.crypto import _decrypt, _encrypt

m1 = 741
m2 = 398

c1 = _encrypt(m1, public_key) * _encrypt(m2, public_key)
c2 = _encrypt(m1 * m2, public_key)

assert _decrypt(c1, private_key) == _decrypt(c2, private_key)
```

## Tests

Tests require `pytest`, which can be installed using the `[tests]` extra.

## License

python-plain-rsa is licensed under the GPL v3 for everyone to use, modify and share freely.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

[![GPL v3 Logo](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Donate

If you found this project useful, please consider donating. Any amount is greatly appreciated! Thank you :smiley:

My bitcoin address is: [bc1q5aygkqypxuw7cjg062tnh56sd0mxt0zd5md536](bitcoin://bc1q5aygkqypxuw7cjg062tnh56sd0mxt0zd5md536)
