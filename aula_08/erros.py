def incrementa_int(n):
    if not isinstance(n, int):
        raise TypeError('n deve ser um inteiro')
    return n + 1


def calcula_idade(idade):
    nova_idade = incrementa_int(idade)
    print('esse código não é executado se der erro na linha acima')
    return nova_idade


def main():
    print('executando a função principal...')
    resposta = calcula_idade(20.5)
    print('esse código não será executado se der erro na linha acima')
    print('a nova idade é:', resposta)


if __name__ == '__main__':
    print('chamando a função principal')
    main()
    print('esse código não será executado se der erro na linha acima')
