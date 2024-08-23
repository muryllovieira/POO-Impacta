from heranca import Mae, Filha, Neta 

print('Criando obejto de Mae')
mae = Mae(1)

print('\nCriando obejto de Filha')
filha = Filha(1, 2)

print('\nCriando obejto de Neta')
neta = Neta(1, 2, 3)

print('\nVisualizando os objetos')
print('\nmae', vars(mae))
print('\nfilha',vars(filha))
print('\nneta',vars(neta))
