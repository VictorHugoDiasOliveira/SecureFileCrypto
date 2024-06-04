from src.system import System
from src.file_manager import FileManager

if __name__ == "__main__":
    system = System()
    while True:
        print('1 - Encrypt Files')
        print('2 - Decrypt Files')
        print('3 - Encrypt File Names')
        print('4 - Decrypt File Names')
        print('5 - Generate Key')
        print('6 - Encrpyt Key')
        print('7 - Decrypt Key')
        print('0 - Exit')
        match input('-> '):
            case '1':
                FileManager.encrypt_and_delete_files_in_directory()
            case '2':
                FileManager.decrypt_and_delete_files_in_directory()
            case '3':
                FileManager.encrypt_file_names_in_directory(system.keypath)
            case '4':
                FileManager.decrypt_file_names_in_directory(system.keypath)
            case '5':
                FileManager.generate_key(system.keypath)
            case '6':
                FileManager.encrypt_key(system.keypath)
            case '7':
                FileManager.decrypt_key(f'{system.keypath}.enc')
            case '0':
                break
            case _:
                print('Invalid Option')