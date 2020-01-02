#########################################################################################################################################

#### This program will read the value from CforPOO1.txt, signed it with Alice's private key and generate a output file, SignedPOO.txt ####

#########################################################################################################################################

from __future__ import unicode_literals
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from datetime import datetime

start_time = datetime.now()


for i in range (1, 1001):

    #########################################
    ## Reading the value from CforPOO1.txt ##
    #########################################

    FileofCforPOO1 = 'C:/Nasim/P2P/Step 1/CforPOO1/CforPOO1_%s' %i + '.txt'
    with open( FileofCforPOO1 , 'rb') as f:
        CforPOO1 = f.read()
        f.close()

    #################################################
    ## Signed CforPOO.txt with Alice's private key ##
    #################################################

    Priv_Key = 'C:/Nasim/P2P/Step 1/Priv_Pub_Key/%s' %i
    with open(Priv_Key + "/Private_key_%s" %i + '.pem', "rb") as key_file:
    
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    signature = private_key.sign(
        CforPOO1,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    ###########################################
    ## Output the signed file, SignedPOO.txt ##
    ###########################################

    with open('C:/Nasim/P2P/Step 1/SignedC/SignedPOO_%s' %i + '.txt', 'wb') as f:
        f.write(signature)
        f.close()
    
    b64format = base64.b64encode(signature)
    with open('C:/Nasim/P2P/Step 1/SignedC/B64format_SignedPOO_%s' %i + '.txt', 'wb') as f:
        f.write(b64format)
        f.close()

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

# #################################################
# ## Signed CforPOO.txt with Alice's private key ##
# #################################################

# with open("Doc\private_key.pem", "rb") as key_file:
    
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
# ## Output the signed file, SignedPOO.txt ##
# ###########################################

# with open('Doc\SignedPOO.txt', 'wb') as f:
#     f.write(signature)

# print(base64.b64encode(signature))