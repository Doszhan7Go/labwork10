import psycopg2
from config import config


def insert(first_name, last_name, number):
    sql = """
    INSERT INTO phonebook(First_name,Last_name, Phone_number)
    VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, last_name, number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
first_name = input()
last_name = input()
phone_number = input()
insert(first_name, last_name, phone_number)