from services.user_services import insert_client,insert_ticketmensal,ver_ticket_mensal,limpar_terminal,buscar_nome_cpf_do_cliente,vaga_disponivel
from datetime import datetime, timedelta



def admin_menu(): 
    while True:
        limpar_terminal()
        print("--- MENU ADMINISTRATIVO ---")
        print("1 - Ver todos os tickets temporários ativos")
        print("2 - Ver todos os tickets mensais ativos")
        print("3 - Inserir novo ticket mensal")
        print("4 - Adicionar Cliente")
        print("0 - Sair")
        option = input("Escolha: ")

        if option == "1":
            print("Mostrando tickets temporários...\n")
          
        elif option == "2":
            limpar_terminal()
            print("Mostrando tickets mensais...\n")
            #criar conexão para mostrar tickets mensais
            tickets = ver_ticket_mensal()
            if tickets:
                for ticket in tickets:
                    id_ticket, id_client, parking_space, due_date = ticket
                    data_formatada = due_date.strftime('%d/%m/%Y')
                    print(f"({id_ticket}, {id_client}, '{parking_space}', {data_formatada})")
                input("\nDigite ENTER para continuar...")  
            else:
                print("Nenhum ticket encontrado.")
                input("\nDigite ENTER para continuar...")
        elif option == "3":
            limpar_terminal()
            create_date = datetime.now()
            due_date = create_date + timedelta(days=30)
            due_date_str = due_date.strftime('%Y-%m-%d') 

            id_mensalista = int(input("Digite o ID do Cliente: "))
            parking_space = str(input("Digite qual será a vaga do cliente: ")).strip()
            print(f"Vencimento: {due_date_str}\n")

            if vaga_disponivel(parking_space):
                
                name, cpf = buscar_nome_cpf_do_cliente(id_mensalista)
                id_ticket = insert_ticketmensal(parking_space, id_mensalista, due_date_str)

                print(f"O ID DO TICKET É: {id_ticket}")
                if name and cpf:
                    print(f"Novo ticket mensal criado para {name} (CPF: {cpf}) -> A Vaga fixa do cliente é: {parking_space}\n")
                    input("\nDigite ENTER para continuar...")
                else:
                    print("Cliente não encontrado.")
                    input("\nDigite ENTER para continuar...")
            else:
                print("Vaga já ocupada. Escolha outra vaga!")

        elif option == "4":
            limpar_terminal()
            name = input("Digite o nome do cliente: ")
            cpf = input("Digite o número do CPF do cliente: ")
            id_cliente = insert_client(name, cpf)
            print(f"Novo cliente Registrado! Nome: {name}, CPF: {cpf}, ID: {id_cliente}")
            input("\nDigite ENTER para continuar...") 


        elif option == "0":
            print("Saindo do menu administrativo...\n")
            break

        else:
            print("Opção inválida, tente novamente.\n")