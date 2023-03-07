
print()
limite = int(input("> Digite o limite: "))

primo = 2

while(primo <= limite):
    if (primo == 2) or (primo == 3) or (primo == 5) or (primo == 7):
        print(primo)
        primo += 1
    elif (primo % 2 == 0) or (primo % 3 == 0) or (primo % 5 == 0) or (primo % 7 == 0):
        ## print("Não é: {}".format(primo))
        primo += 1
    else:
        print(primo)
        primo += 1
