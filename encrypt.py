import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_and_delete_file(filename, key):
    chunk_size = 64 * 1024
    cipher = AES.new(key, AES.MODE_ECB)
    
    with open(filename, 'rb') as infile:
        plaintext = infile.read()
    
    # Padding do texto claro
    padded_plaintext = pad(plaintext, AES.block_size)
    
    # Encripta o texto claro
    ciphertext = cipher.encrypt(padded_plaintext)
    
    with open(filename + ".enc", 'wb') as outfile:
        outfile.write(ciphertext)

    # Deleta o arquivo que foi encriptado
    os.remove(filename)

def encrypt_and_delete_files_in_directory(directory, key):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            encrypt_and_delete_file(os.path.join(directory, filename), key)

if __name__ == "__main__":
    directory_path = input("Digite o caminho para a pasta que deseja criptografar: ")
    if not os.path.exists(directory_path):
        print(f'A pasta "{directory_path}" nao existe')
        sys.exit()
    key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
    if len(key) not in [16, 24, 32]:
        print("A chave precisa ter 16, 24 ou 32 bytes.")
    else:
        encrypt_and_delete_files_in_directory(directory_path, key)
        print("Arquivos criptografados com sucesso!")
