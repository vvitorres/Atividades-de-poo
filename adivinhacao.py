# Alysson Matheus de Souza Rodrigues
# Gabriel Barbosa da Silva
# Lucas Rafael da Silva Santos
# Vitor Vinícius Porangaba Torres
# 512
from funcoes import validacoes, continue_ou_pare, imprime_mensagem_abertura, imprime_nivel_dificuldade, imprime_mensagem_vencedor, imprime_mensagem_perdedor
from random import randint
def jogar():
    imprime_mensagem_abertura("JOGO DE ADIVINHAÇÃO!")
    jogando = True
    while jogando:
        imprime_mensagem_abertura("Dificuldades")
        nivel = imprime_nivel_dificuldade()


        total_de_tentativas = 0
        numero_secreto = randint(0, 100)
        pontos = 1000
        print('o número secreto está de 0 à 100')
        total_de_tentativas += int(24/nivel)


        print('Você tem o total de 1000 pontos')
        rodada = 0
        ganhou = False
        perdeu = False
        while not ganhou and not perdeu:
            rodada += 1
            imprime_mensagem_abertura(f"Tentativa {rodada} de {total_de_tentativas}")
            chute = input('Digite o seu número: ')
            validacao = validacoes(chute,101, -1)
            while not validacao:
                chute = input(f'Numero ou caractere inválido!\nEscolha um numero entre 0 e 100: ')
                validacao = validacoes(chute, 101, -1)
            chute = int(chute)
            pontos -= abs(int(numero_secreto - chute - (chute/100)+(chute/10)+5))
            print('Você digitou: ', chute)
            print('*' * 25)
            print(f'\nVocê tem {pontos} pontos')
            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto
            if acertou:
                print('Você acertou!')
                imprime_mensagem_vencedor()
                ganhou = True
            elif maior:
                print('Você errou! O seu chute foi maior que o número secreto\n')
            elif menor:
                print('Você errou! O seu chute foi menor que o número secreto\n')
            if total_de_tentativas == rodada:
                imprime_mensagem_perdedor()
                perdeu = True
        jogando = continue_ou_pare()
    print('\nFim de jogo.')