from config.db import criar_conexao



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





def insert_ticketmensal(parking_space: int, id_client: int, due_date: str):
    try:
        connection = criar_conexao()
        cursor = connection.cursor()

        sql = "INSERT INTO TICKET_MONTH (ID_CLIENT, PARKING_SPACE, DUE_DATE) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id_client, parking_space, due_date))
        connection.commit()
        
        print("Ticket mensal cadastrado com sucesso!")
        

    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
