#########################################################################################################################################

#### This program will read the value from CforPOR1.txt, decrypt signed SignedPOR.txt with Bob's public_key and verify the data ####

#########################################################################################################################################


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
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key

#########################################
## Reading the value from CforPOR1.txt ##
#########################################

#Input the CforPOR1.txt with its location

msg = input("Please enter the file name: ")
msg2 = open(msg, 'rb') 
message = msg2.read() # The key will be type bytes
msg2.close()

#####################################
## Load the public key and decrypt ##
#####################################

with open("Doc\public_key.pem", "rb") as key_file:
    public_key = key_file.read()

key = load_pem_public_key(public_key, backend=default_backend())


with open("Doc\SignedPOR.txt", "rb") as key_file:
    signature = key_file.read()

########################################################################################################################
## This will verify the signature. If the signature does not match, verify() will raise an InvalidSignature exception ##
########################################################################################################################

key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

