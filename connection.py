import pyodbc

conn = pyodbc.connect("DRIVER={SQL Server};SERVER=.;DATABASE=iStockCoop")

def connection_databases():
    if conn:
        print("Connection successful",conn)
        code = 1
        return code
    else:
        print("Connection failed",conn)
        code = 2
        return code

def Execute_data(query):
    select = conn.cursor()

    select.execute(query)

    row = select.fetchall()

    conn.commit()
    return row

def Execute_data_insert(query):
    select = conn.cursor()

    select.execute(query)

    conn.commit()

    try:
        row = select.fetchall()
    except :
        row = None

    
    return row