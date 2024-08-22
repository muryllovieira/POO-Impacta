#***************
# Objetivo: Criação de Classes e Atributos
# Data: 21/08/2024
# Versão: 1.0
#*****************

################# EXEMPLO #################
# class NomeDaClasse:
#     pass

# objeto_1 = NomeDaClasse()
# objeto_2 = NomeDaClasse()


# objeto_1.atributo_1 = 'valor do atributo 1'


########################################

class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.editoria = 'Nome da editora'
    
    def identidade (self):
        return (f'Sou o livro {self.nome}, e estou salvo'
                f'no endereço de memoria: {id(self)} ')


if __name__ == '__main__':
    livro_1 = Livro('Com amor Simon', 'ELISABETH')
    livro_2 = Livro('Harry Potter', 'JK. ROWLING')

    print('livro 1:', vars(livro_1))
    print(livro_1.nome) 
    print(livro_1.autor)
    #print('livro 2:',vars(livro_2))

