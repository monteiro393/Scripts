import random

def jogar():    ## definir o código como variável executável

    boas_vindas_jogo()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]   ## susbtitui "_" para cada letra na palavra secreta

    ## variáveis avulsas
    
    enforcou = False
    acertou = False
    tentativas = 7      ## número de tentativas

    print("> Tentativas restantes {}".format(tentativas))
    print()
    print(letras_acertadas)
    print()

    lista_chutes = []   ## lista com os chutes

    while(not enforcou and not acertou):    ## loop que verifica se não acabaram as tentativas ou se não acertou
        chute = input_do_chute()


        if(chute in palavra_secreta):   ## verifica se o chute está contido na palavra
            verifica_chute_correto(tentativas, palavra_secreta, chute, letras_acertadas)

        else:
            tentativas -= 1
            verifica_chute_incorreto(tentativas, lista_chutes, chute)

        enforcou = tentativas == 0              ## enforca se as tentativas zerarem
        acertou = "_" not in letras_acertadas   ## vence se não houver mais espaços em branco nas palavras

        print(letras_acertadas)
        print()
        print("> Seus chutes incorretos: {}".format(lista_chutes))
        print()


    if(acertou):
        print("> Você venceu!")
    else:
        perdeu(palavra_secreta)


    print()
    print("--- Fim do Jogo ---")
    print()

def boas_vindas_jogo():
    print("-"*35)
    print("--- Bem vindo ao jogo da Forca! ---")
    print("-"*35)
    print()

def carregar_palavra_secreta():
    ## importar o arquivo de texto com as palavras, em modo de leitura "r"
    with open(r"C:\Users\FT0152\Desktop\MInhas Coisas\André\Scripts\Python\Jogos\palavras.txt", "r") as arquivo:
        palavras = []   ## inicializar uma lista
    
        for linha in arquivo:   ## definir uma variável 'linha' e fazer um loop para "ler" o arquivo
            linha = linha.strip()   ## remover os espaços e \n das palavras no arquivo
            palavras.append(linha)  ## adicionar cada palavra na lista de palavras

        index = random.randrange(0,len(palavras))   ## escolher um index aleatoriamente a partir das palavras contidas na lista
        palavra_secreta = palavras[index].upper()     ## palavra secreta do jogo escolhida aleatóriamente a partir de um index da lista
        return palavra_secreta

def input_do_chute():
    chute = input("> Insira uma letra: ")   ## input do chute
    chute = chute.strip().upper()   ## remove espaços e coloca em letras maiúsculas
    print()
    return chute

def verifica_chute_correto(tentativas, palavra_secreta, chute, letras_acertadas):
    posicao = 0                 ## index de cada letra, definido como 0
    for letra in palavra_secreta:   ## define variável 'letra' baseada na palavra selecionada aleatoriamente
        if (chute == letra):
            letras_acertadas[posicao] = letra   ## caso o acertado, muda o "_" para a letra na posição definida
        posicao += 1
    desenha_forca(tentativas)
     
def verifica_chute_incorreto(tentativas, lista_chutes, chute):
    lista_chutes.append(chute)  ## lista contendo os chutes incorretos
    print("> Tentativas restantes {}".format(tentativas))
    print()
    desenha_forca(tentativas)

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 7):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def perdeu(palavra_secreta):
    print("> Você perdeu!")
    print()
    print("> A palavra era {}".format(palavra_secreta))

if(__name__ == "__main__"): ## se "forca.py" for o arquivo em foco, executá-lo
    jogar()