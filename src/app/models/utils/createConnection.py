import sqlite3
from sqlite3 import Error

def CreateConnection(db_file):
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print("Database UP, version: ", sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
    return conn