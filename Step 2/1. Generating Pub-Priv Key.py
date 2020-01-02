#############################################################################################

#### This program will generate the Public and Private key pair and store it as pem file ####

#############################################################################################


from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

###########################
## Generating a Key-Pair ##
###########################

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

########################################
## Storing a Private Key as .pem file ##
########################################

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('Doc/private_key.pem', 'wb') as f:
    f.write(pem)
    

#######################################
## Storing a Public Key as .pem file ##
#######################################
    
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('Doc/public_key.pem', 'wb') as f:
    f.write(pem)