print("-" * 28)
print("--- Encontrar triângulos ---")
print("-" * 28)
print()

l1 = int(input("> Insira a primeira medida: "))
l2 = int(input("> Insira a segunda medida: "))
l3 = int(input("> Insira a terceira medida: "))
print()

if(l1 + l2 < l3) or (l1 + l3 < l2):
    print("> As medidas inseridas não formam um triângulo.")

elif(l1 == 0) or (l2 == 0) or (l3 == 0):
    print("> As medidas inseridas não formam um triângulo.")

else:
    print("> As medidas inseridas formam um triângulo")
    print("  de lados {}, {} e {}.".format(l1, l2, l3))
    print()