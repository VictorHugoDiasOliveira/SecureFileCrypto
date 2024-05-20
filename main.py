import os
from src.utils import verify_if_path_exists, clear_console
from src.key import generate_key, load_key
from src.encrypt_file import encrypt_and_delete_files_in_directory, encrypt_and_delete_file
from src.decrypt_file import decrypt_and_delete_files_in_directory, decrypt_and_delete_file
from src.encrypt_file_name import encrypt_file_names_in_directory
from src.decrypt_file_name import decrypt_file_names_in_directory
from src.interface import form, two_steps_verification, select_path

class KeyManager:
    KEY_PATH = f'/home/{os.getlogin()}/Documents/key.txt'
    ENCRYPTED_KEY_PATH = f'/home/{os.getlogin()}/Documents/key.txt.enc'
    
    def generate_key():
        if verify_if_path_exists(KeyManager.KEY_PATH):
            print('Chave já existente.')
        else:
            generate_key(KeyManager.KEY_PATH)
            clear_console()
            print('Chave gerada com sucesso.')

    def load_key():
        return load_key(KeyManager.KEY_PATH)

    def encrypt_key():
        key = UserInterface.get_key_input()
        if key and two_steps_verification(key):
            encrypt_and_delete_file(KeyManager.KEY_PATH, key)
            clear_console()
            print("Chave criptografada com sucesso!")

    def decrypt_key():
        key = UserInterface.get_key_input()
        if key and two_steps_verification(key):
            decrypt_and_delete_file(KeyManager.ENCRYPTED_KEY_PATH, key)
            clear_console()
            print("Chave descriptografada com sucesso!")

class FileManager:
    def encrypt_files():
        clear_console()
        print("Selecione a pasta que deseja criptografar")
        directory_path = select_path()
        if verify_if_path_exists(directory_path):
            key = UserInterface.get_key_input()
            if key and two_steps_verification(key):
                encrypt_and_delete_files_in_directory(directory_path, key)
                clear_console()
                print("Arquivos criptografados com sucesso!")

    def decrypt_files():
        clear_console()
        print("Selecione a pasta que deseja descriptografar")
        directory_path = select_path()
        if verify_if_path_exists(directory_path):
            key = UserInterface.get_key_input()
            if key and two_steps_verification(key):
                decrypt_and_delete_files_in_directory(directory_path, key)
                clear_console()
                print("Arquivos descriptografados com sucesso!")

    def encrypt_file_names():
        clear_console()
        key = KeyManager.load_key()
        if key:
            print('Selecione a pasta que deseja encriptar os nomes')
            directory_path = select_path()
            encrypt_file_names_in_directory(directory_path, key)
            clear_console()
            print("Nomes criptografados com sucesso!")
        else:
            print("Crie uma chave primeiro.")

    def decrypt_file_names():
        clear_console()
        key = KeyManager.load_key()
        if key:
            print('Selecione a pasta que deseja decriptar os nomes')
            directory_path = select_path()
            decrypt_file_names_in_directory(directory_path, key)
            clear_console()
            print("Nomes descriptografados com sucesso!")
        else:
            print("Crie uma chave primeiro.")

class UserInterface:
    def get_key_input():
        key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
        if len(key) in [16, 24, 32]:
            return key
        else:
            print("A chave precisa ter 16, 24 ou 32 bytes.")
            return None

class Application:
    def run():
        while True:
            decision = form()
            match decision:
                case '1':
                    FileManager.encrypt_files()
                case '2':
                    FileManager.decrypt_files()
                case '3':
                    FileManager.encrypt_file_names()
                case '4':
                    FileManager.decrypt_file_names()
                case '5':
                    KeyManager.generate_key()
                case '6':
                    KeyManager.encrypt_key()
                case '7':
                    KeyManager.decrypt_key()
                case '0':
                    clear_console()
                    break
                case _:
                    clear_console()
                    print('Opção inválida.')

if __name__ == "__main__":
    Application.run()
