from cryptography.fernet import Fernet
import os

# Gerar uma chave para criptografia
def generate_key():
    return Fernet.generate_key()

# Carregar a chave de um arquivo ou gerar uma nova se o arquivo não existir
def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return key

# Criptografar o nome do arquivo
def encrypt_filename(key, filename):
    f = Fernet(key)
    encrypted_filename = f.encrypt(filename.encode())
    return encrypted_filename.decode()

# Descriptografar o nome do arquivo
def decrypt_filename(key, encrypted_filename):
    f = Fernet(key)
    decrypted_filename = f.decrypt(encrypted_filename.encode())
    return decrypted_filename.decode()

# Renomear um arquivo com o nome criptografado
def rename_files_in_directory(directory, key):
    for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)
        if os.path.isfile(original_path):
            encrypted_filename = encrypt_filename(key, filename)
            encrypted_path = os.path.join(directory, encrypted_filename)
            os.rename(original_path, encrypted_path)
            print(f"Arquivo original '{filename}' renomeado para '{encrypted_filename}'")

# Exemplo de uso
if __name__ == "__main__":
    # Diretório onde os arquivos estão localizados
    directory = "caminho/para/sua/pasta"

    # Carregar ou gerar uma chave de criptografia
    key_file = "key.key"
    key = load_key(key_file)

    # Renomear todos os arquivos na pasta com os nomes criptografados
    rename_files_in_directory(directory, key)
