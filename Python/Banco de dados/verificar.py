alternativas = [1, 2]

print("> Você já possui login?")
print("    1- Sim   2- Não")
print()

escolha = int(input("> "))

while escolha not in alternativas:
    escolha = int(input("> Erro, escolha novamente: "))

## WIP

