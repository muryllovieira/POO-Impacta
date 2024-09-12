import _csv

colunas = ['Descrição', 'Potência (Watts)', 'Tensão (Volts)',
           'Quantidade em estoque', 'Preço (R$)'
]
estoque = [
    ['Liquidificador 5 velocidades', 800, 220, 8, 259.99],
    ['Geladeira 350 litros', 75, 110, 4, 1372.99],
    ['Microondas 20 litros', 1500, 220, 21, 499.99],
]


with open('estoque.csv', 'w', newline='',
          encoding='utf-8') as arquivo_csv:
    escritor = _csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(estoque)

with open('estoque.csv', 'r', newline='',
          encoding='utf-8') as arquivo_csv:
    leitor = _csv.reader(arquivo_csv, delimiter=';')
    novo_estoque = []
    for linha in leitor:
        novo_estoque.append(linha)


novas_colunas, *novo_estoque = novo_estoque         # 1
print(novas_colunas)
print('[', *novo_estoque, sep='\n  ', end='\n]') 
