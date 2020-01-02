#########################################################################################################################################

#### This program will read the value from CforPOO1.txt, decrypt signed SignedPOO.txt with Alice's public_key and verify the data ####

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
from datetime import datetime

start_time = datetime.now()


for i in range (1, 1001):
    FileofCforPOO1 = 'C:/Nasim/P2P/Step 1/CforPOO1/CforPOO1_%s' %i + '.txt' #change the directory according to your setup
    with open( FileofCforPOO1 , 'rb') as f:
        CforPOO1 = f.read()
        f.close()

    Pub_Key = 'C:/Nasim/P2P/Step 1/Priv_Pub_Key/%s' %i #change the directory according to your setup
    with open(Pub_Key + "/Public_key_%s" %i + '.pem', "rb") as key_file:
        public_key = key_file.read()

    key = load_pem_public_key(public_key, backend=default_backend())

    
    with open("C:/Nasim/P2P/Step 1/SignedC/SignedPOO_%s"%i + ".txt", "rb") as key_file:
        signature = key_file.read()
    
    
    key.verify(
        signature,
        CforPOO1,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# #########################################
# ## Reading the value from CforPOO1.txt ##
# #########################################

# #Input the CforPOO1.txt with its location

# msg = input("Please enter the file name: ")
# msg2 = open(msg, 'rb') 
# message = msg2.read() # The key will be type bytes
# msg2.close()

# #####################################
# ## Load the public key and decrypt ##
# #####################################

# with open("Doc\public_key.pem", "rb") as key_file:
#     public_key = key_file.read()

# key = load_pem_public_key(public_key, backend=default_backend())


# with open("Doc\SignedPOO.txt", "rb") as key_file:
#     signature = key_file.read()


# ########################################################################################################################
# ## This will verify the signature. If the signature does not match, verify() will raise an InvalidSignature exception ##
# ########################################################################################################################

# key.verify(
#     signature,
#     message,
#     padding.PSS(
#         mgf=padding.MGF1(hashes.SHA256()),
#         salt_length=padding.PSS.MAX_LENGTH
#     ),
#     hashes.SHA256()
# )

