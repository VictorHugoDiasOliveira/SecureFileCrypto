from src.utils import (
    verify_if_path_exists,
    clear_console)
from src.key import (
    generate_key,
    load_key)
from src.encrypt_file import (
    encrypt_and_delete_files_in_directory,
    encrypt_and_delete_file)
from src.decrypt_file import (
    decrypt_and_delete_files_in_directory,
    decrypt_and_delete_file)
from src.encrypt_file_name import encrypt_file_names_in_directory
from src.decrypt_file_name import decrypt_file_names_in_directory
from src.interface import (
    form,
    two_steps_verification)
import os

KEY_PATH = f'/home/{os.getlogin()}/Documents/Secure/key.txt'
ENCRYPTED_KEY_PATH = f'/home/{os.getlogin()}/Documents/Secure/key.txt.enc'

while True:
    decision = form()
    match decision:
        case '1':
            clear_console()
            directory_path = input("Digite o caminho para a pasta que deseja criptografar: ")
            if verify_if_path_exists(directory_path):
                key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
                if len(key) not in [16, 24, 32]:
                    print("A chave precisa ter 16, 24 ou 32 bytes.")
                else:
                    if two_steps_verification(key):
                        encrypt_and_delete_files_in_directory(directory_path, key)
                        print("Arquivos criptografados com sucesso!")
                    else:
                        continue
            else:
                print('Pasta nao encontrada.')

        case '2':
            clear_console()
            directory_path = input("Digite o caminho para a pasta que deseja descriptografar: ")
            if verify_if_path_exists(directory_path):
                key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
                if len(key) not in [16, 24, 32]:
                    print("A chave precisa ter 16, 24 ou 32 bytes.")
                else:
                    if two_steps_verification(key):
                        decrypt_and_delete_files_in_directory(directory_path, key)
                        print("Arquivos descriptografados com sucesso!")
                    else:
                        continue
            else:
                print('Pasta nao encontrada.')

        case '3':
            clear_console()
            key = load_key(KEY_PATH)
            directory_path = input('Digite o caminho para a pasta que deseja encriptar: ')
            encrypt_file_names_in_directory(directory_path, key)
            print("Nomes criptografados com sucesso!")

        case '4':
            clear_console()
            key = load_key(KEY_PATH)
            directory_path = input('Digite o caminho para a pasta que deseja decriptar: ')
            decrypt_file_names_in_directory(directory_path, key)
            print("Nomes decriptografados com sucesso!")

        case '5':
            clear_console()
            if verify_if_path_exists(KEY_PATH):
                print('Chave ja existente.')
            else:
                generate_key(KEY_PATH)

        case '6':
            clear_console()
            key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
            if len(key) not in [16, 24, 32]:
                print("A chave precisa ter 16, 24 ou 32 bytes.")
            else:
                if two_steps_verification(key):
                    encrypt_and_delete_file(KEY_PATH, key)
                    print("Chave criptografada com sucesso!")
                else:
                    continue

        case '7':
            clear_console()
            key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
            if len(key) not in [16, 24, 32]:
                print("A chave precisa ter 16, 24 ou 32 bytes.")
            else:
                if two_steps_verification(key):
                    decrypt_and_delete_file(ENCRYPTED_KEY_PATH, key)
                    print("Chave criptografada com sucesso!")
                else:
                    continue

        case '0':
            clear_console()
            break

        case _:
            clear_console()
            print('Opcao invalida.')