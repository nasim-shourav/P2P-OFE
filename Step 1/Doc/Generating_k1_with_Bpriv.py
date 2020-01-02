from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import ast
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

msg = input("Please enter the file name: ")
msg2 = open(msg, 'rb') 
encrypted = msg2.read() # The key will be type bytes
msg2.close()

private_key = RSA.importKey(open('Doc\private_key.pem', 'rb').read())
cipher = PKCS1_OAEP.new(private_key)  
print (cipher.decrypt(encrypted))

#message = decryptor.decrypt(encrypted)
# with open('Doc\Bpubk1.txt', 'wb') as f:
#     f.write(binascii.hexlify(plaintext))

# print("Plaintext:", plaintext)