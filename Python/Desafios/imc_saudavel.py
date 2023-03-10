peso = int(input("> Insira o peso em quilos da pessoa: "))        ## Input do peso da pessoa em Kg
altura = float(input("> Insira a altura em metros da pessoa: "))  ## Input da altura da pessoa em m 
print()

altura_quadrado = altura ** 2   ## Quadrado da altura

imc = peso / altura_quadrado    ## Fórmula para calcular o IMC
imc_round = round(imc, 1)       ## Arredondar o IMC

if(imc >= 18) and (imc <= 25):  ## Se for entre 18 e 25 é saudável
    print("> O paciente possui um IMC saudável de número {}".format(imc_round))

elif(imc < 18): ## Se for abaixo de 18
    print("> O paciente possui um IMC de número {} abaixo do recomendado".format(imc_round))

elif(imc > 25): ## Se for acima de 25
    print("> O paciente possui IMC de número {} maior que o recomendado".format(imc_round))