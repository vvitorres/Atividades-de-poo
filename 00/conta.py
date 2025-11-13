# Vitor Vinícius Porangaba Torres - 512

import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self, conta):
        print(f"\nData abertura da conta {conta.numero}: {self.data_abertura}")
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    __slots__ = ['_numero', '_cliente', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite = 2000.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def imprime_hitorico(self):
        self.historico.imprime(self)

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor} em {datetime.datetime.today()}")

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"saque de {valor}")
            return True
            
    def extrato(self):
        print(f"Nome: {self.cliente.nome} \nSonbrenome: {self.cliente.sobrenome} \nCPF: {self.cliente.cpf} \nNumero: {self.numero} \nSaldo: {self.saldo}\n")
        self.historico.transacoes.append(f"tirou extrato em {datetime.datetime.today()} - saldo de {self.saldo}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")
            return True