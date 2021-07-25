import sqlite3

# def create():
#     conn=sqlite3.connect('orcl.db')
#     cur=conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS USERINFO(Username text, Passwordd text);")
#     cur.execute('INSERT INTO USERINFO VALUES("client","client@123")')
#     conn.commit()
#     conn.close()

# def inst():
#     conn=sqlite3.connect('orcl.db')
#     cur=conn.cursor()
    
#     conn.close()



# def search():
#     conn=sqlite3.connect('orcl.db')
#     cur=conn.cursor()
#     cur.execute('SELECT * FROM USERINFO ')
#     row= cur.fetchall()
#     return row

# create()

#############################################################################



# rot=Tk()
#                 rot.geometry('500x500')
#                 rot.title('Login')
#                 ff=Frame(rot,width = 100,height=100,relief="sunken").pack(side=TOP)
                
#                 def pr():
#                         print('done')

                
#                 User=Label(ff, font=( 'aria' ,16, 'bold' ),text="Username",fg="blue",bd=10,anchor='w').pack()
#                 btnlogi=Button(ff,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text='LOGIN', bg="steel blue",state=NORMAL,command=pr).pack()
                    

                    
                    
                
#                 rot.mainloop()


def sh():
    conn=sqlite3.connect("orcl.db")
    cur=conn.cursor()
    cur.execute("SELECT frenchf FROM Rates")
    
    rows=cur.fetchall()
    
    r=[]
    for i in rows:
        for j in i:
            r.append(j)
    # print(r)
    for ii in r:
        a1=ii
    conn.commit()
    conn.close()
    return a1
    
print(sh())