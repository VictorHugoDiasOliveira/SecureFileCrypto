from tkinter import filedialog

class ApplicationInterface():

    @staticmethod
    def two_steps_verification(password: str) -> bool:
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
    def get_key_value() -> bytes|None:
        key = input("Enter the AES key (16, 24 or 32 bytes): ").encode('utf-8')
        if len(key) in [16, 24, 32]:
            ApplicationInterface.two_steps_verification(key)
            return key
        else:
            print("The key must be 16, 24 or 32 bytes.")
            return None
        
    @staticmethod
    def select_path() -> str:
        return filedialog.askdirectory()