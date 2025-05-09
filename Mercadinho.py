import os

ListaProdutos = []
ListaCodigos = []
ListaValidade = []
ListaQuantidade = []
ListaValorUnitario = []


def SubMenu():
    print("1 - Cadastrar Produto")
    print("2 - Pesquisar Produto")
    print("3 - Alterar Produto")
    print("4 - Excluir Produto")
    print("5 - Realizar Venda")
    print("0 - Voltar ao menu principal")
    
def CadastrarProduto():
    while True:
        produto = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        validade = input("Digite a validade do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        valorUnitario = float(input("Digite o valor unitário do produto: "))
        ListaProdutos.append(produto)
        ListaCodigos.append(codigo)
        ListaValidade.append(validade)
        ListaQuantidade.append(quantidade)
        ListaValorUnitario.append(valorUnitario)
        print(f"Produto '{produto}' cadastrado com sucesso.")
        
        continuar = int(input("Deseja cadastrar outro produto? (1 - Sim / 2- Não): "))
        
        if continuar == 2:
            break
        elif continuar == 1:
            os.system('cls')
            print("Continuando...")
        else:
            print("Opção inválida. Tente novamente.")
    
def PesquisarProduto():
    while True:
        produto = input("Digite o nome do produto que deseja pesquisar: ")
        if produto in ListaProdutos:
            indice = ListaProdutos.index(produto)
            print(f"Produto: {ListaProdutos[indice]}")
            print(f"Código: {ListaCodigos[indice]}")
            print(f"Validade: {ListaValidade[indice]}")
            print(f"Quantidade: {ListaQuantidade[indice]}")
            print(f"Valor Unitário: {ListaValorUnitario[indice]} R$")
        else:
            print(f"Produto '{produto}' não encontrado.")
            
        continuar = int(input("Deseja pesquisar outro produto? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            os.system('cls')
            print("Continuando...")
        else:
            print("Opção inválida. Tente novamente.") 
        
def AlterarProduto():
    while True:
        produto = input("Digite o nome do produto que deseja alterar: ")
        if produto in ListaProdutos:
            NovoProduto = input(f"Digite o novo nome para '{produto}': ")
            NovoCodigo = input(f"Digite o novo código para '{produto}': ")
            NovoValidade = input(f"Digite a nova validade para '{produto}': ")
            NovaQuantidade = int(input(f"Digite a nova quantidade para '{produto}': "))
            NovoValorUnitario = float(input(f"Digite o novo valor unitário para '{produto}': "))
            indice = ListaProdutos.index(produto)
            ListaProdutos[indice] = NovoProduto
            ListaCodigos[indice] = NovoCodigo
            ListaValidade[indice] = NovoValidade
            ListaQuantidade[indice] = NovaQuantidade
            ListaValorUnitario[indice] = NovoValorUnitario
            print(f"Produto '{NovoProduto}' alterado com sucesso.")
        else:
            print(f"Produto '{produto}' não encontrado.")
            
        continuar = int(input("Deseja alterar outro produto? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            os.system('cls')
            print("Continuando...")
        else:
            print("Opção inválida. Tente novamente.")
            
def ExcluirProduto():
    while True:
        produto = input("Digite o nome do produto que deseja excluir: ")
        if produto in ListaProdutos:
            indice = ListaProdutos.index(produto)
            ListaProdutos.pop(indice)
            ListaCodigos.pop(indice)
            ListaValidade.pop(indice)
            ListaQuantidade.pop(indice)
            ListaValorUnitario.pop(indice)
            print(f"Produto '{produto}' excluído com sucesso.")
        else:
            print(f"Produto '{produto}' não encontrado.")
            
        continuar = int(input("Deseja excluir outro produto? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            print("Continuando...")
        else:
            print("Opção inválida. Tente novamente.")
            
def RealizarVenda():
    while True:
        produto = input("Digite o nome do produto que deseja vender: ")
        if produto in ListaProdutos:
            indice = ListaProdutos.index(produto)
            quantidade = int(input("Digite a quantidade que deseja vender: "))
            if quantidade <= ListaQuantidade[indice]:
                ListaQuantidade[indice] =  ListaQuantidade[indice] - quantidade
                valorTotal = quantidade * ListaValorUnitario[indice]
                print(f"Valor total da compra: R$ {valorTotal:.2f}")
                valorPago = float(input("Digite o valor pago pelo cliente: "))
                if valorPago >= valorTotal:
                    troco = valorPago - valorTotal
                    print(f"Troco: R$ {troco:.2f}")
                    print("Venda realizada com sucesso!")
                else:
                    print("Valor insuficiente. Venda não realizada.")
                    ListaQuantidade[indice] += quantidade  # Reverte a quantidade
            else:
                print(f"Quantidade disponível: {ListaQuantidade[indice]}. Venda não realizada.")
        else:
            print(f"Produto '{produto}' não encontrado.")
        
        continuar = int(input("Deseja realizar outra venda? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            print("Continuando...")
        else:
            print("Opção inválida. Tente novamente.")

            
while True:
    print("1 - Entrar no sistema de mercadinho")
    print("2 - Sair do mercadinho")
    
    opcao = int(input("Escolha uma opção: "))
    if opcao == 2:
        print("Saindo do mercadinho...")
        break
    elif opcao == 1:
        while True:
            os.system('cls')
            print("Bem vindo ao sistema de mercadinho!")
            SubMenu()
            opcao = int(input("Escolha uma opção: "))
            if opcao == 0:
                os.system('cls')
                print("Voltando ao menu principal...")
                break
            elif opcao == 1:
                os.system('cls')
                CadastrarProduto()
            elif opcao == 2:
                os.system('cls')
                PesquisarProduto()
            elif opcao == 3:
                os.system('cls')
                AlterarProduto()
            elif opcao == 4:
                os.system('cls')
                ExcluirProduto()
            elif opcao == 5:
                os.system('cls')
                RealizarVenda()
            else:
                print("Opção inválida. Tente novamente.")
                