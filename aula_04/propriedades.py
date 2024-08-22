#***************
# Objetivo: Criação de Property e Setter
# Data: 21/08/2024
# Versão: 1.0
#*****************

class Teste:
    def __init__(self):
        self._nome = ''
        self.cont = 0

    @property
    def nome(self):
        self.cont += 1
        print(f'executando a property... {self.cont}')
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        print('executando o setter....')
        self._nome = novo_nome