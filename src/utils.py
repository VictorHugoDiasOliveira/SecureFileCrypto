import os
import sys
from cryptography.fernet import Fernet

def verify_if_path_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'A pasta "{directory_path}" nao existe')
        sys.exit()


def generate_key():
    return Fernet.generate_key()

def clear_terminal():
    os.system('clear')