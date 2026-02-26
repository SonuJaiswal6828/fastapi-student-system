import mysql.connector 

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sonu@1234",
        database="Sonu",
        autocommit=False,
        connection_timeout=10
)


