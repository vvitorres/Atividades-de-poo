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
    __slots__ = ['_numero', '_cliente', '_saldo', '_limite', '_historico', '_identificador']
    identificador = 1
    def __init__(self, numero, cliente, saldo, limite = 2000.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._identificador = Conta.identificador
        Conta.identificador += 1

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

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
    
    def __str__(self):
        return f"Dados da Conta: \nNumero: {self._numero} \nTitular: {self._cliente} \nSaldo: {self._limite} \nLimite:{self._saldo}"

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        return super().atualiza(taxa * 2)
        

    def deposita(self, valor):
        self._saldo += valor - 0.10
        
class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        return super().atualiza(taxa * 3)

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
        #propriedades
    def roda(self, conta):
        print(f"Saldo da Conta: {conta.saldo}")
        self._saldo_total += conta.atualiza(self._selic)
        print(f"Saldo Final: {self._saldo_total}")

class Banco:
    def __init__(self):
        self._lista_contas = []

    def adiciona(self, conta):
        self._lista_contas.append(conta)
    
    def pega_Conta(self, posicao_conta):
        return self._lista_contas[posicao_conta]

    @property
    def pegaTotalDeCOntas(self):
        n = 0
        for _ in self._lista_contas:
            n += 1
        return f'O número total de contas é: {n}'
        
if __name__ == '__main__':
    c = Conta('123-4', 'Vitor', 1000.0)
    cc = ContaCorrente('123-5', 'Vinícius', 2000.0)
    cc2 = ContaCorrente('123-6', 'porangaba', 4000.0)
    cp = ContaPoupanca('123-7', 'Torres', 3000.0)
    adc = AtualizadorDeContas(0.02)
    banco = Banco()
    banco.adiciona(c)
    banco.adiciona(cc)
    banco.adiciona(cc2)
    banco.adiciona(cp)
    print(banco.pega_Conta(0))
    print(banco.pegaTotalDeCOntas)
    for i in banco._lista_contas:
        adc.roda(i)


'''
    
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    print(f'Saldo total: {adc._saldo_total}') # O saldo final é sempre igual ao saldo total
      
if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)
    print(cc)
'''