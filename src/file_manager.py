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
    def encrypt_and_delete_file(filename: str, key: str) -> None:
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
        System.clear_console()
        print("Select Path")
        directory_path = ApplicationInterface.select_path()
        if System.verify_if_path_exists(directory_path):
            key = ApplicationInterface.get_key_value()
            if key:
                for filename in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, filename)):
                        FileManager.encrypt_and_delete_file(os.path.join(directory_path, filename), key)
                System.clear_console()
                print("Successfully files encrypted!")
            else:
                print("You need a key to proceed")



    @staticmethod
    def decrypt_and_delete_file(filename: str, key: str) -> None:
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
        System.clear_console()
        print("Select Path")
        directory_path = ApplicationInterface.select_path()
        if System.verify_if_path_exists(directory_path):
            key = ApplicationInterface.get_key_value()
            if key:
                for filename in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, filename)) and filename.endswith('.enc'):
                        FileManager.decrypt_and_delete_file(os.path.join(directory_path, filename), key)
                System.clear_console()
                print("Successfully decrypted files!")
            else:
                print("You need a key to proceed")



    @staticmethod
    def encrypt_file_name(key: str, filename: str) -> str:
        f = Fernet(key)
        encrypted_filename = f.encrypt(filename.encode())
        return encrypted_filename.decode()
    
    @staticmethod
    def encrypt_file_names_in_directory(keypath: str) -> None:
        System.clear_console()
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
            print("Successfully encrypted names!")
        else:
            print("You need a key to proceed")



    @staticmethod
    def decrypt_filename(key: str, encrypted_filename: str) -> str:
        f = Fernet(key)
        decrypted_filename = f.decrypt(encrypted_filename.encode())
        return decrypted_filename.decode()

    @staticmethod
    def decrypt_file_names_in_directory(keypath: str) -> None:
        System.clear_console()
        key = KeyManager.read_key(keypath)
        if key:
            print('Select Path')
            directory_path = ApplicationInterface.select_path()
            for filename in os.listdir(directory_path):
                full_path = os.path.join(directory_path, filename)
                if os.path.isfile(full_path):
                    decrypted_filename = FileManager.decrypt_filename(key, filename)
                    os.rename(full_path, os.path.join(directory_path, decrypted_filename))
            print("Successfully decrypted names!")
        else:
            print("You need a key to proceed")



    @staticmethod
    def generate_key(keypath: str) -> None:
        if System.verify_if_path_exists(keypath):
            System.clear_console()
            print('Key already exists.')
        else:
            with open(keypath, 'wb') as f:
                f.write(Fernet.generate_key())
            System.clear_console()
            print('Key created.')



    @staticmethod
    def encrypt_key(keypath: str) -> None:
        System.clear_console()
        key = ApplicationInterface.get_key_value()
        if key:
            FileManager.encrypt_and_delete_file(keypath, key)
            System.clear_console()
            print("Successfully encrypted key!")
        else:
            print("You need a key to proceed")


    @staticmethod
    def decrypt_key(keypath: str) -> None:
        System.clear_console()
        key = ApplicationInterface.get_key_value()
        if key:
            FileManager.decrypt_and_delete_file(keypath, key)
            System.clear_console()
            print("Successfully decrypt key!")
        else:
            print("You need a key to proceed")