#***************
# Objetivo: Herança em Python
# Data: 23/08/2024
# Versão: 1.0
#*****************

class Mae:  # MAMIFERO
    def __init__(self, p1):
        print('executando o init da Mae')
        self.p1 = p1

class Filha(Mae):   # FELINO
     def __init__(self, p1, p2):
        print('executando o init da Filha')
        self.p2 = p2
        super().__init__( p1)

class Neta(Filha):   # GATO
     def __init__(self, p1, p2, p3):
        print('executando o init da Neta')
        self.p3 = p3
        super().__init__(p1, p2)

