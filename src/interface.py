from tkinter import filedialog

class ApplicationInterface():

    @staticmethod
    def two_steps_verification(password):
        print(f'Are you sure you want to proceed with the password you used: {password}')
        print('1 - Yes')
        print('2 - No')
        match input('-> '):
            case '1':
                return True
            case '2':
                return False
            case _:
                print('Invalid Option')
                return False

    @staticmethod
    def get_key_value():
        key = input("Digite a chave AES (16, 24 ou 32 bytes): ").encode('utf-8')
        if len(key) in [16, 24, 32]:
            ApplicationInterface.two_steps_verification(key)
            return key
        else:
            print("A chave precisa ter 16, 24 ou 32 bytes.")
            return None
        
    @staticmethod
    def select_path():
        return filedialog.askdirectory()