from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

msg = input("Please enter the file name: ")
msg2 = open(msg, 'rb') 
msg1 = msg2.read() # The key will be type bytes
msg2.close()

with open("E:\Canada\Thesis\P2P-OFE\P2P\private_key.pem", "rb") as k:
    key = RSA.importKey(k.read())
encryptor = PKCS1_OAEP.new(key)
encrypted = encryptor.encrypt(msg1)
with open('POO1.txt', 'wb') as f:
    f.write(binascii.hexlify(encrypted))
print("Encrypted:", binascii.hexlify(encrypted))

