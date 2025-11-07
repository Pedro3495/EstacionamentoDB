from services.user_services import insert_client,insert_ticketmensal
from datetime import datetime, timedelta

users = {
    "admin": "admin"
}

def adminLogin():
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if user in users and users[user] == password:
        print("Login realizado com sucesso!\n")
        admin_menu(user)
    else:
        print("Usuário e/ou senha incorreta.\n")

def admin_menu(user): 
    while True:
        print("--- MENU ADMINISTRATIVO ---")
        print("1 - Ver todos os tickets temporários ativos")
        print("2 - Ver todos os tickets mensais ativos")
        print("3 - Inserir novo ticket mensal")
        print("4 - Adicionar Cliente")
        print("0 - Sair")
        option = input("Escolha: ")

        if option == "1":
            print("Mostrando tickets temporários...\n")
            #criar conexão para mostrar tickets temp

        elif option == "2":
            print("Mostrando tickets mensais...\n")
            #criar conexão para mostrar tickets mensais

        elif option == "3":
            create_date = datetime.now()
            due_date = create_date + timedelta(days=30)

            parking_space = input("Digite qual será a vaga do cliente:")
            print(f"Vencimento: {due_date.strftime('%d/%m/%Y')}\n")
            insert_ticketmensal(parking_space)

            print(f"Novo ticket mensal criado para {name} (CPF: {cpf}) -> O ID DO TICKET É: | A Vaga fixa do cliente é: {parking_space}\n")
        
        elif option == "4":
            name = input("Digite o nome do cliente: ")
            cpf = input("Digite o número do CPF do cliente: ")
            id_cliente = insert_client(name, cpf)
            print(f"Novo cliente Registrado! Nome: {name}, CPF: {cpf}, ID: {id_cliente}")


        elif option == "0":
            print("Saindo do menu administrativo...\n")
            break

        else:
            print("Opção inválida, tente novamente.\n")