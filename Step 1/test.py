import os
import io
import sys
import glob
import os.path
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from base64 import b64encode
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

for i in range(1,3):
    a = 'Folder/%s' %i
    createFolder(a)
    for x in range(1,3):
        key = Fernet.generate_key()
        # a = os.urandom(32)
        print (type (key)) 
        # key = b64encode(key).decode('utf-8')
        # print (type(key))
        file1 = open(a + '/%s.key' %x, 'wb') 
        file1.write(key) # The key is type bytes still
        file1.close()