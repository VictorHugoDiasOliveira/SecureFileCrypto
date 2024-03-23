import os
import sys
from cryptography.fernet import Fernet

def verify_if_path_exists(path):
    if os.path.exists(path):
        return True
    return False

def clear_console():
    os.system('clear')

def generate_key(key_path):
    with open(key_path, 'wb') as f:
        f.write(Fernet.generate_key())
    print('Chave gerada com sucesso.')

def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()