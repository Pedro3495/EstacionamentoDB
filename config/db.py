import psycopg2


def criar_conexao():
    try:
        connection = psycopg2.connect(
            dbname = 'estacionamentodb',
            user = 'postgres',
            password = '1234',
            host = 'localhost',
            port = '5432'
        )
        print("Conexão com Sucesso!")
        return connection
    except Exception as e:
        print(f"Error de conexão: {e}")