import psycopg2
from config import config

def create_table():
    sql =  """
        CREATE TABLE snake_game_users (
            username VARCHAR (20),
            last_score INT
        );
    """
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
        
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

create_table()