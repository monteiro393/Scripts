import os

os.chdir(".\Python\Banco de dados") ## Muda o diretório para a pasta onde contém os arquivos .txt

'''
diretorio_atual = os.getcwd()   ## Teste para saber se o diretório atual está correto
print(diretorio_atual)
'''

def escolha_inicio():   ## Escolha inicial de sign in ou sign up
    alternativas = [1, 2]

    print("> Você já possui login?")
    print("    1- Sim   2- Não")
    print()

    escolha = int(input("> "))

    while escolha not in alternativas:  ## Enquanto não for 1 ou 2, repetir o input
        escolha = int(input("> Erro, escolha novamente: "))
    
    return escolha

def carrega_email():    ## Carrega arquivo email.txt
    with open("email.txt", "r") as arquivo_email_r:
        emails = []

        for linha_e in arquivo_email_r:   ## definir uma variável 'linha_e' e fazer um loop para "ler" o arquivo
                linha_e = linha_e.strip()   ## remover os espaços e \n das palavras no arquivo
                emails.append(linha_e)  ## adicionar cada palavra na lista de palavras 
                ## print(emails)
        return emails

def carrega_usuario():  ## Carrega arquivo usuario.txt
    with open("usuario.txt", "r") as arquivo_usuario_r:
        usuarios = []

        for linha_u in arquivo_usuario_r:   ## definir uma variável 'linha_u' e fazer um loop para "ler" o arquivo
                linha_u = linha_u.strip()   ## remover os espaços e \n das palavras no arquivo
                usuarios.append(linha_u)  ## adicionar cada palavra na lista de palavras 
                ## print(usuarios)
        return usuarios

def carrega_senha():    ## Carrega arquivo senha.txt
    with open("senha.txt", "r") as arquivo_senha_r:
        senhas = []

        for linha_s in arquivo_senha_r:   ## definir uma variável 'linha_s' e fazer um loop para "ler" o arquivo
                linha_s = linha_s.strip()   ## remover os espaços e \n das palavras no arquivo
                senhas.append(linha_s)  ## adicionar cada palavra na lista de palavras 
                ## print(senhas)
        return senhas

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

def verifica_login(emails, usuarios, login):
    for log in emails:
        print(log)
    print(usuarios)

escolha = escolha_inicio()

if(escolha == 1):
    login = input_login()
    

emails = carrega_email()
usuarios = carrega_usuario()

verifica_login(emails, usuarios, login)

## WIP
