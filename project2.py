import tkinter 
from tkinter import *
from tkinter import messagebox
import time
import random
import win32print  
import backend
import os
import datetime
        
# =====================================MAIN SCREEN================================================================

def main_screen():
    # rots=Tk()
    # rots.geometry('500x500')
    # rots.title('Login')

    # ff=Frame(rots,width = 450,height=450,relief="sunken").pack()

    # username=StringVar()
    # User=Label(ff, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bd=10,anchor='w').pack()
    # Userent=Entry(ff,font=('ariel' ,16,'bold'), textvariable=username , bd=6,insertwidth=4,bg="white" ,justify='left').pack()

    # password=StringVar()
    # Pass=Label(ff, font=( 'aria' ,16, 'bold' ),text="Password",fg="blue",bd=10,anchor='w').pack()
    # Passent=Entry(ff,font=('ariel' ,16,'bold'), textvariabl=password , bd=6,insertwidth=4,bg="white" ,justify='left').pack()













    root=Tk()
    root.geometry("1350x750+0+0")
    root.title("CAFE BILLING SYSTEM")

# =============================================PRINT CODE===========================================================

    def Print():
        r="receipt.docx"
        file=open(r,'w')
        file.writelines(str(txtReceipt))
        file.close()


        # os.system("lpr -P FleetSheet SM-G7102 (515b6b) receipt.docx")





    #     # txtReceipt.print()
    #     # os.system(Ctrl+p)


        # printer_name = win32print.GetDefaultPrinter()
        # hPrinter = win32print.OpenPrinter(printer_name)
        # hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
        # win32print.StartPagePrinter(hPrinter)
        # win32print.WritePrinter(hPrinter, bytes("Hello", "utf-8")
        # win32print.EndPagePrinter(hPrinter)

        # win32print.EndDocPrinter(hPrinter)
        # win32print.ClosePrinter(hPrinter)


        # p = win32print.OpenPrinter("FleetSheet SM-G7102c (e78828)")
        # # vv="Hello World"
        # stri = bytes("Hello World",'UTF-8')
        # job = win32print.StartDocPrinter(p, 1, ("This is RAW Data", None, "RAW")) 
        # win32print.StartPagePrinter(p)
        # win32print.WritePrinter(p,stri)
        # win32print.EndPagePrinter(p)

        
        # printer = getNetworkPrinter(commandSet='Generic')(host='192.168.1.102' , port = 9100)
        # printer.text("Hello World")
        # printer.lf()
        # return printer

        


# ==============================================MAIN SCREEN FRAMES=================================================== 

    Tops=Frame(root,bg="white",width = 1350,height=100,relief="sunken")
    Tops.pack(side=TOP)

    f1=Frame(root,width = 900,height=800,relief="sunken")
    f1.pack(side=LEFT)

    f2=Frame(root,width = 490,height=435,bd=4,relief="raised")
    f2.pack(side=RIGHT)

# ====================================================================================================================

# =====================================TIME CODE========================================================================

    localtime=time.asctime(time.localtime(time.time()))
    date=datetime.date.today()
    d=str(date)
    
    # print(type(d)) 
    print(d)  
    

# ======================================TOP LABEL AND TIME INFO========================================================

    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="CAFE BILLING SYSTEM",fg="Blue",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)

# ==============================================================================================================================

# =========================================RECEIPT FUNCTION======================================================================

    def receipt():
        txtReceipt.delete("1.0", END)

        txtReceipt.insert(END, '\t\tCAFE BILLING SYSTEM\n')
        txtReceipt.insert(END, '\nBill No: \t'+rand.get()+"\t\t\t"+str(localtime)+"\n")
        txtReceipt.insert(END, '---------------------------------------------------------------------------------------')
        txtReceipt.insert(END, '\nItems\t\t'+'Quantity\t\t'+"Price \n\n")
        
        if Fries.get() != '0':
            txtReceipt.insert(END, 'Fries:\t\t'+str(Fries.get())+'\t\t'"25"'\n')
        if Drinks.get() != '0':
            txtReceipt.insert(END, 'Drinks:\t\t'+str(Drinks.get())+'\t\t'"35"'\n')
        if coffee.get() != '0':
            txtReceipt.insert(END, 'Coffee:\t\t'+str(coffee.get())+'\t\t'"40"'\n')
        if pizza.get() != '0':
            txtReceipt.insert(END, 'Pizza:\t\t'+str(pizza.get())+'\t\t'"50"'\n')
        if Cheese_burger.get() != '0':
            txtReceipt.insert(END, 'Cheese Burger:\t\t'+str(Cheese_burger.get())+'\t\t'"40"'\n')
        if Burger.get() != '0':
            txtReceipt.insert(END, 'Burger:\t\t'+str(Burger.get())+'\t\t'"35"'\n')

        txtReceipt.insert(END, '------------------------------------------------------------')

        if cost.get() != '0':
            txtReceipt.insert(END, '\nCost of Items:\t\t'+cost.get()+'\n')
        if Service_Charge.get() != '0':
            txtReceipt.insert(END, 'Service Charge:\t\t'+Service_Charge.get()+'\n')
        if Tax.get() != '0':
            txtReceipt.insert(END, 'TAX:\t\t'+Tax.get()+'\n')
        if Total.get() != '0':
            txtReceipt.insert(END, 'Total:\t\t'+Total.get()+'\n')

        txtReceipt.insert(END, '------------------------------------------------------------')
    

# ================================== CALCULATION FUNCTION =======================================================================

    def Ref():
        bill=random.randint(12980, 50876)
        randomRef = str(bill)
        rand.set(randomRef)

        cof =float(Fries.get())
        coco= float(coffee.get())
        cob= float(Burger.get())
        copi= float(pizza.get())
        cochee= float(Cheese_burger.get())
        codr= float(Drinks.get())

        costoffries = cof*30
        costofcoffee = coco*45
        costofburger = cob*40
        costofpizza = copi*55
        costofcheeseburger = cochee*45
        costofdrinks = codr*40

        costofmeal = "Rs.",str('%.2f'% (costoffries +  costofcoffee + costofburger + costofpizza + costofcheeseburger + costofdrinks))
        PayTax=((costoffries +  costofcoffee + costofburger + costofpizza +  costofcheeseburger + costofdrinks)*0.33)
        Totalcost=(costoffries +  costofcoffee + costofburger + costofpizza  + costofcheeseburger + costofdrinks)
        Ser_Charge=((costoffries +  costofcoffee + costofburger + costofpizza + costofcheeseburger + costofdrinks)/99)
        Service="Rs.",str('%.2f'% Ser_Charge)
        OverAllCost="Rs.",str('%.2f' %( PayTax + Totalcost + Ser_Charge))
        PaidTax="Rs.",str('%.2f'% PayTax)

        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)

        if Drinks.get()!='0' or coffee.get()!='0' or Fries.get()!='0' or Burger.get()!='0' or pizza.get()!='0' or Cheese_burger.get()!='0':
            backend.adds(str(rand.get()),d,Drinks.get(),coffee.get(),Fries.get(),Burger.get(),pizza.get(),Cheese_burger.get(),cost.get(),Service_Charge.get(),Tax.get(),Total.get())
  


# ===============================================RESET============================================================

    def reset():
        rand.set("")
        Fries.set("0")
        coffee.set("0")
        Burger.set("0")
        pizza.set("0")
        Subtotal.set("")
        Total.set("")
        Service_Charge.set("")
        Drinks.set("0")
        Tax.set("")
        cost.set("")
        Cheese_burger.set("0")
        txtReceipt.delete("1.0",END)

# ========================================================================================================

    
# =================================TO EXIT THE MAIN WINDOW================================================
    def qexit():
        qexit=messagebox.askyesno("Quit System","Do you want to quit?")
        if qexit > 0:
            root.destroy()
            return


# =================================Labels and Entry for Items===============================================
                 
    rand = StringVar()
    lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Bill No.",fg="brown",bd=20,anchor='w')
    lblreference.grid(row=0,column=0)
    txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="white" ,justify='left',state="readonly")
    txtreference.grid(row=0,column=1)
    txtreference.focus_set()
    

    Drinks = StringVar()
    lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
    lblDrinks.grid(row=1,column=0)
    txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtDrinks.insert(0,0)
    txtDrinks.grid(row=1,column=1) 
    txtDrinks.focus_set()

    Fries = StringVar()
    lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text=" French Fries ",fg="blue",bd=10,anchor='w')
    lblfries.grid(row=2,column=0)
    txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtfries.insert(0,0)
    txtfries.grid(row=2,column=1)
    txtfries.focus_set()

    coffee = StringVar()
    lblcoffee = Label(f1, font=( 'aria' ,16, 'bold' ),text="Coffee ",fg="blue",bd=10,anchor='w')
    lblcoffee.grid(row=3,column=0)
    txtcoffee = Entry(f1,font=('ariel' ,16,'bold'), textvariable=coffee , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtcoffee.insert(0,0)
    txtcoffee.grid(row=3,column=1)
    txtcoffee.focus_set()

    Burger = StringVar()
    lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger ",fg="blue",bd=10,anchor='w')
    lblburger.grid(row=4,column=0)
    txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtburger.insert(0,0)
    txtburger.grid(row=4,column=1)
    txtburger.focus_set()

    pizza = StringVar()
    lblpizza = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bd=10,anchor='w')
    lblpizza.grid(row=5,column=0)
    txtpizza = Entry(f1,font=('ariel' ,16,'bold'), textvariable=pizza , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtpizza.insert(0,0)
    txtpizza.grid(row=5,column=1)
    txtpizza.focus_set()

    Cheese_burger = StringVar()
    lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese Burger",fg="blue",bd=10,anchor='w')
    lblCheese_burger.grid(row=6,column=0)
    txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtCheese_burger.insert(0,0)
    txtCheese_burger.grid(row=6,column=1)
    txtCheese_burger.focus_set()


# ==================================TOTAL COST TAX LABEL AND ENTRY==================================================
    
    cost = StringVar()
    lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
    lblcost.grid(row=0,column=2)
    txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right',state="readonly")
    txtcost.grid(row=0,column=3)

    Service_Charge = StringVar()
    lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
    lblService_Charge.grid(row=1,column=2)
    txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right',state="readonly")
    txtService_Charge.grid(row=1,column=3)

    Tax = StringVar()
    lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
    lblTax.grid(row=2,column=2)
    txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right',state='readonly')
    txtTax.grid(row=2,column=3)

    Subtotal = StringVar()
    lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
    lblSubtotal.grid(row=3,column=2)
    txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right',state='readonly')
    txtSubtotal.grid(row=3,column=3)

    Total = StringVar()
    lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
    lblTotal.grid(row=4,column=2)
    txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right',state='readonly')
    txtTotal.grid(row=4,column=3)

    lblTotal = Label(f1,text="---------------------",fg="white")
    lblTotal.grid(row=7,columnspan=3)

    lblTotal = Label(f1,text="---------------------",fg="white")
    lblTotal.grid(row=9,column=0)

# =================================BUTTONS=================================================================================

    btnTotal=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="steel blue",command=Ref)
    btnTotal.grid(row=8, column=1)
    

    btnreset=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="steel blue",command=reset)
    btnreset.grid(row=8, column=2)

    btnexit=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="steel blue",command=qexit)
    btnexit.grid(row=10, column=3)


    btnreceipt=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RECEIPT", bg="steel blue",command=receipt)
    btnreceipt.grid(row=10, column=1)
    

    #==============================================Receipt====================================================
    
   

    txtReceipt = StringVar()
    lblReceipt = Label(f2, font=('arial', 12, 'bold'), text="Receipt:",bd = 2, anchor = "w")
    lblReceipt.grid(row = 0, column = 0, sticky = W)
    txtReceipt = Text(f2, font=('arial', 11, 'bold'), width = 55, height =25, bg="white", bd=8,state="normal")
    txtReceipt.grid(row = 1, column = 0)



    # ======================================================================================================== 

    
    btnprint=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT", bg="steel blue",command=Print)
    btnprint.grid(row=10, column=0)

    # ================================================PRICE BUTTON WINDOW========================================================

    def price():
        rootz = Tk()
        rootz.geometry("500x250+0+0")
        rootz.title("Items Price List Info")

        lblinfo = Label(rootz, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)

        lblinfo = Label(rootz, font=('aria', 15,'bold'), text="              ", fg="white", anchor=W)
        lblinfo.grid(row=0, column=1)

        lblinfo = Label(rootz, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)

        ffinfo = Label(rootz, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
        ffinfo.grid(row=1, column=0)

        ffcinfo = Label(rootz, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
        ffcinfo.grid(row=1, column=3)

        cofinfo = Label(rootz, font=('aria', 15, 'bold'), text="Coffee ", fg="steel blue", anchor=W)
        cofinfo.grid(row=2, column=0)

        cofcinfo = Label(rootz, font=('aria', 15, 'bold'), text="45", fg="steel blue", anchor=W)
        cofcinfo.grid(row=2, column=3)

        buinfo = Label(rootz, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
        buinfo.grid(row=3, column=0)

        bucinfo = Label(rootz, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
        bucinfo.grid(row=3, column=3)

        piinfo = Label(rootz, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
        piinfo.grid(row=4, column=0)

        picinfo = Label(rootz, font=('aria', 15, 'bold'), text="55", fg="steel blue", anchor=W)
        picinfo.grid(row=4, column=3)

        cbinfo = Label(rootz, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
        cbinfo.grid(row=5, column=0)

        cbcinfo = Label(rootz, font=('aria', 15, 'bold'), text="45", fg="steel blue", anchor=W)
        cbcinfo.grid(row=5, column=3)

        drinfo = Label(rootz, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
        drinfo.grid(row=6, column=0)


        drcinfo = Label(rootz, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
        drcinfo.grid(row=6, column=3)

        rootz.mainloop()

    btnprice=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="steel blue",command=price)
    btnprice.grid(row=8, column=0) 

    def database():
        import backend
        rootd = Tk()
        rootd.geometry("1168x700+0+0")
        rootd.title("Data Base")

        Topd=LabelFrame(rootd,bg="white",width = 700 ,height=700,relief="raised")
        Topd.pack(side=LEFT)


        lblitems=Label(Topd, font=( 'aria' ,9, 'bold' ),text="Bill_No.\t        Date/Time\t         Dr Co Fr Bu Pi Cb             COFM\t            Service\t\tTAX\t\tTotal",fg="Black",bd=10,anchor='w')
        lblitems.grid(row=0,column=0,sticky="w")

        scrollbar=Scrollbar(Topd,orient='vertical')
        scrollbar.grid(row=1,column=1,sticky='ns')
        

        rec_list=Listbox(Topd,width=97,height=30,font=('arial',12,'bold'),yscrollcommand=scrollbar.set,justify="left")
        rec_list.grid(row=1,column=0,padx=8)
        rec_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command= rec_list.yview)

        


        def display():
            rec_list.delete(0,END)
            # rec_list.insert(END,'Bill_No\t')
            for row in backend.show():
                rec_list.insert(END,row,str(" "))
        
        display()
        
        
        # lblTotal = Label(Topd,text="---------------------",fg="white")
        # lblTotal.grid(row=2,column=0)
       
    btndb=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SHOW DB", bg="steel blue",command=database)
    btndb.grid(row=10,column=2 )
    
    def search():
        import backend
        roots = Tk()
        roots.geometry("920x655+0+0")
        roots.title("Data Base")

        Topl=LabelFrame(roots,bg="white",width = 700 ,height=665,relief="raised")
        Topl.pack(side=LEFT)


        lblitems=Label(Topl, font=( 'aria' ,9, 'bold' ),text="Bill_No.\t        Date/Time\t         Dr Co Fr Bu Pi Cb             COFM\t            Service\t\tTAX\t\tTotal",fg="Black",bd=10,anchor='w')
        lblitems.grid(row=0,column=0,sticky="w")

        scrollbar=Scrollbar(Topl,orient='vertical')
        scrollbar.grid(row=1,column=1,sticky='ns')
        

        rec_listt=Listbox(Topl,width=97,height=30,font=('arial',12,'bold'),yscrollcommand=scrollbar.set,justify="left")
        rec_listt.grid(row=1,column=0,padx=8)
        rec_listt.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command= rec_listt.yview)

        # backend.search(sr.get())
        # df=str(sr.get())
        # print(sr.get())
        # df='2019-10-01'
        # print(type(df),'+',df)
        
        

        def disp():
            backend.search(sr.get())
            rec_listt.delete(0,END)
          
            # rec_list.insert(END,'Bill_No\t')
            # print(type(sr.get()),' : ',sr.get())############ DEBUG PURPOSE 
            for row in backend.search():
                rec_listt.insert(END,row,str(" "))
        disp()
        
        

    sr = StringVar()
    txtsearch = Entry(f1,font=('ariel' ,16,'bold'), textvariable=sr , bd=6,insertwidth=4,bg="white" ,justify='left')
    txtsearch.grid(row=6,column=3)
    lblsearch = Label(f1, font=( 'aria' ,16, 'bold' ),text="S.B.D",fg="red",bd=10,anchor='w')
    lblsearch.grid(row=6,column=2)

    btnsearch=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SEARCH", bg="steel blue",command=search)
    btnsearch.grid(row=8, column=3)

    
    
    

    root.mainloop()

main_screen()
