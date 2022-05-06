import psycopg2
from config import config
 
def create_table():
    command = """
        CREATE TABLE Phonebook (
            First_name VARCHAR (20) UNIQUE NOT NULL,
            Last_name VARCHAR (20) UNIQUE NOT NULL,
            Phone_number VARCHAR (17) UNIQUE NOT NULL
        );
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
create_table()