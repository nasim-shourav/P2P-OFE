###########################################################################################################

#### This program will read the value from files test_ecrypted_twice.encrypted, HK2.txt and Bpubk1.txt ####
#### Hashed those value and write it into another file, CforPOO1.txt                                   ####

###########################################################################################################


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

    ##########################################################
    ## Reading the value from test_ecrypted_twice.encrypted ##
    ##########################################################
    encrypted_mssg = 'C:/Nasim/P2P/Step 1/Encrypted_Message/Twice/%s' %i + '.encrypted'
    with open( encrypted_mssg , 'rb') as f:
        encrypted_message1 = f.read()
        f.close()


    ####################################
    ## Reading the value from HK2.txt ##
    ####################################
    
    key2 = open('C:/Nasim/P2P/Step 1/HK2/HK2_of_%s' %i + '.txt', 'rb')
    hex_dig_k2 = key2.read()
    key2.close()

    #######################################
    ## Reading the value from Bpubk1.txt ##
    #######################################

    encrypted_Bpubk1 = 'C:/Nasim/P2P/Step 1/Encrypted_K1/Bpubk1_%s' %i + '.txt'
    with open(encrypted_Bpubk1, 'rb') as f:
        encrypted_key11 = f.read()
        f.close()

    ######################################################################################################
    ## Writing down the data read from test_ecrypted_twice.encrypted, HK2.txt and Bpubk1.txt into c.txt ##
    ######################################################################################################

    with open('C:/Nasim/P2P/Step 1/CforPOO1/c_%s' %i + '.txt', 'wb') as f:
        f.write(encrypted_message1)
        f.write(encrypted_key11)
        f.write(hex_dig_k2)

    with open('C:/Nasim/P2P/Step 1/CforPOO1/c_%s' %i + '.txt', 'rb') as f:
        data = f.read()
    hash_object = hashlib.sha256(data)
    str_dig = hash_object.hexdigest()
    byte_dig = str_dig.encode()
    with open('C:/Nasim/P2P/Step 1/CforPOO1/CforPOO1_%s' %i + '.txt', 'wb') as f:
        f.write(byte_dig)
        f.close()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


# ##########################################################
# ## Reading the value from test_ecrypted_twice.encrypted ##
# ##########################################################

# with open('Doc/test_ecrypted_twice.encrypted', 'rb') as f:
#     encrypted_message1 = f.read()


# ####################################
# ## Reading the value from HK2.txt ##
# ####################################

# key2 = open('Doc/HK2.txt', 'rb')
# hex_dig_k2 = key2.read()

# #######################################
# ## Reading the value from Bpubk1.txt ##
# #######################################

# encrypted_message = 'Doc/Bpubk1.txt'
# with open(encrypted_message, 'rb') as f:
#     encrypted_key11 = f.read()


# ######################################################################################################
# ## Writing down the data read from test_ecrypted_twice.encrypted, HK2.txt and Bpubk1.txt into c.txt ##
# ######################################################################################################

# with open('Doc/c.txt', 'wb') as f:
#     f.write(encrypted_message1)
#     f.write(encrypted_key11)
#     f.write(hex_dig_k2)



# ################################################################################
# ## Reading the value from c.txt, hashed it and write the hash to CforPOO1.txt ##
# ################################################################################

# with open('Doc/c.txt', 'rb') as f:
#     data = f.read()
# hash_object = hashlib.sha256(data)
# str_dig = hash_object.hexdigest()
# byte_dig = str_dig.encode()
# with open('Doc/CforPOO1.txt', 'wb') as f:
#     f.write(byte_dig)



# #print(byte_dig)