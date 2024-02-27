# PQCryptography

This library was written due to rising threat of quantum computing.
It main goal is to create easy wrapper of liboqs to spread post quantum cryptography

## Installation
```bash
pip install pqcryptography
```
## How to use pqcryptography
### Importing
```python3
import pqcryptography as pqc
```

### Generating keys / signs
```python3
public_key, private_key = pqc.encryption.generate_keypair()
public_sign, private_sign = pqc.signing.generate_signs()
```
Just like in any other asymmetric encryption library.

### Encryption and decryption
**How encryption work**
```python3
message = "Test Message"
encrypted_message = pqc.encryption.encrypt(public_key, message.encode("utf-8"))
```
Please take into consideration that message needs to be encoded before encryption. Here I used utf-8 encoding. Alternatively you can use raw bytes for message.
Also encryption of message increases its size exactly by 1600 bytes. This is because AES-256 nonce and tag is stored at the beginning of the message.
`encrypted_message` type is bytes.
**How decryption work**
```python3
retrieved_message = pqc.encryption.decrypt(private_key, encrypted_message)
print(retrieved_message.decode("utf-8"))
```
`retrieved_message` needs to be decoded if you didn't encrypt raw bytes.
Output is "Test Message"

## Signing and verifying
**How signing works**
```python3
signed_message = pqc.signing.sign(private_sign, message.encode("utf-8"))
```
`signed_message` type is bytes. Signature is appended to the message and its size will vary from algorithm to algorithm. Here's how to get it's size:
```python3
print(pqc.signing.get_details()["length_signature"])
```
**How verification works**
So we got our message. That is how we should verify that it is legit:
```python3
verified_message = pqc.signing.verify(public_sign, signed_message)
print(verified_message.decode("utf-8"))
```
`verified_message` is just encoded `message` with signature stripped.
If message was tampered with verify function will raise `AssertionError`

### Using non-default algorithm
So you want to change encryption/signing algorithm? Sure! Just use keyword `algorithm`. It is supported for every function except `get_algorithms()`

### Default algorithms
Default encryption algorithm is `Kyber1024`. Default signing algorithm is `Dilithium5`

### Algorithms
If you don't want to use default algorithm you can pick one from the algorithm list.
```python3
print(pqc.encryption.get_algorithms())
print(pqc.signing.get_algorithms())
```
*Note: Results are incomplete and probably outdated. You should run the code yourself*
```python3
['BIKE-L1', 'BIKE-L3', ..., 'FrodoKEM-1344-AES', 'FrodoKEM-1344-SHAKE']
['Dilithium2', 'Dilithium3', ..., 'SPHINCS+-SHAKE-256f-simple', 'SPHINCS+-SHAKE-256s-simple']
```

## so you don't trust me bro?
This package uses [**unofficial** liboqs python package](https://pypi.org/project/liboqs/) which is shipped with precompiled [oqs](https://github.com/open-quantum-safe/liboqs) libraries. You can not be certain that those binaries aren't malicious so you want to build your own. You can build binaries by following build instructions at [oqs official repository](https://github.com/open-quantum-safe/liboqs) and replace **.so**/**.dll** files in the package folder (*python_directory*/site-packages/liboqs/).

## Im using pyinstaller / nuitka and it doesnt work

Just copy **.so**/**.dll** files from liboqs package folder (*python_directory*/site-packages/liboqs/) to your executable folder and it will load files from your local directory.
