from config.db import criar_conexao
import os


def insert_client(client_name: str, cpf: str):
    connection = None
    cursor = None
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "INSERT INTO client(client_name, CPF) VALUES (%s, %s) RETURNING id_client"
        cursor.execute(sql, (client_name, cpf))
        id_client = cursor.fetchone()[0]  # Captura o id gerado
        connection.commit()
        print("Cliente cadastrado com sucesso!")
        return id_client
    
    except Exception as e:
        print(e)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def insert_ticketmensal(parking_space: str, id_client: int, due_date: str):
    connection = None
    cursor = None
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "INSERT INTO TICKET_MONTH (ID_CLIENT, PARKING_SPACE, DUE_DATE) VALUES (%s, %s, %s) RETURNING ID_TICKET_MONTH"
        cursor.execute(sql, (id_client, parking_space, due_date))
        id_ticket = cursor.fetchone()[0]  # Agora funciona!
        connection.commit()
        print("Ticket mensal cadastrado com sucesso!")
        return id_ticket
    except Exception as e:
        print(f"Erro ao inserir ticket: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def login(user:str ,senha: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM USUARIOS where EMAIL=%s and password=%s"
        cursor.execute(sql,(user,senha))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(e)

def insert_user(email: str, password: str):
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "INSERT INTO usuarios(email, password) VALUES (%s, %s)"
        cursor.execute(sql, (email, password))
        connection.commit()
    
    except Exception as e:
        print(e)
    cursor.close()
    connection.close()

def ver_ticket_mensal():
    connection = None
    cursor = None
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "SELECT * FROM TICKET_MONTH"
        cursor.execute(sql)  # Sem parâmetros desnecessários
        tickets = cursor.fetchall()  # Pega todos os registros
        return tickets
    except Exception as e:
        print(f"Erro ao buscar tickets: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def limpar_terminal():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux e Mac
    else:
        os.system('clear')

def buscar_nome_cpf_do_cliente(id_cliente: int):
    connection = None
    cursor = None
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "SELECT CLIENT_NAME, CPF FROM CLIENT WHERE ID_CLIENT =%s"
        cursor.execute(sql,(id_cliente,))  # Sem parâmetros desnecessários
        result = cursor.fetchone()
        if result:
            name, cpf = result
            return name, cpf
    except Exception as e:
        print(f"Erro ao buscar dados do cliente: {e}")
        return None, None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



def vaga_disponivel(parking_space: str):
    connection = None
    cursor = None
    try:
        connection = criar_conexao()
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM TICKET_MONTH WHERE PARKING_SPACE =%s"
        cursor.execute(sql, (parking_space,))
        result = cursor.fetchone()
        return result[0] == 0
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
