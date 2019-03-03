import os 
import random
import struct
import smtplib
import string
import datetime
import time
import requests
from multiprocessing import Pool
from simplecrypt import encrypt, decrypt

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

files_to_enc = []
key = "PASSWORD"
    
def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    print in_filename
    out_filename = in_filename.split('.')[0]+"."+in_filename.split('.')[1]
    filesize = os.path.getsize(in_filename)
    with open(in_filename,'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            ciphertext = decrypt(key,infile.read())
            outfile.write(ciphertext)

def selectfiles():
    files_to_enc = []
    for root, dirs, files in os.walk("/root/Dokumente/test/"):
        for file in files:
            if file.endswith(".Silcrypt"):
                decrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))

pool = Pool(processes=4)
selectfiles()
