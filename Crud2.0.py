ListaClientes = []
ListaAnoNascimento = []

def SubMenu():
    print("\n--- Gerenciar Clientes ---")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Pesquisar")
    print("0 - Voltar ao menu principal")

def CadastrarCliente():
    while True:
        nome = input("Digite o nome do cliente: ")
        AnoNascimento = input("Digite o ano de nascimento do cliente: ")
        ListaClientes.append(nome)
        ListaAnoNascimento.append(AnoNascimento)
        print(f"Cliente '{nome}' cadastrado com sucesso.")
        
        continuar = int(input("Deseja cadastrar outro cliente? (1 - Sim / 2- Não): "))
        if continuar == 2:
            break
        else:
            print("Continuando...")

def AlterarDados():
    while True:
        nome = input("Digite o nome do cliente que deseja alterar: ")
        if nome in ListaClientes:
            NovoNome = input(f"Digite o novo nome para '{nome}': ")
            NovoAnoNascimento = input(f"Digite o novo ano de nascimento para '{nome}': ")
            indice = ListaClientes.index(nome)
            ListaClientes[indice] = NovoNome
            ListaAnoNascimento[indice] = NovoAnoNascimento
            print(f"Dados alterados com sucesso para '{NovoNome}'.")
        else:
            print(f"Cliente '{nome}' não encontrado.")
            
        continuar = int(input("Deseja alterar os dados de outro cliente? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        else:
            print("Continuando...")
    
def ExcluirCliente():
    while True:
        nome = input("Digite o nome do cliente que deseja excluir: ")
        if nome in ListaClientes:
            indice = ListaClientes.index(nome)
            ListaClientes.pop(indice)
            ListaAnoNascimento.pop(indice)
            print(f"Cliente '{nome}' excluído com sucesso.")
        else:
            print(f"Cliente '{nome}' não encontrado.")
            
        continuar = int(input("Deseja excluir outro cliente? (1 - Sim / 2- Não): "))
        if continuar == 2:
            break
        else:
            print("Continuando...")

def PesquisarCliente():
    while True:
        nome = input("Digite o nome que deseja pesquisar: ")
        if nome in ListaClientes:
            indice = ListaClientes.index(nome)
            print(f"Cliente '{nome}' está cadastrado. Ano de nascimento: {ListaAnoNascimento[indice]}")
        else:
            print(f"Cliente '{nome}' não foi encontrado.")
            
        continuar = int(input("Deseja pesquisar outro cliente? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        else:
            print("Continuando...")
    
while True:
    print("1 - Gerenciar Clientes")
    print("0 - Sair")
    
    op = int(input("Escolha uma opção: "))
    
    if op == 0:
        print("Programa encerrado.")
        break
    elif op == 1:
        while True:
            SubMenu()
            Opcao = int(input("Escolha uma opção: "))
            
            if Opcao == 0:
                break
            elif Opcao == 1:
                CadastrarCliente()
            elif Opcao == 2:
                AlterarDados()
            elif Opcao == 3:
                ExcluirCliente()
            elif Opcao == 4:
                PesquisarCliente()
            else:
                print("Opção inválida. Tente novamente.")