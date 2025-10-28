# Vitor Vinícius Porangaba Torres - 512

from conta import Conta
conta1 = Conta('123-45', 'Vini', 120.0, 1000.0)
conta2 = Conta('678-90', 'Vitor', 300.0, 2000.0)

conta1.deposita(100)
conta1.extrato()
conta1.saca(200)
conta1.extrato()
conta2.deposita(50)
conta2.extrato()
conta2.saca(300)
conta2.extrato()
conta1.transfere_para(conta2, 20)
conta1.extrato()
conta2.extrato()