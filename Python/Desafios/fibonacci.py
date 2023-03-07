print("-"*30)
print("--- Sequência de Fibonacci ---")
print("-"*30)
print()

n = int(input("> Quantos termos você quer mostrar? > "))
print()

n1 = 0
n2 = 1

cont = 3

print("{} \n{} ".format(n1, n2), end="")
print()

while(cont <= n):
    n3 = n1 + n2
    print("{} ".format(n3), end="")
    print()
    n1 = n2
    n2 = n3
    cont += 1

print()