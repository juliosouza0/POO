import os

Pacientes = []
Medicos = []
Consultas = []
# Inicio do sistema de pacientes
def SubMenuPacientes():
    while True:
        print("\n----- Gerenciar Pacientes -----")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Editar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Voltar ao Menu Principal")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            break
        elif opcao == 1:
            os.system('cls')
            CadastrarPaciente()
        elif opcao == 2:
            os.system('cls')
            ListarPacientes()
        elif opcao == 3:
            os.system('cls')
            EditarPaciente()
        elif opcao == 4:
            os.system('cls')
            ExcluirPaciente()
        else:
            print("Opção inválida. Tente novamente.")
            
def CadastrarPaciente():
    while True:
        os.system('cls')
        cpf = input("Digite o CPF do paciente: ")
        
        cpfExiste = False
        for paciente in Pacientes:
            if paciente[1] == cpf:
                cpfExiste = True
                break

        if cpfExiste:
            print("CPF já está cadastrado no sistema. ")
        else:
            nome = input("Digite o nome do paciente: ")
            endereco = input("Digite o endereço do paciente (rua, casa e bairro): ")
            telefone = input("Digite o telefone do paciente: ")
            Pacientes.append([nome, cpf, endereco, telefone])
            print("Paciente cadastrado com sucesso!")

        continuar = int(input("Deseja cadastrar outro paciente? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            print("Continuando...")
        else:
            print("Opção inválida.")
            break

            
def ListarPacientes():
    os.system('cls')
    print("Listando Pacientes:")
    if len(Pacientes) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        for indice, paciente in enumerate(Pacientes):
            print(f"{indice} - Nome: {paciente[0]}, CPF: {paciente[1]}, Endereço: {paciente[2]}, Telefone: {paciente[3]}")

    
def EditarPaciente():
    os.system('cls')
    while True:
        cpf = input("Digite o CPF do paciente que deseja editar: ")
        encontrado = False
        for paciente in Pacientes:
            if paciente[1] == cpf:
                print(f"Paciente encontrado: Nome: {paciente[0]}, CPF: {paciente[1]}, Endereço: {paciente[2]}, Telefone: {paciente[3]}")
                nome = input("Digite o novo nome do paciente: ")
                endereco = input("Digite o novo endereço do paciente (rua, casa e bairro): ")
                telefone = input("Digite o novo telefone do paciente: ")
                paciente[0] = nome
                paciente[2] = endereco
                paciente[3] = telefone
                print("Paciente editado com sucesso!")
                encontrado = True
                break
        
        if encontrado == False:
            print("Paciente não encontrado.")
        
        continuar = int(input("Deseja editar outro paciente? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar != 1:
            print("Opção inválida. Tentando novamente...")



def ExcluirPaciente():
    os.system('cls')
    while True:    
        cpf = input("Digite o CPF do paciente que deseja excluir: ")
        encontrado = False
        for paciente in Pacientes:
            if paciente[1] == cpf:
                Pacientes.remove(paciente)
                print("Paciente excluído com sucesso!")
                encontrado = True
                break
        
        if encontrado == False:
            print("Paciente não encontrado.")
        
        continuar = int(input("Deseja excluir outro paciente? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            print("Voltando...")
            break
        elif continuar != 1:
            print("Opção inválida. Tentando novamente...")



# Fim do sistema de pacientes

# Inicio do sistema de medicos

def SubMenuMedicos():
    while True:
        print("\n----- Gerenciar Medicos -----")
        print("1 - Cadastrar Medico")
        print("2 - Listar Medicos")
        print("3 - Editar Medico")
        print("4 - Excluir Medico")
        print("0 - Voltar ao Menu Principal")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            break
        elif opcao == 1:
            os.system('cls')
            CadastrarMedico()
        elif opcao == 2:
            os.system('cls')
            ListarMedicos()
        elif opcao == 3:
            os.system('cls')
            EditarMedico()
        elif opcao == 4:
            os.system('cls')
            ExcluirMedico()
        else:
            print("Opção inválida. Tente novamente.")
            
def CadastrarMedico():
    while True:
        os.system('cls')
        crm = input("Digite o CRM do médico: ")

        crmExiste = False
        for medico in Medicos:
            if medico[1] == crm:
                crmExiste = True
                break

        if crmExiste:
            print("CRM já está cadastrado no sistema.")
        else:
            nome = input("Digite o nome do médico: ")
            especialidade = input("Digite a especialidade do médico: ")
            Medicos.append([nome, crm, especialidade])
            print("Médico cadastrado com sucesso!")

        continuar = int(input("Deseja cadastrar outro médico? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar == 1:
            print("Continuando...")
        else:
            print("Opção inválida.")

            
def ListarMedicos():
    os.system('cls')
    print("Listando Médicos:")
    if len(Medicos) == 0:
        print("Nenhum médico cadastrado.")
    else:
        for indice, medico in enumerate(Medicos):
            print(f"{indice} - Nome: {medico[0]}, CRM: {medico[1]}, Especialidade: {medico[2]}")


def EditarMedico():
    os.system('cls')
    while True:
        crm = input("Digite o CRM do médico que deseja editar: ")
        encontrado = False
        for medico in Medicos:
            if medico[1] == crm:
                print(f"Médico encontrado: Nome: {medico[0]}, CRM: {medico[1]}, Especialidade: {medico[2]}")
                nome = input("Digite o novo nome do médico: ")
                especialidade = input("Digite a nova especialidade do médico: ")
                medico[0] = nome
                medico[2] = especialidade
                print("Médico editado com sucesso!")
                encontrado = True
                break
        
        if encontrado == False:
            print("Médico não encontrado.")
        
        continuar = int(input("Deseja editar outro médico? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar != 1:
            print("Opção inválida. Tentando novamente...")



def ExcluirMedico():
    os.system('cls')
    while True:
        crm = input("Digite o CRM do médico que deseja excluir: ")
        encontrado = False
        for medico in Medicos:
            if medico[1] == crm:
                Medicos.remove(medico)
                print("Médico excluído com sucesso!")
                encontrado = True
                break
        
        if encontrado == False:
            print("Médico não encontrado.")
        
        continuar = int(input("Deseja excluir outro médico? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            print("Voltando...")
            break
        elif continuar != 1:
            print("Opção inválida. Tentando novamente...")

# Fim do sistema de medicos

# Agendar consulta
def AgendarConsulta():
    while True:
        os.system('cls')
        cpf = input("Digite o CPF do paciente: ")
        PacienteEncontrado = False

        for paciente in Pacientes:
            if paciente[1] == cpf:
                PacienteEncontrado = True
                print(f"Paciente encontrado: Nome: {paciente[0]}, CPF: {paciente[1]}, Endereço: {paciente[2]}, Telefone: {paciente[3]}")

                print("\nLista de médicos disponíveis: ")
                for indice, medico in enumerate(Medicos):
                    print(f"{indice} - Nome: {medico[0]}, CRM: {medico[1]}, Especialidade: {medico[2]}")

                MedicoEscolhido = int(input("\nEscolha o médico (número): "))

                if MedicoEscolhido < 0 or MedicoEscolhido >= len(Medicos):
                    print("Médico inválido.")
                else:
                    data = input("Digite a data da consulta (dd/mm/aaaa): ")
                    hora = input("Digite a hora da consulta (hh:mm): ")
                    Consultas.append([paciente[0], paciente[1], Medicos[MedicoEscolhido][0], Medicos[MedicoEscolhido][1], data, hora])
                    print("Consulta agendada com sucesso!")
                break

        if PacienteEncontrado == False:
            print("Paciente não encontrado.")

        continuar = int(input("Deseja agendar outra consulta? (1 - Sim / 2 - Não): "))
        if continuar == 2:
            break
        elif continuar != 1:
            print("Opção inválida. Tentando novamente...")

# Fim do sistema de consultas

# Inicio do sistema de relatorio de consultas
def RelatorioConsultas():
    os.system('cls')
    print("Relatório de Consultas\n")
    if len(Consultas) == 0:
        print("Nenhuma consulta agendada.")
    else:
        for indice, consulta in enumerate(Consultas):
            print(f"{indice}. Paciente: {consulta[0]}, CPF: {consulta[1]}")
            print(f"\tMédico: {consulta[2]}, CRM: {consulta[3]}")
            print(f"\tData: {consulta[4]}, Hora: {consulta[5]}")
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
        os.system('cls')
        SubMenuPacientes()
    elif opcao == 2:
        os.system('cls')
        SubMenuMedicos()
    elif opcao == 3:
        os.system('cls')
        AgendarConsulta()
    elif opcao == 4:
        os.system('cls')
        RelatorioConsultas()
    else:
        os.system('cls')
        print("Opção inválida. Tente novamente.")