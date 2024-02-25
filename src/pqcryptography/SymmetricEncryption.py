# Layer for symetric encryption

from Crypto.Cipher import AES #pycryptodome

def encrypt(key, plaintext):
	cipher = AES.new(key, AES.MODE_EAX)
	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(plaintext)
	return nonce+tag+ciphertext

def decrypt(key, ciphertext):
	nonce = ciphertext[0:16]
	tag = ciphertext[16:32]
	ciphertext = ciphertext[32:]
	cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	cipher.verify(tag)
	return plaintext
