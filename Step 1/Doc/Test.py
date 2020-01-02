from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Taking the data from encrypted message, EK(M). Put that in encrypted_message1 and then write into c.txt file for hashing

encrypted_message = 'test_ecrypted_twice.encrypted'
with open(encrypted_message, 'rb') as f:
    encrypted_message1 = f.read()


# Taking the data from key2.key. Make a hash (HK2), that in hex_of_hash_key2 and then write into c.txt file for hashing

key2 = open('key2.key', 'rb')
data = key2.read()
hash_object_k2 = hashlib.sha256(data) # hash_object_k2 is a _hashlib.HASH data type
str_dig_k2 = hash_object_k2.hexdigest() # str_dig_k2 is a str data type
hex_dig_k2 = str_dig_k2.encode() # hex_dig_k2 is a bytes data type

# Taking the data from key1, encrypt it with Bpub (Bpub(k1)). Put that in encrypted_k1_hex and then write into c.txt file for hashing


encrypted_message = 'Bpubk1.txt'
with open(encrypted_message, 'rb') as f:
    encrypted_key11 = f.read()


# Taking the data from encrypted_message1, encrypted_key11 and encrypted_k1_hex and write it to c.txt

with open('c.txt', 'wb') as f:
    f.write(encrypted_message1)
    f.write(encrypted_key11)
    f.write(hex_dig_k2)



# Taking the data from c.txt, hash it with sha256

with open('c.txt', 'rb') as f:
    data = f.read()
hash_object = hashlib.sha256(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
