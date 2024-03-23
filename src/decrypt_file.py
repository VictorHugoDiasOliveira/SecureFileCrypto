import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from src.utils import verify_if_path_exists

def decrypt_and_delete_file(filename, key):
    cipher = AES.new(key, AES.MODE_ECB)
    
    with open(filename, 'rb') as infile:
        ciphertext = infile.read()
    
    # Desencripta o texto cifrado
    plaintext = cipher.decrypt(ciphertext)
    
    # Remove o padding do texto
    unpadded_plaintext = unpad(plaintext, AES.block_size)
    
    with open(filename[:-4], 'wb') as outfile:
        outfile.write(unpadded_plaintext)

    # Deletando o arquivo encriptado
    os.remove(filename)

def decrypt_and_delete_files_in_directory(directory, key):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and filename.endswith('.enc'):
            decrypt_and_delete_file(os.path.join(directory, filename), key)

if __name__ == "__main__":
    directory_path = input("Digite o caminho para a pasta que deseja descriptografar: ")
    verify_if_path_exists(directory_path)

    key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')

    if len(key) not in [16, 24, 32]:
        print("A chave precisa ter 16, 24 ou 32 bytes.")

    else:
        decrypt_and_delete_files_in_directory(directory_path, key)
        print("Arquivos descriptografados com sucesso!")
