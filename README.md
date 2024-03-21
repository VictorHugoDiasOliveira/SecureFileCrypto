# Programas de Encriptação e Decriptação

## Visão Geral
Este repositório contém dois programas em Python para encriptar e decriptar arquivos usando o algoritmo AES (Advanced Encryption Standard).

## Pré-requisitos
- Python 3.x instalado
- Biblioteca pycryptodome instalada (você pode instalar executando `pip install pycryptodome` ou `pacman -S python-pycryptodome`)

## Como Usar

### Programa de Encriptação
1. Execute o programa `encrypt.py`.
2. Digite o caminho para a pasta que deseja encriptar quando solicitado.
3. Insira uma chave AES válida quando solicitado (16, 24 ou 32 bytes).
4. Os arquivos na pasta especificada serão encriptados e salvos com a extensão `.enc`.

### Programa de Decriptação
1. Execute o programa `decrypt.py`.
2. Digite o caminho para a pasta que deseja decriptar quando solicitado.
3. Insira a mesma chave AES que você usou para encriptar os arquivos.
4. Os arquivos encriptados na pasta especificada serão decriptados e salvos sem a extensão `.enc`.

## Avisos
- Certifique-se de fazer backup dos arquivos importantes antes de usar estes programas, pois os arquivos serão alterados irreversivelmente.
- Mantenha a chave de criptografia em um local seguro e não a compartilhe com ninguém que você não confie.

## To Do

- Criar a funcao para decriptar os nomes dos arquivos.
- Criar validacoes se os caminhos de fato existem.