import psycopg2

cursor = None
conn = None

def connect():
    
    global cursor
    global conn
    
    _conn = psycopg2.connect(database="postgres",
        host="localhost",
        user="postgres",
        password="6656",
        port="5432")
    _cursor = _conn.cursor()
    
    with open('db/schema.sql', 'r') as f:
        _cursor.execute(f.read())
        
    _conn.commit()
    cursor, conn = _cursor, _conn

class Database:
    
    cursor = None
    conn = None
    
    def __init__(self):
        if not cursor or not conn:
            connect()
        self.cursor, self.conn = cursor, conn
            
