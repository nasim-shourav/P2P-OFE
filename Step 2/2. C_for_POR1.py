
####################################################################################################################################

#### This program will read the value from file CforPOO1.txt and also ask user to select the time and wrtie that down in a file ####
#### Hashed those value and write it into another file, CforPOR1.txt                                                            ####

####################################################################################################################################

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



for i in range (1 , 1001):

    FileofCforPOO1 = 'C:/Nasim/P2P/Step 1/CforPOO1/CforPOO1_%s' %i + '.txt' #change the directory according to your setup
    with open( FileofCforPOO1 , 'rb') as f:
        CforPOO1 = f.read()
        f.close()

    # time2PublishInBC = input('Please insert the time limit: ')
    # time2PublishInBC_inBytes = time2PublishInBC.encode() #convert str into bytes
    with open('Doc/time.txt', 'rb') as f:
        # f.write(time2PublishInBC_inBytes)
        time2PublishInBC_inBytes = f.read()

    with open('C:/Nasim/P2P/Step 2/CforPOR1/c_%s' %i + '.txt', 'wb') as f:
        f.write(CforPOO1)
        f.write(time2PublishInBC_inBytes)

    with open('C:/Nasim/P2P/Step 2/CforPOR1/c_%s' %i + '.txt', 'rb') as f:
        data = f.read()
    hash_object = hashlib.sha256(data)
    str_dig = hash_object.hexdigest()
    byte_dig = str_dig.encode()
    with open('C:/Nasim/P2P/Step 2/CforPOR1/CforPOR1_%s' %i + '.txt', 'wb') as f:
        f.write(byte_dig)


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))



# #########################################
# ## Reading the value from CforPOO1.txt ##
# #########################################

# with open('Doc/CforPOO1.txt', 'rb') as f:
#     CforPOO1 = f.read()


# #########################################################
# ## Ask Bob to enter the time, write that into time.txt ##
# #########################################################

# time2PublishInBC = input('Please insert the time limit: ')
# time2PublishInBC_inBytes = time2PublishInBC.encode() #convert str into bytes
# with open('Doc/time.txt', 'wb') as f:
#     f.write(time2PublishInBC_inBytes)



# ###########################################################################
# ## Writing down the data read from CforPOO1 and time2PublishInBC_inBytes ##
# ###########################################################################

# with open('Doc/c.txt', 'wb') as f:
#     f.write(CforPOO1)
#     f.write(time2PublishInBC_inBytes)



# ################################################################################
# ## Reading the value from c.txt, hashed it and write the hash to CforPOR1.txt ##
# ################################################################################

# with open('Doc/c.txt', 'rb') as f:
#     data = f.read()
# hash_object = hashlib.sha256(data)
# str_dig = hash_object.hexdigest()
# byte_dig = str_dig.encode()
# with open('Doc/CforPOR1.txt', 'wb') as f:
#     f.write(byte_dig)


# #print(byte_dig)