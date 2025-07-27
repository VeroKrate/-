import psycopg2
from config.settings import DB_CONFIG

class DatabaseConnector:
    def __init__(self):
        self.connection = None
    
    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()