#Estruturas para armazenar dados 
Pacientes=[]
Medicos=[]
consultas=[]
#Sistema de cadastro do paciente
def SubmenuPaciente():
    while True:
        print("\n -----Gerenciamento de Pacientes-----")
        print("1- Cadastrar Paciente ")
        print("2- Listar Pacientes  ")
        print("3- Alterar paciente ")
        print("4- Excluir Paciente ")
        print("0- Voltar ao menu principal ")
        op=int(input("\nEscolha uma opção: "))
        if op==0:
            break
        elif op==1:
            print("Bem vindo ao sistema de cadastro de pacientes!")
            Cadastrar_Paciente()
        elif op==2:
            print("Lista de Pacientes")
            Listar_Pacientes()
        elif op==3:
            print("Alterar Paciente")
            Alterar_Paciente()
        elif op==4:
            print("Excluir Paciente")
            Excluir_Paciente()
        else:
            ("Opção inválida")
            
def Cadastrar_Paciente():
    while True:
        cpf=int(input("Digite o CPF do paciente: ")) 
        
        cpfExiste = False
        for paciente in Pacientes:
            if paciente[2] == cpf:
                if cpfExiste==True:
                    break
                if cpfExiste:
                  print("CPF já cadastrado.") 
        else:
            Nome=input("Digite o nome do paciente: ") 
            Endereço=input("Digite o endereço do paciente(rua,casa e bairro): ")
            Telefone=int(input("Digite o telefone do paciente: "))
            Pacientes.append([cpf,Nome,Endereço,Telefone])
            print("Paciente cadastrado com sucesso!")
            
        continuar=int(input("Deseja cadastrar outro paciente? \n1-Sim\n2-Não\n"))
        if continuar==2:
            break
        elif continuar==1:
            print("Continuando...")
        else:
            print("Opção inválida.")
            
def Listar_Pacientes():
    print("Lista de pacientes: ")
    for indice,paciente in enumerate(Pacientes):
         print("\n") 
         print(f"Nome: {paciente[1]}") 
         print(f"CPF: {paciente[2]}")
         print(f"Endereço: {paciente[3]}")
         print(f"Telefone: {paciente[4]}")
         print("---------------------------------")
            
def Alterar_Paciente():
    while True:
        cpf=int(input("Digite o CPF  do paciente que deseja alterar: "))
        encontrado=False 
        for paciente in Pacientes:
            if paciente[2]==cpf:
                print(f"Paciente encontrado: {paciente[2]}")
                print(f"Nome: {paciente[1]}")
                print(f"CPF:{paciente[2]}")
                print(f"Endereço: {paciente[3]}")
                print(f"Telefone: {paciente[4]}") 
                nome=input("Digite o novo nome do paciente: ")
                cpf=int(input("Digite o novo CPF do paciente: "))
                Endereço=input("Digite o novo endereço do paciente(rua,casa e bairro): ") 
                Telefone=int(input("Digite o novo telefone do paciente: "))
                paciente[1]=nome
                paciente[2]=cpf
                paciente[3]=Endereço
                paciente[4]=Telefone
                print("Paciente alterado com sucesso!")
                encontrado=True
                break  
            if encontrado==False:
                print("Paciente não encontrado.")
            continuar=int(input("Deseja alterar outro paciente? \n1-Sim\n2-Não\n"))
            if continuar==2:
                break
            elif continuar==1:
                print("Continuando...")
            else:
                print("Opção inválida.")
                
def Excluir_Paciente():
    while True:
        cpf=int(input("Digite o CPF do paciente que deseja excluir: "))
        encontrado=False
        for paciente in Pacientes:
            if paciente[2]==cpf:
                Pacientes.remove(paciente) 
                print("Paciente excluído com sucesso!")
                encontrado=True
                break
            if encontrado==False:
                print("Paciente não encontrado.")
            continuar=int(input("Deseja excluir outro paciente? \n1-Sim\n2-Não\n"))
            if continuar==2:
                break
            elif continuar==1:
                print("Continuando...")
            else:
                print("Opçãp inválida.") 
                
#FIM do sistema de cadastro de pacientes

#Incio do sistema de cadastro de medicos

def SubmenuMedicos():
    while True:
        print("\n-----Gerenciamento de Médicos-----")
        print("1- Cadastrar Médico ") 
        print("2- Listar Médicos ")
        print("3- Alterar Médico ") 
        print("4- Excluir Médico ")
        print("0-Voltar ao menu principal ")
        op=int(input("Escolha uma opção: "))
        if op==0:
            break
        elif op==1:
            print("Bem vindo ao cadastro de médicos!")
            Cadastrar_Medico() 
        elif op==2:
            print("Lista de Médicos ")
            Listar_Medicos()
        elif op==3:
            print("Alterar Médico ") 
            Alterar_Medico()
        elif op==4:
            print("Excluir Médico ") 
            Excluir_Medico()
        else: 
            print("Opção inválida") 
            
def Cadastrar_Medico():
    while True:
        crm=input("Digite o CRM do médico: ")
        crmExiste = False
        for medico in Medicos:
            if medico[1] == crm:
                crmExiste = True
                break
        if crmExiste:
            print("CRM já cadastrado.")
        else:
            nome=input("Digite o nome do médico: ")
            especialidade=input("Digite a especialidade do médico: ")
            Medicos.append([crm,nome,especialidade])
            print("Médico cadastrado com sucesso!")
            continuar=int(input("Desejar cadastrar outro médico? \n1-Sim\n2-Não\n"))
            if continuar==2:
                break
            elif continuar==1:
                print("Continuando...")
            else:
                print("Opção inválida")
                
def Listar_Medicos():
    print("Listando Medicos")
    if len(Medicos)==0:
        print("Nenhum médico cadastrado.")
    else:
        for indice,medico in enumerate(Medicos):
            print("\n")
            print(f"Nome: {medico[1]}")
            print(f"CRM: {medico[2]}")
            print(f"Especialidade: {medico[3]}")  
            print("---------------------------------")
            
def Alterar_Medico():
    while True:
        crm=input("Digite o CRM do medico que deseja alterar: ")
        encontrado=False
        for medico in Medicos:
            if medico[2]==crm:
                print(f"Médico encontrado: Nome:{medico[1]}, CRM:{medico[2]}, Especialidade:{medico[3]}")
                nome=input("Digite o novo nome do medico: ") 
                especialidade=input("Digite a nova especialidade do medico: ")
                medico[1]=nome
                medico[2]=especialidade
                print("Médico alterado com sucesso!")
                encontrado=True
                break   
            if encontrado==False:
                print("Medico não encontrado.")
            continuar=int(input("Deseja continuar? \n1-Sim\n2-Não\n"))
            if continuar==2:
                break
            elif continuar==1:
                print("Continuando...") 
            else:
                print("Opção inválida") 
                
def Excluir_Medico():
    while True:
        crm=input("Digite o CRM do medico que deseja excluir: ")
        encontrado=False
        for medico in Medicos:
            if medico[2]==crm:
               Medicos.remove(medico)
               print("Médico excluido com sucesso")
               encontrado=True
               break
        if encontrado==False:
            print("Medico não encontrado")
            continuar=int(input("Deseja continuar? \n1-Sim\n2-Não\n"))
            if continuar==2:
                break
            elif continuar==1:
                print("Continuando...")
            else:
                print("Opção invalida")
        
#FIM do sistema de medico

#Agendar consulta
def Agendar_Consulta():
    while True:
        cpf=input("Digite o CPF do paciente")
        PacienteEncontrado=False
        for paciente in Pacientes:
            if paciente[2]==cpf:
                PacienteEncontrado=True
                print(f"Paciente encontrado: Nome: {paciente[1]} CPF: {paciente[2]}, Endereco: {paciente[3]}, Telefone: {paciente[4]}")
                
                print(f"\nLista de medicos disponiveis: ")
                for indice,conteudo in enumerate(Medicos):
                    print("Nome: {medico[1]}, CRM: {medico[2]}, Especialidade: {medico[3]}")
                MedicoEscolhido=int(input("\nEscolha o medico(Numero)"))
                if MedicoEscolhido < 0 or MedicoEscolhido >= len(Medicos):
                    print("Médico inválido.")
                else:
                    data = input("Digite a data da consulta (dd/mm/aaaa): ")
                    hora = input("Digite a hora da consulta (hh:mm): ")
                    consultas.append([paciente[1], paciente[2], Medicos[MedicoEscolhido][1], Medicos[MedicoEscolhido][1], data, hora])
                    print("Consulta agendada com sucesso!")
                break
            if PacienteEncontrado == False:
                print("Paciente não encontrado.")

        continuar = int(input("Deseja agendar outra consulta? \n1 - Sim \n 2 - Não\n "))
        if continuar == 2:
            break
        elif continuar == 1:
            print("Continuando...")
        else:
            print("Opção invalida")
            
# Fim do sistema de consultas

# Inicio do sistema de relatorio de consultas
def RelatorioConsultas():
    print("Relatório de Consultas\n")
    if len(consultas) == 0:
        print("Nenhuma consulta agendada.")
    else:
        for indice, consulta in enumerate(consultas):
            print(f"{indice}. Paciente: {consulta[1]}, CPF: {consulta[2]}")
            print(f"\tMédico: {consulta[3]}, CRM: {consulta[4]}")
            print(f"\tData: {consulta[5]}, Hora: {consulta[6]}")
            print("-" * 40)
    input("Pressione qualquer tecla para voltar ao menu...")
    
# Fim do sistema de relatorio de consultas
    
# Cerebro do sistema    

while True:
    print("\n----- Clinica -----")
    print("1 - Gerenciar Pacientes")
    print("2 - Gerenciar Medicos")
    print("3 - Agendar Consulta")
    print("4 - Relatorio de Consultas")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 0:
        print("Saindo do sistema...")
        break
    elif opcao == 1:
        SubmenuPaciente()
    elif opcao == 2:
        SubmenuMedicos()
    elif opcao == 3:
        Agendar_Consulta()
    elif opcao == 4:
        RelatorioConsultas()
    else:
        print("Opção inválida. Tente novamente.")