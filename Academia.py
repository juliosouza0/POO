import os

nomes_planos = ["Plano Básico", "Plano Intermediário", "Plano Premium"] # Vai iniciar com tres planos iniciais
valores_planos = [100.00, 150.00, 200.00]

lista_nome = ["Administrador Geral"]
lista_login = ["admin"]
lista_senha = ["admin"]

lista_nome_professor = []
lista_login_professor = []
lista_senha_professor = []
lista_contato_professor = []

lista_nome_recepcionista = []
lista_login_recepcionista = []
lista_senha_recepcionista = []
lista_contato_recepcionista = []

nomes_alunos = []
telefones_alunos = []

nome_exercicio = []
quantidade_repeticao = []



# Matricula de Alunos
def matricular_alunos():
    while True:
        nome_aluno = input("Digite o nome do aluno(a) a ser cadastrado: ")
        
        if nome_aluno in nomes_alunos:
            print("Já tem um aluno cadastrado com esse nome. Tente outro.")
            continue
            
        telefone_aluno = input("Digite o telefone do aluno(a) a ser cadastrado: ")
        
        nomes_alunos.append(nome_aluno)
        telefones_alunos.append(telefone_aluno)
        
        print(f"Aluno(a) {nome_aluno} cadastrado com sucesso!")
        
        continuar = input("Deseja continuar a matricula de alunos? (1 - Sim / 2 - Nao): ")
        if continuar == "2":
            break
        elif continuar == "1":
            print("Continuando...")
        else:
            print("Opcao Invalida")
            continue
        
# Cadastro de Funcionarios
def cadastrar_funcionario():
    while True:
        print("1 - Cadastrar Professor")
        print("2 - Cadastrar Recepcionista")
        
        escolha = int(input("Digite o que voce deseja cadastrar: "))
        
        if escolha == 1:
            print("\n ----- Cadastro de Professor -----")
            nome_professor = input("Digite o nome do professor(a): ")
            login_professor = input("Digite o login do professor(a): ")
            
            if login_professor in lista_login_professor:
                print("Este login já esta cadastrado. Tente outro.")
                continue
            
            senha_professor = input("Digite a senha do professor(a): ")
            contato_professor = input("Digite o contato do professor(a) (E - Mail ou Numero de Telefone): ")
            
            lista_nome_professor.append(nome_professor)
            lista_login_professor.append(login_professor)
            lista_senha_professor.append(senha_professor)
            lista_contato_professor.append(contato_professor)
            
            print(f"Professor(a) {nome_professor} cadastrado com sucesso! ")
            
            continuar = input("Deseja continuar o cadastro de professores? (1 - Sim / 2 - Nao): ")
            if continuar == "2":
                break
            elif continuar == "1":
                print("Continuando...")
            else:
                print("Opcao Invalida")
                continue
            
        elif escolha == 2:
            print("\n ----- Cadastro de Recepcionista -----")
            nome_recepcionista = input("Digite o nome do recepcionista: ")
            login_recepcionista = input("Digite o nome do login: ")
            
            if login_recepcionista in lista_login_recepcionista:
                print("Este login ja esta cadastrado. Tente outro.")
                continue
                
            senha_recepcionista = input("Digite a senha do recepcionista: ")
            contato_recepcionista = input("Digite o contato do recepcionista: (E - Mail ou Numero de Telefone): ")
            
            lista_nome_recepcionista.append(nome_recepcionista)
            lista_login_recepcionista.append(login_recepcionista)
            lista_senha_recepcionista.append(senha_recepcionista)
            lista_contato_recepcionista.append(contato_recepcionista)
            
            continuar = input("Deseja continuar o cadastro de recepcionistas? (1 - Sim / 2 - Nao): ")
            if continuar == "2":
                break
            elif continuar == "1":
                print("Continuando...")
            else:
                print("Opcao Invalida")
                continue
        
# Cadastro de Planos
def cadastrar_planos():
    while True:
        nome_plano = input("Digite o nome do plano: ")

        if nome_plano in nomes_planos:
            print("Erro: Este plano já está cadastrado. Tente outro.")
            continue

        valor_plano = float(input("Digite o valor do plano: R$"))

        nomes_planos.append(nome_plano)
        valores_planos.append(valor_plano)
        
        print("Plano cadastrado com sucesso!")
        
        continuar = input("Deseja cadastrar outro plano? (1 - Sim / 2 - Não): ")
        if continuar == "2":
            break
        elif continuar == "1":
            print("Continuando...")
        else:
            print("Opcao Invalida")

# Cadastro de Administrador
def cadastrar_administrador():
    while True:
        nome = input("Digite o nome: ")
        login = input("Digite o login: ")

        if login in lista_login:
            print("Este login já está cadastrado. Tente outro.")
            continue  # Faz voltar ao inicio do loop

        senha = input("Digite a senha: ")
        
        lista_nome.append(nome)
        lista_login.append(login)
        lista_senha.append(senha)
        
        print(f"Administrador {nome} cadastrado com sucesso!")
        
        continuar = input("Deseja cadastrar outro administrador? (1 - Sim / 2 - Não): ")
        if continuar == "2":
            break
        elif continuar == "1":
            print("Continuando...")
        else:
            print("Opcao Invalida")
            
# Login do Professor          
def login_professor():
    os.system('cls')
    print("Você precisa fazer login para acessar a aba de professores!")

    acesso_permitido = False

    for tentativa in range(3):
        print(f"Tentativas restantes: {3 - tentativa}")
        user = input("Digite o login: ")
        senha = input("Digite a senha: ")

        for indice, login in enumerate(lista_login_professor):
            if user == login:
                if senha == lista_senha_professor[indice]:
                    print("Acesso permitido!")
                    acesso_permitido = True
                else:
                    print("Senha incorreta.")
                break
        else:
            print("Usuário não encontrado.")

        if acesso_permitido:
            break

    if acesso_permitido:
        menu_professor()
    else:
        print("Acesso bloqueado.")

# Login do recepcionista
def login_recepcionista():
    os.system('cls')
    print("Você precisa fazer login para acessar a aba de recepcionistas!")

    acesso_permitido = False

    for tentativa in range(3):
        print(f"Tentativas restantes: {3 - tentativa}")
        user = input("Digite o login: ")
        senha = input("Digite a senha: ")

        for indice, login in enumerate(lista_login_recepcionista):
            if user == login:
                if senha == lista_senha_recepcionista[indice]:
                    print("Acesso permitido!")
                    acesso_permitido = True
                else:
                    print("Senha incorreta.")
                break
        else:
            print("Usuário não encontrado.")

        if acesso_permitido:
            break

    if acesso_permitido:
        menu_recepcionista()
    else:
        print("Acesso bloqueado.")

        
# Login do administrador
def login_admin():
    os.system('cls')
    print("Você precisa fazer login para acessar a aba de administradores!")

    acesso_permitido = False

    for tentativa in range(3):
        print(f"Tentativas restantes: {3 - tentativa}")
        user = input("Digite o login: ")
        senha = input("Digite a senha: ")

        for indice, login in enumerate(lista_login):
            if user == login:
                if senha == lista_senha[indice]:
                    print("Acesso permitido!")
                    acesso_permitido = True
                else:
                    print("Senha incorreta.")
                break
        else:
            print("Usuário não encontrado.")

        if acesso_permitido:
            break

    if acesso_permitido:
        menu_admin()
    else:
        print("Acesso bloqueado.")
        
# Criacao de Treino
def criar_treino():
    if len(nomes_alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n ----- Lista de Alunos -----")
        for indice, nome in enumerate(nomes_alunos):
            print(f"{indice + 1}. {nome}")

        nome_aluno = input("Digite o nome do aluno(a) em que deseja criar o treino: ")

        if nome_aluno not in nomes_alunos:
            print("Aluno não encontrado.")
        else:
            while True:
                exercicio = input("Digite o nome do exercício: ")
                repeticoes = input("Digite a quantidade de repetições: ")

                nome_exercicio.append(exercicio)
                quantidade_repeticao.append(repeticoes)

                print(f"Exercício {exercicio} com {repeticoes} repetições adicionado para {nome_aluno}.")
                
                continuar = int(input("Deseja continuar criando treino? (1 - Sim / 2 - Nao): "))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Continuando...")
                else:
                    print("Opcao Invalida!")
        
# Menu do Professor
def menu_professor():
    while True:
        print("\n ----- Professor -----")
        print("1 - Criar Treino")
        print("0 - Sair")
        
        op = input("Escolha uma das opcoes: ")
        
        if op == "1":
            criar_treino()
        elif op == "0":
            break
        else:
            print("Opcao Invalida")

# Menu Recepcionista
def menu_recepcionista():
    while True:
        print("\n----- Recepcionista -----")
        print("1 - Matricular Aluno")
        print("0 - Sair")
        
        op = input("Escolha uma das opções: ")
        
        if op == "1":
            matricular_alunos()
        elif op == "0":
            break
        else:
            print("Opção inválida")

# Menu Administrador
def menu_admin():
    while True:
        print("\n----- Administrador -----")
        print("1 - Cadastrar outro administrador")
        print("2 - Cadastrar Funcionário")
        print("3 - Matricular Aluno")
        print("4 - Cadastrar Planos")
        print("5 - Listar Planos")
        print("0 - Sair")
        
        op = input("Escolha uma das opções: ")
        
        if op == "1":
            cadastrar_administrador()
        elif op == "2":
            cadastrar_funcionario()
        elif op == "3":
            matricular_alunos()
        elif op == "4":
            cadastrar_planos()
        elif op == "5":
            listar_planos()
        elif op == "0":
            break
        else:
            print("Opção inválida")

# Função para listar os planos existentes
def listar_planos():
    print("\n--- Planos Disponíveis ---")

    for indice, nome in enumerate(nomes_planos):
        valor = valores_planos[indice]
        print(f"{indice + 1}. {nome} - R$ {valor}")


# Inicialização do Sistema
while True:
    print("\n====== Academia ======")
    print("1 - Administrador")
    print("2 - Recepcionista")
    print("3 - Professor")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        login_admin()
    elif opcao == "2":
        login_recepcionista()
    elif opcao == "3":
        login_professor()
    else:
        print("Opção inválida")
