from services.user_services import insert_client,insert_ticketmensal,ver_ticket_mensal,limpar_terminal
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
                    print(ticket)
                input("\nDigite ENTER para continuar...")  # Pausa até o usuário pressionar ENTER
            else:
                print("Nenhum ticket encontrado.")
                input("\nDigite ENTER para continuar...")
        elif option == "3":
            limpar_terminal()
            create_date = datetime.now()
            due_date = create_date + timedelta(days=30)

            parking_space = input("Digite qual será a vaga do cliente:")
            print(f"Vencimento: {due_date.strftime('%d/%m/%Y')}\n")
            insert_ticketmensal(parking_space)

            print(f"Novo ticket mensal criado para {name} (CPF: {cpf}) -> O ID DO TICKET É: | A Vaga fixa do cliente é: {parking_space}\n")
            input("\nDigite ENTER para continuar...") 
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