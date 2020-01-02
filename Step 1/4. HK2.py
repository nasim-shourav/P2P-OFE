###############################################################################################

#### This program will hashed the key2 and generate a file of that hash value as an output ####

###############################################################################################


from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime

start_time = datetime.now()


for i in range (1, 1001): 
    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i
    key2 = open(key_dir + '/2.key', 'rb')
    data = key2.read()
    hash_object_k2 = hashlib.sha256(data) # hash_object_k2 is a _hashlib.HASH data type
    str_dig_k2 = hash_object_k2.hexdigest() # str_dig_k2 is a str data type
    hex_dig_k2 = str_dig_k2.encode() # hex_dig_k2 is a bytes data type
    with open('C:/Nasim/P2P/Step 1/HK2/HK2_of_%s' %i + '.txt', 'wb') as f:
        f.write(hex_dig_k2)
        f.close()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))