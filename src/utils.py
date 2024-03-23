import os
import sys

def verify_if_path_exists(path):
    if os.path.exists(path):
        return True
    return False

def clear_console():
    os.system('clear')