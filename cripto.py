#Vitor Vinícius Porangaba Torres
from funcoes0 import validacoes, criptografia, continue_ou_pare, escolha_nivel_palavras, escolha_nivel_dicas, imprime_mensagem_abertura
from random import randint
def jogar():
    jogando = True
    while jogando:
        imprime_mensagem_abertura('Bem vindo Ao jogo da Criptografia!')
        imprime_mensagem_abertura('Dificuldades')
        nivel_l = ['NÍVEL FÁCIL', 'NÍVEL MÉDIO', 'NÍVEL DIFÍCIL']
        for n in range(3):
            print(f'*{f"{n + 1} = {nivel_l[n]}":<28}*')
        print('*' * 30)
        nivel = '0'
        while not nivel in '123':
            nivel = input('\nDigite o número válido do nível que você deseja jogar:')
        print('\n')
        #variáveis
        dicas = []
        palavras = []
        dicas_1 = escolha_nivel_dicas(nivel)
        palavras_1 = escolha_nivel_palavras(nivel)

        for sorteio in range(10):
            n = -1
            for contador in dicas_1:
                n += 1
            if n < 0:
                print('O histórico de palavras acabou, reinicie o jogo!')
                break
            elemento_sorteado = randint(0, n)
            palavras.append(palavras_1.pop(elemento_sorteado))
            dicas.append(dicas_1.pop(elemento_sorteado))

        casas = []
        indice_letras = {}
        letras_usadas = ''
        numeros = -1
        caracteres = []
        numeros_chutados = ''
        letras_chutadas = ' '

        for palavra in palavras:
            caracteres.append(len(palavra))
            for letras in palavra:
                if letras in letras_usadas:
                    n = 0
                    for letra in letras_usadas:
                        if letras == letra:
                            casas.append(n)
                            indice_letras[n] = letras
                        n += 1
                    continue
                numeros += 1
                indice_letras[numeros] = letras
                casas.append(numeros)
                letras_usadas = letras_usadas + letras

        ganhou = False
        perdeu = False
        acertos = numeros
        erros = 0
        while not ganhou and not perdeu:
            if int(nivel) < 3:
                print('Intruçoes:\n1- Desconsidere os acentos das palavras;\n2- Primeiro você escolhe o número que está na posição desejada,\ndepois você digita a letra desejada.')
            if int(nivel) == 3:
                print('\nIntruçoes:\n1- considere os acentos das palavras;\n2- Primeiro você escolhe o número que está na posição desejada,\ndepois você digita a letra desejada.')
            criptografia(dicas, casas, caracteres)
            print(f'\nVocê pode errar {5 - erros} vezes.')

            escolha = input('Digite o número da posição da letra que você quer chutar: ')
            validacao = validacoes(escolha, numeros+2, -1, numeros_chutados)
            while not validacao:
                escolha = input('Escolha um número que esteja sendo apresentado: ')
                validacao = validacoes(escolha, numeros+2, -1, numeros_chutados)
            escolha = int(escolha)

            chute = input('Digite a letra: ')
            while chute in letras_chutadas:
                chute = input('Digite uma letra que não tenha sido chutada: ')
            validacao2 = validacoes(chute, 101, -1)
            while validacao2:
                chute = input('Escolha uma letra em vez de um número: ')
                validacao2 = validacoes(chute, 101, -1)
            if indice_letras[escolha].upper() == chute.upper():
                numeros_chutados = numeros_chutados + str(escolha) + ' '
                letras_chutadas = letras_chutadas + chute
                acertos -= 1
                posicao_chute = -1
                for casa in casas:
                    posicao_chute += 1
                    if casa == escolha:
                        casas[posicao_chute] = chute.upper()
            else:
                erros += 1
            if not chute in letras_usadas:
                letras_chutadas = letras_chutadas + chute
            if erros == 6:
                perdeu = True
                print('Que pena, você perdeu!')
            elif acertos == -1:
                ganhou = True
                criptografia(dicas, casas, caracteres)
                print('\nParabens, você ganhou!')
        palavras.clear()
        dicas.clear()
        jogando = continue_ou_pare()
    print('Fim de jogo')