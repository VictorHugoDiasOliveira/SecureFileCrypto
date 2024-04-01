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
    two_steps_verification,
    select_path)
import os

KEY_PATH = f'/home/{os.getlogin()}/Documents/key.txt'
ENCRYPTED_KEY_PATH = f'/home/{os.getlogin()}/Documents/key.txt.enc'

while True:
    decision = form()
    match decision:
        case '1':
            clear_console()
            print("Selecione a pasta que deseja criptografar")
            directory_path = select_path()
            if verify_if_path_exists(directory_path):
                key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
                if len(key) not in [16, 24, 32]:
                    print("A chave precisa ter 16, 24 ou 32 bytes.")
                else:
                    if two_steps_verification(key):
                        encrypt_and_delete_files_in_directory(directory_path, key)
                        clear_console()
                        print("Arquivos criptografados com sucesso!")
                    else:
                        continue
            else:
                clear_console()
                print('Pasta nao encontrada.')

        case '2':
            clear_console()
            print("Selecione a pasta que deseja descriptografar")
            directory_path = select_path()
            if verify_if_path_exists(directory_path):
                key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
                if len(key) not in [16, 24, 32]:
                    print("A chave precisa ter 16, 24 ou 32 bytes.")
                else:
                    if two_steps_verification(key):
                        decrypt_and_delete_files_in_directory(directory_path, key)
                        clear_console()
                        print("Arquivos descriptografados com sucesso!")
                    else:
                        continue
            else:
                clear_console()
                print('Pasta nao encontrada.')

        case '3':
            clear_console()
            if os.path.exists(KEY_PATH):
                key = load_key(KEY_PATH)
                print('Selecione a pasta que deseja encriptar os nomes')
                directory_path = select_path()
                encrypt_file_names_in_directory(directory_path, key)
                clear_console()
                print("Nomes criptografados com sucesso!")
            else:
                print("Crie uma chave primeiro.")
                continue

        case '4':
            clear_console()
            if os.path.exists(KEY_PATH):
                key = load_key(KEY_PATH)
                print('Selecione a pasta que deseja decriptar os nomes')
                directory_path = select_path()
                decrypt_file_names_in_directory(directory_path, key)
                clear_console()
                print("Nomes decriptografados com sucesso!")
            else:
                print("Crie uma chave primeiro.")
                continue

        case '5':
            clear_console()
            if verify_if_path_exists(KEY_PATH):
                clear_console()
                print('Chave ja existente.')
            else:
                generate_key(KEY_PATH)
                clear_console()
                print('Chave gerada com sucesso.')

        case '6':
            clear_console()
            key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
            if len(key) not in [16, 24, 32]:
                print("A chave precisa ter 16, 24 ou 32 bytes.")
            else:
                if two_steps_verification(key):
                    encrypt_and_delete_file(KEY_PATH, key)
                    clear_console()
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
                    clear_console()
                    print("Chave criptografada com sucesso!")
                else:
                    continue

        case '0':
            clear_console()
            break

        case _:
            clear_console()
            print('Opcao invalida.')