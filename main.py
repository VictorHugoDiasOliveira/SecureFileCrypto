from src.encrypt_file import encrypt_and_delete_files_in_directory
from src.decrypt_file import decrypt_and_delete_files_in_directory
from src.utils import verify_if_path_exists
from src.utils import generate_key
from src.utils import clear_terminal
from src.utils import load_key
from src.encrypt_file_name import encrypt_file_names_in_directory
from src.decrypt_file_name import decrypt_file_names_in_directory
import os

print('1 - Encriptar Arquivos')
print('2 - Decriptar Arquivos')
print('3 - Encriptar Nomes')
print('4 - Decriptar Nomes')
print('5 - Gerar chave')
decision = input('-> ')

match decision:
    case '1':
        clear_terminal()

        directory_path = input("Digite o caminho para a pasta que deseja criptografar: ")
        if verify_if_path_exists(directory_path):
            key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')

            if len(key) not in [16, 24, 32]:
                print("A chave precisa ter 16, 24 ou 32 bytes.")

            else:
                encrypt_and_delete_files_in_directory(directory_path, key)
                print("Arquivos criptografados com sucesso!")
        else:
            print('Pasta nao encontrada.')

    case '2':
        clear_terminal()

        directory_path = input("Digite o caminho para a pasta que deseja descriptografar: ")
        if verify_if_path_exists(directory_path):
            key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')

            if len(key) not in [16, 24, 32]:
                print("A chave precisa ter 16, 24 ou 32 bytes.")

            else:
                decrypt_and_delete_files_in_directory(directory_path, key)
                print("Arquivos descriptografados com sucesso!")
        else:
            print('Pasta nao encontrada.')

    case '3':
        clear_terminal()

        key_path = '/home/mamada/Documents/Secure/key.txt'
        key = load_key(key_path)

        directory_path = input('Digite o caminho para a pasta que deseja encriptar: ')
        encrypt_file_names_in_directory(directory_path, key)
        print("Nomes criptografados com sucesso!")

    case '4':
        clear_terminal()

        key_path = '/home/mamada/Documents/Secure/key.txt'
        key = load_key(key_path)

        directory_path = input('Digite o caminho para a pasta que deseja decriptar: ')
        decrypt_file_names_in_directory(directory_path, key)
        print("Nomes decriptografados com sucesso!")

    case '5':
        clear_terminal()

        key_path = '/home/mamada/Documents/Secure/key.txt'

        if verify_if_path_exists(key_path):
            print('Chave ja existente.')
        else:
            generate_key(key_path)

    case _:
        print('Opcao invalida, finalizando programa...')