# Alysson Matheus de Souza Rodrigues
# Gabriel Barbosa da Silva
# Lucas Rafael da Silva Santos
# Vitor Vinícius Porangaba Torres
# 512
import adivinhacao, forca, imprensadinho, funcoes
def menu1():

        funcoes.imprime_mensagem_abertura('Menu de Jogos')
        print("1. Adivinhação\n2. Forca\n3. Imprensadinho\n4. Sair do menu")

        escolha = input("Qual jogo quer jogar? Digite o número: ")
        while not escolha in '12345':
            escolha = input("Qual jogo quer jogar? Digite o número válido: ")
        if escolha == '1':
            adivinhacao.jogar()
        elif escolha == '2':
            forca.jogar()
        elif escolha == '3':
            imprensadinho.jogar()
        elif escolha == '4':
            print('Fim dos jogos, obrigado por jogar!')

repetir = True
while repetir:
    menu1()
    escolha = input('Você quer escolher outro jogo?\nDigite s/n:')
    if escolha == 'n':
        repetir = False