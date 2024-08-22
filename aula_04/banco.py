#***************
# Objetivo: Criação de Métodos
# Data: 21/08/2024
# Versão: 1.0
#*****************

class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    # Método acessor
    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0 :
            return 'Valor deve ser positivo'
        self.__saldo += valor
        return 'Deposito realizado com sucesso'

    def sacar(self, valor):
        if valor < 0 :
            return 'Valor deve ser positivo'
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        self.__saldo -= valor
        return 'Saque realizado com sucesso'


if __name__ == '__main__':
    c1 = Conta(1, 'Muryllo')