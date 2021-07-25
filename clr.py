import sqlite3

def cler():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Rates VALUES(0,0,0,0,0,0,0,0,0,0)")
    print("Table inserted")
    conn.commit()
    conn.close()
cler()