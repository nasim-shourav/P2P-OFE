#########################################################################################################################################

#### This program will read the value from CforPOR1.txt, signed it with Bob's private key and generate a output file, SignedPOR.txt ####

#########################################################################################################################################


from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64
from datetime import datetime

start_time = datetime.now()


for i in range (1, 1001):

    #########################################
    ## Reading the value from CforPOO1.txt ##
    #########################################

    FileofCforPOR1 = 'C:/Nasim/P2P/Step 2/CforPOR1/CforPOR1_%s' %i + '.txt' #change the directory according to your setup
    with open( FileofCforPOR1 , 'rb') as f:
        CforPOR1 = f.read()
        f.close()

    #################################################
    ## Signed CforPOO.txt with Alice's private key ##
    #################################################

    Priv_Key = 'C:/Nasim/P2P/Step 1/Priv_Pub_Key/%s' %i #change the directory according to your setup
    with open(Priv_Key + "/Private_key_%s" %i + '.pem', "rb") as key_file:
    
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    signature = private_key.sign(
        CforPOR1,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    ###########################################
    ## Output the signed file, SignedPOO.txt ##
    ###########################################

    with open('C:/Nasim/P2P/Step 2/SignedC/SignedPOR_%s' %i + '.txt', 'wb') as f:
        f.write(signature)
        f.close()
    
    b64format = base64.b64encode(signature)
    with open('C:/Nasim/P2P/Step 2/SignedC/B64format_SignedPOR_%s' %i + '.txt', 'wb') as f:
        f.write(b64format)
        f.close()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))



# #########################################
# ## Reading the value from CforPOR1.txt ##
# #########################################

# #Input the CforPOR1.txt with its location

# msg = input("Please enter the file name: ")
# msg2 = open(msg, 'rb') 
# message = msg2.read() # The key will be type bytes
# msg2.close()

# #################################################
# ## Signed CforPOO.txt with Bob's private key ####
# #################################################

# with open("Doc\private_key.pem", "rb") as key_file:
#     #key = RSA.importKey(k.read()) #RSA.importKey
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None,
#         backend=default_backend()
#     )

# signature = private_key.sign(
#     message,
#     padding.PSS(
#         mgf=padding.MGF1(hashes.SHA256()),
#         salt_length=padding.PSS.MAX_LENGTH
#     ),
#     hashes.SHA256()
# )

# ###########################################
# ## Output the signed file, SignedPOR.txt ##
# ###########################################

# with open('Doc\SignedPOR.txt', 'wb') as f:
#     f.write(signature)