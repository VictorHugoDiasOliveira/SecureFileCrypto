from cryptography.fernet import Fernet
import os

def encrypt_filename(key, filename):
    f = Fernet(key)
    encrypted_filename = f.encrypt(filename.encode())
    return encrypted_filename.decode()

def rename_files_in_directory(directory, key):
    for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)
        if os.path.isfile(original_path):
            encrypted_filename = encrypt_filename(key, filename)
            encrypted_path = os.path.join(directory, encrypted_filename)
            os.rename(original_path, encrypted_path)
            print(f"Arquivo original '{filename}' renomeado para '{encrypted_filename}'")
