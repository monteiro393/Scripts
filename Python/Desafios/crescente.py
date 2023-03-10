print("-" * 26)
print("--- Números Crescentes ---")   ## Título
print("-" * 26)
print()

lista = []

n1 = lista.append(int(input("> Insira o primeiro número: ")))
n2 = lista.append(int(input("> Insira o segundo número: ")))
n3 = lista.append(int(input("> Insira o terceiro número: ")))

crescente = sorted(lista)

print()
print(crescente)