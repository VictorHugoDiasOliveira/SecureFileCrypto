import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from src.interface import ApplicationInterface
from src.system import System
from cryptography.fernet import Fernet
from src.key_manager import KeyManager

class FileManager:

    @staticmethod
    def encrypt_and_delete_file(filename, key) -> None:
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

    @staticmethod
    def encrypt_and_delete_files_in_directory() -> None:
        print("Selecione a pasta que deseja criptografar")
        directory_path = ApplicationInterface.select_path()
        if System.verify_if_path_exists(directory_path):
            key = ApplicationInterface.get_key_value()
            if key:
                for filename in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, filename)):
                        FileManager.encrypt_and_delete_file(os.path.join(directory_path, filename), key)
                print("Arquivos criptografados com sucesso!")



    @staticmethod
    def decrypt_and_delete_file(filename, key) -> None:
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

    @staticmethod
    def decrypt_and_delete_files_in_directory() -> None:
        print("Selecione a pasta que deseja descriptografar")
        directory_path = ApplicationInterface.select_path()
        if System.verify_if_path_exists(directory_path):
            key = ApplicationInterface.get_key_value()
            if key:
                for filename in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, filename)) and filename.endswith('.enc'):
                        FileManager.decrypt_and_delete_file(os.path.join(directory_path, filename), key)
                print("Arquivos descriptografados com sucesso!")



    @staticmethod
    def encrypt_file_name(key, filename):
        f = Fernet(key)
        encrypted_filename = f.encrypt(filename.encode())
        return encrypted_filename.decode()
    
    @staticmethod
    def encrypt_file_names_in_directory(keypath) -> None:
        key = KeyManager.read_key(keypath)
        if key:
            print('Select Path')
            directory_path = ApplicationInterface.select_path()
            for filename in os.listdir(directory_path):
                original_path = os.path.join(directory_path, filename)
                if os.path.isfile(original_path):
                    encrypted_filename = FileManager.encrypt_file_name(key, filename)
                    encrypted_path = os.path.join(directory_path, encrypted_filename)
                    os.rename(original_path, encrypted_path)
            print("Nomes criptografados com sucesso!")
        else:
            print("Crie uma chave primeiro.")



    @staticmethod
    def decrypt_filename(key, encrypted_filename):
        f = Fernet(key)
        decrypted_filename = f.decrypt(encrypted_filename.encode())
        return decrypted_filename.decode()

    @staticmethod
    def decrypt_file_names_in_directory(keypath) -> None:
        key = KeyManager.read_key(keypath)
        if key:
            print('Select Path')
            directory_path = ApplicationInterface.select_path()
            for filename in os.listdir(directory_path):
                full_path = os.path.join(directory_path, filename)
                if os.path.isfile(full_path):
                    decrypted_filename = FileManager.decrypt_filename(key, filename)
                    os.rename(full_path, os.path.join(directory_path, decrypted_filename))
            print("Nomes descriptografados com sucesso!")
        else:
            print("Create a key first.")



    @staticmethod
    def generate_key(system) -> None:
        if system.verify_if_path_exists(system.keypath):
            system.clear_console()
            print('Key already exists.')
        else:
            with open(system.keypath, 'wb') as f:
                f.write(Fernet.generate_key())
            system.clear_console()
            print('Key created.')



    @staticmethod
    def encrypt_key(keypath) -> None:
        key = ApplicationInterface.get_key_value()
        if key:
            FileManager.encrypt_and_delete_file(keypath, key)
            print("Chave criptografada com sucesso!")


    @staticmethod
    def decrypt_key(keypath) -> None:
        key = ApplicationInterface.get_key_value()
        if key:
            FileManager.decrypt_and_delete_file(keypath, key)
            print("Chave descriptografada com sucesso!")