### EXERCÍCIO 1

"""

a = int(input("> Insira o primeiro número: "))
b = int(input("> Insira o segundo número: "))
c = int(input("> Insira o terceiro número: "))

media = (a + b + c)/3

print()
print("> A média dos números inseridos é {}".format(media))

"""

### EXERCÍCIO 2

"""

alt = 0

distancia_km = float(input("> Insira a distância percorrida em quilômetros: "))
print()

tempo_min = float(input("> Insira o tempo utilizado em minutos: "))
print()

while(alt == 0):
    print("> Selecione a unidade de medida:")
    print("> 1- m/s     2- Km/h")

    escolha = float(input("> "))

    if(escolha == 1):
        tempo_s = tempo_min * 60
        distancia_m = distancia_km * 1000
        velmed = distancia_m / tempo_s
        unidade = "m/s"
        alt = 1

    elif(escolha == 2):
        tempo_h = tempo_min / 60
        velmed = distancia_km / tempo_h
        unidade = "Km/h"
        alt = 1

    else:
        print()
        print("> Seleção inválida")
        print("> Selecione novamente: ")
        print("> 1- m/s     2- Km/h")
        escolha = float(input("> "))

    print()

print("> A sua velocidade média, em {} é de {}".format(unidade, velmed))

consumo = distancia_km / 12

print()
print("> Em {} quilômetros você consumiu {}".format(distancia_km, consumo))
print()

"""

### EXERCÍCIO 3

"""

armacao = float(input("> Insira a quantidade de armação, em Kg: "))         ## 1440 Kg de armação
produtividade = float(input("> Insira a produtividade em Kg por hora: "))   ## 10 Kg por hora
humanos = float(input("> Insira o número de trabalhadores na obra: "))      ## 3 trabalhadores na obra
jornada = float(input("> Insira a jornada diária: "))                       ## 8 horas por dia

armacao_diaria = produtividade * humanos * jornada
tempo_necessario = armacao / armacao_diaria

print()
print("> A duração da obra, em dias, é de {}".format(tempo_necessario))

"""