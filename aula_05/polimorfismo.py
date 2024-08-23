#***************
# Objetivo: Polimorfismo em Python
# Data: 23/08/2024
# Versão: 1.0
#*****************

# Sobrecarga
def sobrecarga(nome, numero=10):
    print(nome)
    if numero:
        print(numero)

print('Primeira Execução')
sobrecarga('Muryllo')

print('\nSegunda Execução')
sobrecarga('Muryllo', 10)
