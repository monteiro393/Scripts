import random

def boas_vindas():
    print("-"*31)
    print("---   Bem vindo ao jogo de  ---")
    print("--- pedra, papel e tesoura! ---")
    print("-"*31)

def definir_rodadas():
    print("> Quantas rodadas você quer jogar?")
    print("1- Melhor de 3   2- Melhor de 5   3- Outro")
    escolha_total = int(input("> "))
    print()

    quantidade_rodadas = [1, 2, 3]

    while escolha_total not in quantidade_rodadas:
        print("> Erro, selecione novamente:")
        print("1- Melhor de 3   2- Melhor de 5   3- Outro")
        escolha_total = int(input("> "))
        print()

    if(escolha_total == 1):
        limite = 3
    elif(escolha_total == 2):
        limite = 5
    elif(escolha_total == 5):
        limite = int(input("> Defina o numero de rodadas: "))

    return limite

def escolha_mao():
    print("1- Pedra   2- Papel   3- Tesoura")
    mao = int(input("> Selecione sua mão: "))
    print()

    escolha_lista = [1, 2, 3]

    while mao not in escolha_lista:
        print("> Erro, selecione novamente")
        print("1- Pedra   2- Papel   3- Tesoura")
        mao = int(input("> "))
        print()

    return mao

def jogo(limite, mao):
    for rodada in range (1, limite):
        pc = random.randint(1, 3)

        if(pc == 1):    ## PC Pedra
            escolha_pc = "Pedra"
        elif(pc == 2):  ## PC Papel
            escolha_pc = "Papel"
        else:           ## PC Tesoura
            escolha_pc = "Tesoura"

        if(mao == pc):
            print("> Empate!")
    
## WIP