# PQCryptography

This library was written due to rising threat of quantum computing.

## Installation
```bash
pip install pqcryptography
```
## How to use pqcryptography
### Importing
```python3
import pqcryptography as pqc
```

### Default algorithms
Default encryption algorithm is `Kyber1024`. Default signing algorithm is `Dilithium5`

### Algorithms
If you dont want to use default algorithm you can pick one from the algorithm list.
```python3
print(pqc.encryption.get_algorithms())
print(pqc.signing.get_algorithms())
```
*Note: Results are incompleate and outdated. You should run the code yourself*
```python3
['BIKE-L1', 'BIKE-L3', ..., 'FrodoKEM-1344-AES', 'FrodoKEM-1344-SHAKE']
['Dilithium2', 'Dilithium3', ..., 'SPHINCS+-SHAKE-256f-simple', 'SPHINCS+-SHAKE-256s-simple']
```

## so you dont trust me bro?
This package uses [**unofficial** liboqs python package](https://pypi.org/project/liboqs/) which is shipped with precompiled [oqs](https://github.com/open-quantum-safe/liboqs) libraries. You can not be certain that those binaries arent malicious so you want to build your own. You can build binaries by following build instructions at [oqs official repository](https://github.com/open-quantum-safe/liboqs) and replace `.so`/`.dll` files in the package folder (python_directory/site-packages/liboqs/).
