import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "Sonu@1234"),
        database=os.getenv("DB_NAME", "Sonu"),
        autocommit=False,
        connection_timeout=10
    )