# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:27:30 2024

@author: Daniel Akey
"""

from datetime import datetime
import time
import string
import random

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


class AccessKey(object):    
    def __init__(self):
        self.status = self.check_status()
        self.key_plain = ''.join(random.sample(string.ascii_letters, 5))
        self.key_encrypted = self.encrypt()
        self.proc_date = datetime.now()
        self.proc_date_formatted = self.proc_date.strftime('%Y-%m-%d') # %H:%M:%S')
        self.exp_date = datetime(2025,1,12)
        self.exp_date_formatted = self.exp_date.strftime('%Y-%m-%d')
        self.id = None
        
    def encrypt(self):
        k = str(random.randint(100, 999))
        self.key_encrypted = self.key_plain + k
        return self.key_encrypted
    
    def decrypt(self):
        self.key_plain = self.key_encrypted[:-3]
        print(self.key_plain)
        return self.key_plain
        
    def check_status(self):
        l = ['Active', 'Expired', 'Revoked']
        return random.sample(l, 1)[0]
    
    def __str__(self):
        return self.key_encrypted
    

# Generate Public key and private key
key = RSA.generate(2048)
private_key = key.export_key()
with open('private.pem', 'wb') as f:
    f.write(private_key)

public_key = key.public_key().export_key()
with open('receiver.pem', 'wb') as f:
    f.write(public_key)

k = AccessKey()
data = k.key_plain

recipient_key = RSA.import_key(open('receiver.pem').read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode('utf8'))

with open('encrypted_data.bin', 'wb') as f:
    f.write(enc_session_key)
    f.write(cipher_aes.nonce)
    f.write(tag)
    f.write(ciphertext)
