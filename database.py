import psycopg2

cn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Doszhan777",
    host = "localhost",
    port = "5432"
)

cn.autocommit = True
cr = cn.cursor()
sql = """CREATE database phone"""
cr.execute(sql)
print("Database created successfully........")
