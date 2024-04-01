from tkinter import filedialog

def form():
    print('1 - Encriptar Arquivos')
    print('2 - Decriptar Arquivos')
    print('3 - Encriptar Nomes')
    print('4 - Decriptar Nomes')
    print('5 - Gerar chave')
    print('6 - Encriptar chave')
    print('7 - Decriptar chave')
    print('0 - Sair')
    return input('-> ')

def two_steps_verification(password):
    print(f'Tem certeza que deseja prosseguir com a senha utilizada: {password}')
    print('1 - Sim')
    print('2 - Nao')
    decision = input('-> ')
    match decision:
        case '1':
            return True
        case '2':
            return False
        case _:
            print('Opcao invalida, acao cancelada')
            return False

def select_path():
    return filedialog.askdirectory()