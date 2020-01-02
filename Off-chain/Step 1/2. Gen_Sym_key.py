###########################################################################################################################

#### This program will take the original health data, and encrypt is two times with two symmetric keys, key1 and key2. ####

###########################################################################################################################

import io
import sys
import glob
import os.path
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from base64 import b64encode
import os
from datetime import datetime


start_time = datetime.now()
#generate First symmetric key
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

for i in range(1,1001):
    a = 'Sym_Key/%s' %i
    createFolder(a)
    for x in range(1,3):
        key = Fernet.generate_key()
        # print (type (key)) 
        file1 = open(a + '/%s.key' %x, 'wb') 
        file1.write(key) # The key is type bytes still
        file1.close()



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))