import os
import sys
from cryptography.fernet import Fernet

def verify_if_path_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'A pasta "{directory_path}" nao existe')
        sys.exit()

def clear_terminal():
    os.system('clear')

def generate_key():
    return Fernet.generate_key()

def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    # else:
    #     key = generate_key()
    #     with open(key_file, 'wb') as f:
    #         f.write(key)
    #     return key