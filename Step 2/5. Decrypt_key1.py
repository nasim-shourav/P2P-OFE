from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii



for i in range (1 , 11):

    with open('E:/Canada/Thesis/P2P-OFE/P2P/Step 1/Encrypted_K1/Bpubk1_%s' %i + '.txt', 'rb') as f:
        Bpubk1 = f.read()
    

    priv_key_dir = 'E:/Canada/Thesis/P2P-OFE/P2P/Step 1/Priv_Pub_Key/%s' %i
    with open(priv_key_dir + '/Private_key_%s' %i + '.pem', "rb") as k:
        key = RSA.importKey(k.read())

    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(Bpubk1)
    decrypted_StrFormat = decrypted.decode("utf-8")
    
    with open('Sym_key/key1_%s' %i + '.key', 'w') as f:
        f.write(decrypted_StrFormat)
        f.close()
    
    print('Decrypted:', decrypted)



