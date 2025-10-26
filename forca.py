# Alysson Matheus de Souza Rodrigues
# Gabriel Barbosa da Silva
# Lucas Rafael da Silva Santos
# Vitor Vinícius Porangaba Torres
# 512

import funcoes

def jogar():
    jogando = True
    while jogando:
        funcoes.imprime_mensagem_abertura('Bem vindo ao jogo da forca!')
        funcoes.carrega_palavra_secreta()

        palavra_secreta, dica = funcoes.carrega_palavra_secreta()

        letras_acertadas = funcoes.inicializa_letras_acertadas(palavra_secreta)
        letras_chutadas = []
        letras_erradas = []

        acertou = False
        enforcou = False
        erros = 0
        max_erros = 6
        funcoes.forca(erros)
        print(' '.join(letras_acertadas))
        while not acertou and not enforcou:
            chute = funcoes.pede_chute()
            validacao = funcoes.validacoes(chute, 100, -1, None, letras_chutadas)
            while validacao:
                chute = input('O seu chute é inválido ou é uma letra já chutada.\nDigite uma letra válida: ')
                validacao = funcoes.validacoes(chute, 100, -1, None, letras_chutadas)
            if (len(chute)) > 1:
                if chute == palavra_secreta:
                    acertou = True
                else:
                    acertou = False
                    enforcou = True

            else:
                letras_chutadas.append(chute)
                if chute in palavra_secreta:
                    letras_acertadas = funcoes.marca_chute_correto(chute, letras_acertadas, palavra_secreta)

                else:
                    erros += 1
                    letras_erradas.append(chute)
                acertou = '_' not in letras_acertadas
                enforcou = erros == max_erros
                funcoes.forca(erros)
                print(' '.join(letras_acertadas))
                if len(letras_erradas) > 0:
                    print(f'Letras erradas: {" - ".join(letras_erradas)}')
                    print(f'{max_erros - erros} chances restantes.')
                    if max_erros - erros == 1:
                        print(dica)
        if acertou:
            funcoes.imprime_mensagem_vencedor()
        else:
            funcoes.imprime_mensagem_perdedor(palavra_secreta)
        jogando = funcoes.continue_ou_pare()
    print('Fim do jogo')