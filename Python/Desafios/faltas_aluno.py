print("-" * 28)
print("--- Verificar Reprovação ---")   ## Título
print("-" * 28)
print()

aluno = input("> Insira o nome do aluno: ") ## Inserir o nome do aluno
print()

aulas_totais = int(input("> Insira o total de aulas: "))    ## Inserir a quantidade total de aulas
faltas = int(input("> Insira o total de faltas: "))         ## Inserir a quantidade de faltas
print()

reprovacao_faltas = faltas / aulas_totais * 100    ## Formula para calcular a % de faltas

if(round(reprovacao_faltas, 2) > 25):   ## Se a porcentagem for maior que 25%, o aluno está reprovado
    print("> O aluno {} está reprovado por ter {}% de faltas".format(aluno, round(reprovacao_faltas, 2)))
    exit()

else:   ## Se a porcentagem for menor que 25%, está tudo certo
    print("> O percentual de faltas do aluno {} foi de {}%".format(aluno, reprovacao_faltas))
    print()

n1 = int(input("> Insira a primeira nota: "))   ## Input para a primeira nota
n2 = int(input("> Insira a segunda nota: "))    ## Input para a segunda nota
print()

media = (n1 + n2) / 2   ## Formula para calcular a média

if(media >= 7):     ## Se a média for maior que 7, o aluno foi aprovado
    print("> O aluno {} foi aprovado com média {}!".format(aluno, media))

elif(media >= 4) and (media <= 7):  ## Se a média for entre 4 e 7, o aluno está de prova final
    print("> O aluno {} está de prova final com média {}.".format(aluno, media))

else:   ## Se a média for menor que 4, o aluno foi reprovado
    print("> O aluno {} está reprovado com média {}.")