from src.encrypt import encrypt_and_delete_files_in_directory
from src.decrypt import decrypt_and_delete_files_in_directory
from src.utils import verify_if_path_exists
from src.utils import generate_key
from src.utils import clear_terminal

print('1 - Encriptar')
print('2 - Decriptar')
print('3 - Gerar chave fernet')
decision = input('-> ')

if decision == '1':
    clear_terminal()

    directory_path = input("Digite o caminho para a pasta que deseja criptografar: ")
    verify_if_path_exists(directory_path)

    key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')

    if len(key) not in [16, 24, 32]:
        print("A chave precisa ter 16, 24 ou 32 bytes.")

    else:
        encrypt_and_delete_files_in_directory(directory_path, key)
        print("Arquivos criptografados com sucesso!")

elif decision == '2':
    clear_terminal()

    directory_path = input("Digite o caminho para a pasta que deseja descriptografar: ")
    verify_if_path_exists(directory_path)

    key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')

    if len(key) not in [16, 24, 32]:
        print("A chave precisa ter 16, 24 ou 32 bytes.")

    else:
        decrypt_and_delete_files_in_directory(directory_path, key)
        print("Arquivos descriptografados com sucesso!")

elif decision == '3':
    clear_terminal()
    print(generate_key())

else:
    print('Opcao invalida, finalizando programa...')