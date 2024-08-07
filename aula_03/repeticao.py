#***************
# Objetivo: Relembrar estrutura de repetição 
# Data: 06/08/2024
# Versão: 1.0
#*****************

n = int(input('Digite um número: '))

cont = 0

while cont < n:
    print(cont)
    cont += 1

print('fim while')


for cont2 in range(n):
    print(cont2)

print('fim for')
