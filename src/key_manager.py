class KeyManager:

    @staticmethod
    def read_key(key_file: str) -> bytes:
        try:
            with open(key_file, 'rb') as f:
                return f.read()
        except:
            print(f"{key_file} does not exist")