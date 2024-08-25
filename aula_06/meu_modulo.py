#***************
# Objetivo: Criação de Modulo em Python
# Data: 25/08/2024
# Versão: 1.0
#*****************


def exibe_nome():
    print(f'O nome deste módulo é: {__name__!r}')



if __name__ == '__main__':
    print('olá')
    nome = input('digite seu nome: ')
    exibe_nome()


