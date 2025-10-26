# Alysson Matheus de Souza Rodrigues
# Gabriel Barbosa da Silva
# Lucas Rafael da Silva Santos
# Vitor Vinícius Porangaba Torres
# 512
from funcoes import validacoes , continue_ou_pare, imprime_mensagem_abertura, imprime_mensagem_vencedor, imprime_mensagem_perdedor
import random
def jogar(): # (opcional)
    imprime_mensagem_abertura("Bem vindo ao jogo do imprensadinho!")

    jogando = True # (opcional) Variável para manter o jogo em loop até onde o usuário quiser
    while jogando:
        intervalo_maior = 100 #variável que vai armazenar o numero caso ele seja maior que o número sorteado
        intervalo_menor = 1   #variável que vai armazenar o numero caso ele seja menor que o número sorteado
        numero_secreto = random.randint(intervalo_menor + 1, intervalo_maior - 1) # sortear um número de 2 até 99

        ganhou = False  #|Variáveis opcionais, são boas para caso tenha incrementações futuras, mas precisa ao menos de uma variável
        perdeu = False  #|
        print('(obs: não escolha o menor nem o maior número do intervalo)') # Aviso de uma regra do jogo
        while not ganhou and not perdeu: # inicio do jogo
            numero_escolhido = input(f'Escolha um numero entre {intervalo_menor} e {intervalo_maior}: ') # Saida
#########################################################################################################################################
            validacao = validacoes(numero_escolhido, intervalo_maior, intervalo_menor)
            while not validacao:
                numero_escolhido = input(f'Numero ou caractere inválido!\nEscolha um numero entre {intervalo_menor} e {intervalo_maior}: ')
                validacao = validacoes(numero_escolhido, intervalo_maior, intervalo_menor)
            numero_escolhido = int(numero_escolhido)
#########################################################################################################################################|
            if numero_escolhido == numero_secreto: # Caso o número escolhido seja igual ao número secreto o usuário perde e o jogo acaba
                imprime_mensagem_perdedor() # mensagem que o usuário perdeu
                perdeu = True # encerra o loop do jogo
            elif numero_secreto < numero_escolhido:  #|
                intervalo_maior = numero_escolhido   #|intervalo dos números
            elif numero_secreto > numero_escolhido:  #|
                intervalo_menor = numero_escolhido   #|
            if (intervalo_menor + 1) == numero_secreto and (intervalo_maior - 1) == numero_secreto: # "if" para detectar se o usuário ganhou
                imprime_mensagem_vencedor() # mensagem que o usuário ganhou o jogo
                ganhou = True # encerra o loop do jogo

        jogando = continue_ou_pare()
    print('Fim de jogo!') # mensagem que o jogo finalizou