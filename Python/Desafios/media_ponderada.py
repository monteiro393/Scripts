import random

print("> Qual o limitante?")
maximo_alt = int(input("> "))   ## Define o limite para o aleatório

maximo = 100

aleatorio = random.randint(2, maximo_alt)  ## Cria um número inteiro aleatorio

valores_n = []      ## Inicia uma lista de valores para n
valores_p = []      ## Inicia uma lista de valores para p

lista_numeradores = []   ## Inicia uma lista de numeradores
lista_denominadores = [] ## Inicia uma lista de denominadores

for i in range(1, aleatorio):
    n = random.randint(1, maximo)  ## Gera valores aleatorios para n
    p = random.randint(1, maximo)  ## Gera valores aleatorios para p

    numerador = n * p     ## Realiza e armazena a multiplicação no numerador
    denominador = p       ## Armazena o 'p' no denominadore

    valores_n.append(n)   ## Inclui os valores na lista N
    valores_p.append(p)   ## Inclui os valores na lista P
    lista_numeradores.append(numerador)     ## Inclui os numeradores na lista
    lista_denominadores.append(denominador) ## Inclui os denominadores na lista

'''

    print("> Index: {}".format(i))  ## Imprime o valor do Index
    print("> n = {}".format(n))     ## Imprime o valor de 'n' para aquele Index
    print("> p = {}".format(p))     ## Imprime o valor de 'p' para aquele index
    print()

'''

soma_numeradores = sum(lista_numeradores)       ## Realiza a soma de todos os numeradores
soma_denominadores = sum(lista_denominadores)   ## Realiza a soma de todos os denominadores

media_ponderada = soma_numeradores / soma_denominadores ## Divide num. por den., assim fazendo uma mp

print()
print("> Valores de n: {}".format(valores_n))   ## Imprime a lista com os valores de n
print()
print("> Valores de p: {}".format(valores_p))   ## Imprime a lista com os valores de p
print()

'''

print("> Numeradores: {}".format(lista_numeradores))        ## Imprime a lista com os numeradores
print("> Denominadores: {}".format(lista_denominadores))    ## Imprime a lista com os denominadores
print()
print("> Soma numeradores: {}".format(soma_numeradores))    ## Imprime a lista com a soma dos numer.
print("> Soma denominadores: {}".format(soma_denominadores))  ## Imprime a lista com a soma dos denom.
print()

'''

## Imprime a mp, com apenas duas casas decimais

print("> A média ponderada é de aproximadamente: {}".format(round(media_ponderada, 2)))
print()

