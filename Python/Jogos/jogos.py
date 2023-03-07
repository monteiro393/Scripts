import adivinhacao
import forca

def escolha_jogo():

    print()
    print("> Escolha seu jogo")
    print("(1) Forca (2) Adivinhação")
    print()

    jogo = int(input("> "))
    print()

    while(jogo < 1) or (jogo > 2):
        print("> Inválido, selecione novamente")
        jogo = int(input("> "))
        print()

    if(jogo == 1):
        print("> iniciando Jogo da Forca...")
        print()
        forca.jogar()

    elif(jogo == 2):
        print("> Iniciando Jogo de Adivinhação...")
        print()
        adivinhacao.jogar()

if (__name__ == "__main__"): ## se "jogos.py" for o arquivo em foco, executá-lo
    escolha_jogo()