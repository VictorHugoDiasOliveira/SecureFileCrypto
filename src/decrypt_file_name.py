from cryptography.fernet import Fernet
import os

def decrypt_filename(key, encrypted_filename):
    f = Fernet(key)
    decrypted_filename = f.decrypt(encrypted_filename.encode())
    return decrypted_filename.decode()

def decrypt_file_names_in_directory(directory, key):
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            decrypted_filename = decrypt_filename(key, filename)
            os.rename(full_path, os.path.join(directory, decrypted_filename))