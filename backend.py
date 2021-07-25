import sqlite3

def cret():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Cafe(Bill_No text, Date_Time text,D_time text,Drinks text, Coffee text, French_Fres text,Burger text, Pizza text,Cheese_Burger text,Cost text,Service_Charge text,Tax text,Total text);")
    # print("Table created")
    cur.execute("CREATE TABLE IF NOT EXISTS Signup(username text, passwordd text);")
    cur.execute("CREATE TABLE IF NOT EXISTS Rates(frenchf number, cold_coffe number,hot_coffe number,capachuno number, burger number, pizza number, cburger number, coca_cola number, pepsi number, fanta number );")
    conn.commit()
    conn.close()
    

def adds(rand,Drinks,coffee,Fries,Burger,pizza,Cheese_burger,cost,Service_Charge,Tax,Total):
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Cafe VALUES(?,date('now'),time('now','localtime'),?,?,?,?,?,?,?,?,?,?)",\
               (rand,Drinks,coffee,Fries,Burger,pizza,Cheese_burger,cost,Service_Charge,Tax,Total))
    conn.commit()
    conn.close()

def adduser(username, password):
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Signup VALUES(?,?)",(username, password))
    conn.commit()
    conn.close()

def fet(user):
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Signup WHERE username = ? ",(user,))
    rows=cur.fetchone()
    conn.close()
    return rows

def sho():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Signup")
    rows=cur.fetchall()
    
    #  conn.commit()
    conn.close()
    return rows


def search(Date_Time):
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Cafe WHERE Date_Time = ?",(Date_Time,))
    rows=cur.fetchall()
    conn.close()
    return rows
    



def show():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Cafe")
    rows=cur.fetchall()
    conn.close()
    return rows

def rate(fff,ccc,hc,cap,bbb,ppp,cbb,ddd,pep,fan):
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Rates")
    cur.execute("INSERT INTO Rates VALUES(?,?,?,?,?,?,?,?,?,?)",(fff,ccc,hc,cap,bbb,ppp,cbb,ddd,pep,fan))
    conn.commit()
    conn.close()

def f():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT frenchf FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a1=ii
    conn.commit()
    conn.close()
    return a1

def c():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT cold_coffe FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def ch():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT hot_coffe FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def ca():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT capachuno FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def b():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT burger FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def p():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT pizza FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def cb():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT cburger FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def d():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT coca_cola FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def pe():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT pepsi FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a

def fa():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT fanta FROM Rates")
    rows=cur.fetchall()
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    for ii in r:
        a=ii
    conn.commit()
    conn.close()
    return a








cret()


    
