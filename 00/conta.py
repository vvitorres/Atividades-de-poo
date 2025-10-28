# Vitor Vinícius Porangaba Torres - 512

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self, cliente):
        print(f"Nome: {cliente.nome} \nSonbrenome: {cliente.sobrenome} \nCPF: {cliente.cpf} \nnumero: {self.numero} \nsaldo: {self.saldo}\n")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True