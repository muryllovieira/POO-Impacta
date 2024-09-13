def decorador(f):
    def envelope(p1):
        print('código executado antes de chamar f')
        retorno = f(p1)
        print('código executado após chamar f')
        return retorno
    return envelope


def ola_mundo():
    print('Olá, mundo!')
