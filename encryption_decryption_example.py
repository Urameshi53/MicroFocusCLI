from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from accesskey import AccessKey

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

private_key = RSA.import_key(open('private.pem').read())

with open('encrypted_data.bin', 'rb') as f:
    enc_session_key = f.read(private_key.size_in_bytes())
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode('utf-8'))