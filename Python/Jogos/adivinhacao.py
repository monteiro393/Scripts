import random

def jogar():    ## definir o código como variável executável
        
    ## variáveis avulsas
    tentativas = None
    pontos = None
    pontos_perdidos = None

    ## variável do número secreto, em int
    numero_secreto = random.randint(0, 50)  ## função para gerar um número aleatório entre 1 e 50

    ## introdução do jogo
    print("-"*41)
    print("--- Bem vindo ao jogo de Adivinhação! ---")
    print("-"*41)
    print()

    print("> Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print()
    dificuldade = int(input("> "))

    while(dificuldade < 1) or (dificuldade > 3): ## caso selecione outra alternativa
        print()
        print("> Inválido, selecione novamente")
        dificuldade = int(input("> "))

    if(dificuldade == 1):   ## fácil
        tentativas = 20
        pontos = 1000
        print()
        print("> Sua pontuação: {}".format(pontos))
    elif(dificuldade == 2): ## médio
        tentativas = 10
        pontos = 2500
        print()
        print("> Sua pontuação: {}".format(pontos))
    else:                   ## difícil
        tentativas = 5
        pontos = 5000
        print()
        print("> Sua pontuação: {}".format(pontos))

    print()

    for rodada in range(1 , tentativas + 1):    ## laço para tentativas restantes
        print("> tentativa {} de {}".format(rodada , tentativas)) ## rodada atual
        print()
        chute = int(input("> Digite um numero de 1 a 50: "))   ## input no terminal em str
        print()

        print("--- Você digitou: {} ---".format(chute))

        ## variáveis de comparação
        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(igual):  ## se for igual
            print()
            print("--- Você acertou! ---")
            print("> Sua pontuação: {}".format(pontos))
            print()
            break
        elif(chute < 1): ## caso digite menor do que 1
            print()
            print("--- Você digitou um número menor do que 1!  ---")
            print()
        elif(chute > 50): ## caso digite maior do que 50
            print()
            print("--- Você digitou um número maior do que 50! ---")
            print()
        else: ## caso digite entre 1 e 50
            print()
            if(maior):      ## se for maior do que o número secreto
                print("> Você errou! O seu chute foi maior do que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute) * 5
                pontos -= pontos_perdidos    ## redução de pontos

            elif(menor):    ## se for menor do que o número secreto
                print("> Você errou! O seu chute foi menor do que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute) * 5
                pontos -= pontos_perdidos    ## redução de pontos
            print()

    print("> O número era {}".format(numero_secreto))
    print()
    print("--- Fim do Jogo ---")
    print()

if(__name__ == "__main__"): ## se "adivinhacao.py" for o arquivo em foco, executá-lo
    jogar()