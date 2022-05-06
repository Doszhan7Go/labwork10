import psycopg2
from config import config

def insert(first_name):
    sql = """
    DELETE FROM phonebook where "first_name"=%s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(first_name,))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


print('Whose number you want to delete?')
name=input()
insert(name)