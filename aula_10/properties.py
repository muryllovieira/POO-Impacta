class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def _get_nome(self):
        return self._nome

    def _set_nome(self, novo_nome):
        self._nome = novo_nome
    
    nome = property(_get_nome, _set_nome)


class Pessoa2:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
