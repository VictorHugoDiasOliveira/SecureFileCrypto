import platform
import os

class System():
    
    clear = ''
    keypath = ''

    def __init__(self) -> None:
        if System.identify_system() == 'Windows':
            System.clear = 'cls'
            System.keypath = f'C:/Users/{os.getlogin()}/Documents/key.txt'
        else:
            System.clear = 'clear'
            System.keypath = f'home/{os.getlogin()}/Documents/key.txt'

    @staticmethod
    def identify_system() -> str:
        return platform.system()
    
    @staticmethod
    def verify_if_path_exists(path) -> bool:
        if os.path.exists(path):
            return True
        return False

    @staticmethod
    def clear_console() -> None:
        os.system(System.clear)