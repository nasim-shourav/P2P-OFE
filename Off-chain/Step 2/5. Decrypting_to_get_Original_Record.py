from cryptography.fernet import Fernet
import io
import sys
import glob
import os.path

from base64 import b64encode
import os

from Crypto.Cipher import AES
import pyaes


for i in range (1,1001):
    file_name = ('C:/Nasim/P2P/Step 1/Encrypted_Message/Twice/%s' %i + '.encrypted') #change the directory according to your setup
    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i #change the directory according to your setup
    file1 = open(key_dir + '/2.key', 'rb')  
    key = file1.read()
    # print(key)
    file1.close()   
    
    with open(file_name, 'rb') as f:
        data = f.read()
        print ("data", type(data))

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("C:/Nasim/P2P/Step 1/Decrypted_Message/Once/DecO%s.encrypted" %i, 'wb') as f:
        f.write(decrypted)
        f.close()
    key_dir = 'C:/Nasim/P2P/Step 1/Sym_Key/%s' %i
    file1 = open(key_dir + '/1.key', 'rb') 
     
    key = file1.read()
    # print(key)
    file1.close()   
    

    with open("C:/Nasim/P2P/Step 1/Decrypted_Message/Once/DecO%s.encrypted" %i, 'rb') as f:
        data = f.read()
        print ("data", type(data))

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    
    with open("C:/Nasim/P2P/Step 1/Decrypted_Message/Twice/Patient_Record_%s.csv" %i, 'wb') as f:
        f.write(encrypted)
        f.close()

