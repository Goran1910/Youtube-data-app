import mysql.connector

class MySQLRepository:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='korisnik1',
            password='12345',
            database='youtube_data'
        )
    
        
        