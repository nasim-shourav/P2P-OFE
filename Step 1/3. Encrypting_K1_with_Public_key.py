###########################################################################################################################

#### This program will encrypt one symmetric key, key1, with Bob's public key and generate a file of that as an output ####

###########################################################################################################################


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
###################################
## Reading the key from key1.key ##
###################################
start_time = datetime.now()
# Enter the exact location of the file as well as correct file name with its extension

for i in range (1, 1001):
    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i
    key2 = open(key_dir + '/1.key', 'rb')
    data = key2.read()
    key2.close()
    pubKey_dir = 'C:/Nasim/P2P/Step 1/Priv_Pub_Key/%s' %i
    with open(pubKey_dir + '/Public_key_%s' %i +'.pem', "rb") as k:
        key = RSA.importKey(k.read())
    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(data)
    with open('C:/Nasim/P2P/Step 1/Encrypted_K1/Bpubk1_%s' %i + '.txt', 'wb') as f:
        f.write(encrypted)
        f.close()



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))