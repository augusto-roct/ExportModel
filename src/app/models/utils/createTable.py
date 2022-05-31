from sqlite3 import Error

async def CreateTable(conn, createTableSql):
    try:
        cursor = conn.cursor()
        cursor.execute(createTableSql)
    except Error as e:
        print(e)