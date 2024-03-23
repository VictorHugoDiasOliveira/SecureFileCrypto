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

KEY_PATH = '/home/mamada/Documents/Secure/key.txt'
ENCRYPTED_KEY_PATH = '/home/mamada/Documents/Secure/key.txt.enc'

print('1 - Encriptar Arquivos')
print('2 - Decriptar Arquivos')
print('3 - Encriptar Nomes')
print('4 - Decriptar Nomes')
print('5 - Gerar chave')
print('6 - Encriptar chave')
print('7 - Decriptar chave')
decision = input('-> ')

match decision:
    case '1':
        clear_console()
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
        clear_console()
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
            encrypt_and_delete_file(KEY_PATH, key)
            print("Chave criptografada com sucesso!")

    case '7':
        clear_console()
        key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
        if len(key) not in [16, 24, 32]:
            print("A chave precisa ter 16, 24 ou 32 bytes.")
        else:
            decrypt_and_delete_file(ENCRYPTED_KEY_PATH, key)
            print("Chave criptografada com sucesso!")

    case _:
        print('Opcao invalida, finalizando programa...')