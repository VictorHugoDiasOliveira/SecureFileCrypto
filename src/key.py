import os
from cryptography.fernet import Fernet

def generate_key(key_path):
    with open(key_path, 'wb') as f:
        f.write(Fernet.generate_key())

def load_key(key_file):
    with open(key_file, 'rb') as f:
        return f.read()