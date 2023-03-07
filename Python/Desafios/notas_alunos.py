
def media_da_turma():
    quantidade_notas = []

    nome_turma = str(input("> Insira o nome da turma: "))
    print()

    quantidade_alunos = int(input("> Insira a quantidade de alunos na turma: "))
    print()

    i = 1

    while(i <= quantidade_alunos):
        nota = int(input("> Insira a nota do aluno {}: ".format(i)))

        quantidade_notas.append(nota)
        print()

        i += 1

    soma = sum(quantidade_notas)

    media = int(soma) / quantidade_alunos

    print("> A media da {} é {}".format(nome_turma, media))

def reinicio():
    print()
    print("> Deseja realizar novamente?")
    a = 0

    while(a == 0):
        print()
        print("1- Sim  2- Não")
        reiniciar = int(input("> "))

        if(reiniciar == 1):
            print()
            media_da_turma()
        elif(reiniciar == 2):
            print()
            print("> Tudo bem, adeus!")
            exit()
        else:
            print()
            print("> Erro, insira novamente")

media_da_turma()

reinicio()
