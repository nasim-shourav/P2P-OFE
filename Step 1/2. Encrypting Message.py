###########################################################################################################################

#### This program will take the original health data, and encrypt is two times with two symmetric keys, key1 and key2. ####

###########################################################################################################################

from cryptography.fernet import Fernet
import io
import sys
import glob
import os.path
from Crypto.Cipher import AES
import pyaes
from base64 import b64encode
import base64
from datetime import datetime
##########################
## Encrypting Files     ##
##########################
start_time = datetime.now()

for i in range(1,1001):
    file_name = ('C:/Nasim/P2P/Step 1/Test/%s' %i + '.csv')
    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i
    file1 = open(key_dir + '/1.key', 'rb') 
    key = file1.read() 
    print("Key 1 ====>", key)
    
    file1.close()   
    
    f = open(file_name, 'rb')
    data = f.read()
    print ("data ==> ", (data))
    print("===========================================================================================")
    print("===========================================================================================")

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)


    with open("C:/Nasim/P2P/Step 1/Encrypted_Message/Once/EncO%s.encrypted" %i, 'wb') as f:
        f.write(encrypted)
        f.close()

    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i
    file1 = open(key_dir + '/2.key', 'rb')     
    key = file1.read()
    print("Key 2 ====> ", key)
    file1.close()   
    
    f = open("C:/Nasim/P2P/Step 1/Encrypted_Message/Once/EncO%s.encrypted" %i, 'rb')
    data = f.read()
    print ("data for Twice", (data))
    print("===========================================================================================")
    print("===========================================================================================")

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)


    with open("C:/Nasim/P2P/Step 1/Encrypted_Message/Twice/%s.encrypted" %i, 'wb') as f:
        f.write(encrypted)
        f.close()



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))