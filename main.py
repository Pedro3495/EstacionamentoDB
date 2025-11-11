from services.admin_services import admin_menu
from services.user_services import insert_user,login,limpar_terminal

while True:
    print(" 1- Criar Novo Usuário \n 2- Entrar \n 3- Sair do Sistema")
    opcao = int(input("Digite a Opção: "))

    if opcao == 1:
        limpar_terminal()
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")
        insert_user(email,password)
    elif opcao == 2:
        limpar_terminal()
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")
        user_logged = login(email,password)
        if user_logged:
            print("Usuário logado com sucesso!")
            admin_menu()
        else:
            print("Usuário ou senha incorreta!")
    else:
        break