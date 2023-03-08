import random

lista_multiplos = []    ## Inicia uma lista com os múltiplos

print("-" * 32)
print("--- Calculadora de Multiplos ---")   ## Título
print("-" * 32)

print()
limite = int(input("> Defina o limite para busca: "))   ## Define o limite para a busca

print()
print("> Escolha os multiplos:")
print("> (1)- 2 e 3   (2)- 2 e 5    (3)- 3 e 5   (4)- 2, 3 e 5")

escolha = int(input("> "))  ## Escolhe uma das opções
print()

opcoes = [1, 2, 3, 4]  ## Lista com as opções

while escolha not in opcoes:    ## Caso a escolha não esteja nas opções, selecionar novamente
    escolha = int(input("> Erro, selecione novamente: "))
    print()

for i in range(1, limite):  ## Define um index, com range de 1 até o limite definido
    if(escolha == 1):       ## Se escolheu (1), multiplos de 2 e 3
        if(i % 2 == 0) or (i % 3 == 0): ## Se o resto da divisão for 0, incluir na lista
            lista_multiplos.append(i)

    elif(escolha == 2):     ## Se escolheu (2), multiplos de 2 e 5
        if(i % 2 == 0) or (i % 5 == 0): ## Se o resto da divisão for 0, incluir na lista
            lista_multiplos.append(i)

    elif(escolha == 3):     ## Se escolheu (3), multiplos de 3 e 5
        if(i % 3 == 0) or (i % 5 == 0): ## Se o resto da divisão for 0, incluir na lista
            lista_multiplos.append(i)
            
    elif(escolha == 4):     ## Se escolheu (4), multiplos de 2, 3 e 5
        if(i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0): ## Se o resto da divisão for 0, incluir na lista
            lista_multiplos.append(i)
        
print(lista_multiplos)      ## Exibe a lista com os múltiplos
print()

soma = sum(lista_multiplos) ## Soma os múltiplos
print("> A soma dos multiplos até {} é {}".format(limite, soma))  ## Exibe a soma
