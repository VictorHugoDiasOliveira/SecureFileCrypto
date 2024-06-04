from cryptography.fernet import Fernet

class KeyManager:

    @staticmethod
    def read_key(key_file):
        with open(key_file, 'rb') as f:
            return f.read()