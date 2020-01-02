#############################################################################################

#### This program will generate the Public and Private key pair and store it as pem file ####

#############################################################################################

import os.path
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

for i in range(1,1001):
    a = 'C:/Nasim/P2P/Step 1/Priv_Pub_Key/%s' %i
    createFolder(a)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(a + '/Private_key_%s' %i + '.pem', 'wb') as f:
        f.write(pem)
        f.close()
    
    pub = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(a + '/Public_key_%s' %i + '.pem', 'wb') as f:
        f.write(pub)
        f.close()













###########################
## Generating a Key-Pair ##
###########################

# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#     backend=default_backend()
# )
# public_key = private_key.public_key()

########################################
## Storing a Private Key as .pem file ##
########################################

# pem = private_key.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.PKCS8,
#     encryption_algorithm=serialization.NoEncryption()
# )

# with open('Doc/private_key.pem', 'wb') as f:
#     f.write(pem)
    

#######################################
## Storing a Public Key as .pem file ##
#######################################
    
# pem = public_key.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )

# with open('Doc/public_key.pem', 'wb') as f:
#     f.write(pem)