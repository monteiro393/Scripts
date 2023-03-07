print("-"*34)
print("--- Calculadora de dois termos ---")
print("-"*34)
print()

## VARIÁVEIS AVULSAS
raiz = None
indice_int = None
indice_flt = None
resultado = None
radicando = None

## OPERAÇÕES DE 1 A 6
soma = "1- Soma "
subtracao = "2- Subtração "
multiplicacao = "3- Multiplicação "
divisao = "4- Divisão "
potenciacao = "5- Potenciação "
radiciacao = "6- Radiciação "

## ÍNDICES DA RADICIAÇÃO
quadrada = "1- Raiz Quadrada "
cubica = "2- Raiz Cúbica "
outro = "3- Outro índice "

## INPUT DO PRIMEIRO NÚMERO A SER UTILIZADO
primeiro_numero = float(input("> Insira o primeiro número da operação: "))

## SELECIONAR A OPERAÇÃO
print()
print("> Selecione a operação:")
print(soma , subtracao , multiplicacao , divisao , potenciacao , radiciacao) ## OPERAÇÕES DE 1 A 6
print()
operacao = int(input("> "))
print()

while(operacao < 1) or (operacao > 6):      ## CASO NÃO ESCOLHA NENHUM
    print("> Erro, selecione novamente:")
    print(soma , subtracao , multiplicacao , divisao , potenciacao , radiciacao)
    print()
    operacao = int(input("> "))

if(operacao >= 1) and (operacao <= 5):  ## INPUT DO SEGUNDO NÚMERO A SER UTILIZADO (caso não escolha a opção 6)
    segundo_numero = float(input("> Insira o segundo número da operação: "))

while(operacao == 0) or (operacao != 0):    ## OPERAÇÕES
    if  (operacao == 1):    ## 1 - ADIÇÃO
        resultado = primeiro_numero + segundo_numero
        print("{} + {} = {}".format(primeiro_numero , segundo_numero , resultado))
        break

    elif(operacao == 2):    ## 2 - SUBTRAÇÃO
        resultado = primeiro_numero - segundo_numero
        print("{} - {} = {}".format(primeiro_numero , segundo_numero , resultado))
        break

    elif(operacao == 3):    ## 3 - MULTIPLICAÇÃO
        resultado = primeiro_numero * segundo_numero
        print("{} * {} = {}".format(primeiro_numero , segundo_numero , resultado))
        break

    elif(operacao == 4):    ## 4 - DIVISÃO
        if(segundo_numero == 0): ## DIVISÃO POR 0
            print("{} / {} = Indefinido".format(primeiro_numero , segundo_numero))
            break
        else:
            resultado = primeiro_numero / segundo_numero
            print("{} / {} = {}".format(primeiro_numero , segundo_numero , resultado))
            break
    
    elif(operacao == 5):    ## 5 - POTENCIAÇÃO
        resultado = primeiro_numero ** segundo_numero
        print("{} ^ {} = {}".format(primeiro_numero , segundo_numero , resultado))
        break
    
    elif(operacao == 6):    ## 6 - RADICIAÇÃO
        radicando = primeiro_numero
        print("## SEU NÚMERO: {} ##".format(radicando))
        print()        
        print("> Qual é o tipo de raiz? ")
        print(quadrada , cubica , outro)
        print()
        raiz = int(input("> "))
        print()
        while(raiz == 0) or (raiz != 0):
            if(raiz == 1):      ## RAÍZ QUADRADA
                resultado = radicando ** 1/2
                print("√{} = {}".format(radicando , resultado))
                break
            elif(raiz == 2):    ## RAÍZ CÚBICA
                resultado = radicando ** 1/3
                print("∛{} = {}".format(radicando , resultado))
                break
            elif(raiz == 3):    ## OUTRO ÍNDICE
                print("> Qual é o índice?")
                indice_int = int(input("> "))
                if(indice_int == 0):    ## RAÍZ DE ÍNDICE 0
                    print()
                    print("{}√{} = Indefinido".format(indice_int , radicando))
                    break
                else:
                    indice_flt = float(1/indice_int)
                    print()
                    resultado = radicando ** indice_flt
                    print("{}√{} = {}".format(indice_int , radicando , resultado))
                    break
            else:   ## NÃO SELECIONOU
                print("> Erro, selecione novamente:")
                print(quadrada , cubica , outro)
                print()
                raiz = int(input("> "))
                print()
        break

print()