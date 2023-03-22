import os

os.chdir(".\Python\Banco de dados") ## Muda o diretório para a pasta onde contém os arquivos .txt

'''
diretorio_atual = os.getcwd()   ## Teste para saber se o diretório atual está correto
print(diretorio_atual)
'''

def carrega_email():
    with open("email.txt", "r") as arquivo_email_r:
        emails = []

        for linha in arquivo_email_r:   ## definir uma variável 'linha' e fazer um loop para "ler" o arquivo
                linha = linha.strip()   ## remover os espaços e \n das palavras no arquivo
                emails.append(linha)  ## adicionar cada palavra na lista de palavras 
                ## print(emails)

def input_login():  ## Input do login
    login = input("> Insira seu usuário ou email: ")    ## Input do login
    login = login.strip().upper()   ## remove espaços e coloca em letras maiúsculas
    print()
    return login

def erro_login():  ## Input para caso erro do login
    login = input("> Erro, insira seu usuário ou email novamente: ")    ## Input do login
    login = login.strip().upper()   ## remove espaços e coloca em letras maiúsculas
    print()
    return login

## def verifica_se_email(carrega_email, input_login, erro_login):
 

alternativas = [1, 2]

print("> Você já possui login?")
print("    1- Sim   2- Não")
print()

escolha = int(input("> "))

while escolha not in alternativas:
    escolha = int(input("> Erro, escolha novamente: "))

carrega_email()

## WIP