# Vitor Vinícius Porangaba Torres - 512

import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
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
    def __init__(self, numero, cliente, saldo, limite = 2000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor} em {datetime.datetime.today()}")

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
            self.historico.transacoes.append(f"saque de {valor}")

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