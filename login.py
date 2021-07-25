import tkinter
from tkinter import *
import tkinter 
from tkinter import *
from tkinter import messagebox
import time
import random
import backend
import os
import datetime
import tempfile
from tkinter import ttk


global rots    
rots=Tk()
rots.geometry('500x600')
rots.title('User Login')

ff=Frame(rots,width = 100,height=100,relief="sunken").pack(side=TOP)

lg=Label(ff, font=( 'aria' ,20, 'bold' ),text="CAFE BILLING SYSTEM \n USER LOGIN / SIGNUP",fg="red",bd=10,anchor='w').pack(side=TOP)

def signup():
    if username.get() in dict(backend.sho()):
        username.set("")
        password.set("")
        qexit=messagebox.askretrycancel("Signup Error","Username Already Exists!!")

    elif username.get() and password.get() != " ":
            backend.adduser(username.get(),password.get())
            username.set("")
            password.set("")
            mid=Label(ff, font=( 'aria' ,16, 'bold' ),text="Registration Successfull!!",fg="green",bd=10,anchor='w').pack(side=BOTTOM)

    else:
        qexit=messagebox.askretrycancel("Signup Error","Please Enter Valid Details!!")



def veri():
    usern=username.get()
    passd=password.get()

    username.set("")
    password.set("")
    
    p=str(backend.fet(usern))
    if passd in p:
        
            rots.destroy()
            
            root=Tk()
            root.geometry("1350x750+0+0")
            root.title("CAFE BILLING SYSTEM") 

            Tops=Frame(root,bg="white",width = 1350,height=100,relief="sunken")
            Tops.pack(side=TOP)

            f1=Frame(root,width = 900,height=800,relief="sunken")
            f1.pack(side=LEFT)

            f2=Frame(root,width = 490,height=435,bd=4,relief="raised")
            f2.pack(side=RIGHT)

            localtime=time.asctime(time.localtime(time.time()))
            # date=datetime.date.today()
            # d=str(date)

            lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="CAFE BILLING SYSTEM",fg="Blue",bd=10,anchor='w')
            lblinfo.grid(row=0,column=0)
            lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
            lblinfo.grid(row=1,column=0) 
            lbllog = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Login: "+usern,fg="green",bd=20,anchor='se')
            lbllog.grid(row=1,column=1)   
                      
                
            def Print():
                r=txtReceipt.get('1.0','end-1c')
                filen = tempfile.mktemp('.txt')
                open(filen,'w').write(r)
                os.startfile(filen,'print')




               
            def receipt():
                txtReceipt.delete("1.0", END)

                txtReceipt.insert(END, '\t\tCAFE BILLING SYSTEM\n')
                txtReceipt.insert(END, '\nBill No :'+rand.get()+"\t\t\t"+str(localtime)+"\n")
                txtReceipt.insert(END, '------------------------------------------------------------------------------')
                txtReceipt.insert(END, '\nItems\t\t'+'Qty\t\t'+"Price\n\n")
                
                a=backend.f()
                b=backend.c()
                c=backend.b()
                ch=backend.ch()
                ca=backend.ca()
                d=backend.p()
                e=backend.cb()
                f=backend.d()
                pe=backend.pe()
                fa=backend.fa()


                if Fries.get() != '0':
                    txtReceipt.insert(END, 'Fries:  \t\t'+str(Fries.get())+'\t\t'+str(a)+'\n')
                if Drinks.get() != '0':
                    if drkcd.get() == "Coca Cola":
                        txtReceipt.insert(END,drkcd.get()+  '\t\t'+str(Drinks.get())+'\t\t'+str(f)+'\n')
                    elif drkcd.get() == "Pepsi":
                        txtReceipt.insert(END,drkcd.get()+  '\t\t'+str(Drinks.get())+'\t\t'+str(pe)+'\n')
                    else:
                        txtReceipt.insert(END,drkcd.get()+  '\t\t'+str(Drinks.get())+'\t\t'+str(fa)+'\n')


                if coffee.get() != '0':
                    if drkc.get() == "Cold Coffee":
                        txtReceipt.insert(END,drkc.get()+  '\t\t'+str(coffee.get())+'\t\t'+str(b)+'\n')
                    elif drkc.get() == "Hot Coffee":
                        txtReceipt.insert(END,drkc.get()+  '\t\t'+str(coffee.get())+'\t\t'+str(ch)+'\n')
                    else:
                        txtReceipt.insert(END,drkc.get()+  '\t\t'+str(coffee.get())+'\t\t'+str(ca)+'\n')
                        

                if pizza.get() != '0':
                    txtReceipt.insert(END, 'Pizza:  \t\t'+str(pizza.get())+'\t\t'+str(d)+'\n')
                if Cheese_burger.get() != '0':
                    txtReceipt.insert(END, 'CBurger:\t\t'+str(Cheese_burger.get())+'\t\t'+str(e)+'\n')
                if Burger.get() != '0':
                    txtReceipt.insert(END, 'Burger: \t\t'+str(Burger.get())+'\t\t'+str(c)+'\n')

                txtReceipt.insert(END, '------------------------------------------------------------\n')

                if cost.get() != '0':
                    txtReceipt.insert(END, 'Items Cost:    \t\t\t'+str(cost.get())+'\n')
                if Service_Charge.get() != '0':
                    txtReceipt.insert(END, 'Service Charge:\t\t\t'+Service_Charge.get()+'\n')
                if Tax.get() != '0':
                    txtReceipt.insert(END, 'TAX:           \t\t\t'+Tax.get()+'\n')
                if Total.get() != '0':
                    txtReceipt.insert(END, 'TOTAL:         \t\t\t'+Total.get()+'\n')

                txtReceipt.insert(END, '------------------------------------------------------------')

            def Ref():
                bill=random.randint(12980, 50876)
                randomRef = str(bill)
                rand.set(randomRef)

                a=backend.f()
                b=backend.c()
                c=backend.b()
                ch=backend.ch()
                ca=backend.ca()
                d=backend.p()
                e=backend.cb()
                f=backend.d()
                pe=backend.pe()
                fa=backend.fa()


                cof =float(Fries.get())
                coco= float(coffee.get())
                cob= float(Burger.get())
                copi= float(pizza.get())
                cochee= float(Cheese_burger.get())
                codr= float(Drinks.get())

                

                costoffries = cof*float(a)

                if drkc.get() == "Cold Coffee":
                    costofcoffee = coco*float(b)
                elif drkc.get() == "Hot Coffee":
                    costofcoffee = coco*float(ch)
                else:
                    costofcoffee = coco*float(ca)

                costofburger = cob*float(c)
                costofpizza = copi*float(d)
                costofcheeseburger = cochee*float(e)

                if drkcd.get() == "Coca Cola":
                    costofdrinks = codr*float(f)
                elif drkcd.get() == "Pepsi":
                    costofdrinks = codr*float(pe)
                else:
                    costofdrinks = codr*float(fa)

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
                    backend.adds(str(rand.get()),Drinks.get(),coffee.get(),Fries.get(),Burger.get(),pizza.get(),Cheese_burger.get(),cost.get(),Service_Charge.get(),Tax.get(),Total.get())
            
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



            def qexit():
                qexit=messagebox.askyesno("Quit System","Do you want to quit?")
                if qexit > 0:
                    root.destroy()
                    return 
                
                    

            rand = StringVar()
            lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Bill No.",fg="brown",bd=20,anchor='w')
            lblreference.grid(row=0,column=0)
            txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="white" ,justify='left',state="readonly")
            txtreference.grid(row=0,column=1)
            txtreference.focus_set()
            

            Drinks = StringVar()
            lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
            lblDrinks.grid(row=1,column=0)
            txtDrinks = Entry(f1,font=('ariel' ,8,'bold'), textvariable=Drinks , bd=6,insertwidth=1,bg="white" ,justify='left')
            txtDrinks.insert(0,0)
            txtDrinks.grid(row=1,column=1,sticky=E) 
            txtDrinks.focus_set()

            drkcd=StringVar()
            drinkcombo=ttk.Combobox(f1,width=12,textvariable=drkcd,state='readonly')
            drinkcombo['values']=('Coca Cola','Pepsi','Fanta')
            drinkcombo.grid(row=1,column=1,sticky= W)

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
            txtcoffee = Entry(f1,font=('ariel' ,8,'bold'), textvariable=coffee , bd=6,insertwidth=1,bg="white" ,justify='left')
            txtcoffee.insert(0,0)
            txtcoffee.grid(row=3,column=1,sticky=E)
            txtcoffee.focus_set()
            
            drkc=tkinter.StringVar()
            drinkcoffe=ttk.Combobox(f1,width=12,textvariable=drkc,state='readonly')
            drinkcoffe['values']=('Cold Coffee','Hot Coffee','Capachuno')
            drinkcoffe.grid(row=3,column=1,sticky= W)

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

            btnTotal=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="steel blue",command=Ref)
            btnTotal.grid(row=8, column=1)
            

            btnreset=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="steel blue",command=reset)
            btnreset.grid(row=8, column=2)

            btnexit=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="steel blue",command=qexit)
            btnexit.grid(row=10, column=3)


            btnreceipt=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RECEIPT", bg="steel blue",command=receipt)
            btnreceipt.grid(row=10, column=1)

            txtReceipt = StringVar()
            lblReceipt = Label(f2, font=('arial', 12, 'bold'), text="Receipt:",bd = 2, anchor = "w")
            lblReceipt.grid(row = 0, column = 0, sticky = W)
            txtReceipt = Text(f2, font=('arial', 11, 'bold'), width = 55, height =25, bg="white", bd=8,state="normal")
            txtReceipt.grid(row = 1, column = 0)

            btnprint=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT", bg="steel blue",command=Print)
            btnprint.grid(row=10, column=2)
            
            
            

            def price():
                import backend
                rootz = Tk()
                rootz.geometry("900x600+0+0")
                rootz.title("Items Price List Info")

                ft=Frame(rootz,width = 900,height=800,relief="sunken")
                ft.pack(side=TOP)

                
                a=backend.f()
                b=backend.c()
                c=backend.b()
                ch=backend.ch()
                ca=backend.ca()
                d=backend.p()
                e=backend.cb()
                f=backend.d()
                pe=backend.pe()
                fa=backend.fa()
                

                lblinfo = Label(ft, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
                lblinfo.grid(row=0, column=0)

                lblinfo = Label(ft, font=('aria', 15,'bold'), text="              ", fg="white", anchor=W)
                lblinfo.grid(row=0, column=1)

                lblinfo = Label(ft, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
                lblinfo.grid(row=0, column=3)

                ffinfo = Label(ft, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
                ffinfo.grid(row=1, column=0)

                
                # ff=StringVar()
                # txtff = Entry(ft,font=('ariel' ,16,'bold') ,textvariable=ff, bd=6,insertwidth=4,bg="white" ,justify='left',state='readonly')
                # txtff.grid(row=1,column=3)
                

                ffcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(a), fg="steel blue", anchor=W)
                ffcinfo.grid(row=1, column=3)

                

                cofinfo = Label(ft, font=('aria', 15, 'bold'), text="Coffee: ", fg="steel blue", anchor=W)
                cofinfo.grid(row=2, column=0)

                cofcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(b), fg="steel blue", anchor=W)
                cofcinfo.grid(row=3, column=3)

                cofinfo = Label(ft, font=('aria', 15, 'bold'), text="Cold Coffee ", fg="steel blue", anchor=W)
                cofinfo.grid(row=3, column=0)

                cofcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(ch), fg="steel blue", anchor=W)
                cofcinfo.grid(row=4, column=3)

                cofinfo = Label(ft, font=('aria', 15, 'bold'), text="Hot Coffee ", fg="steel blue", anchor=W)
                cofinfo.grid(row=4, column=0)

                cofcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(ca), fg="steel blue", anchor=W)
                cofcinfo.grid(row=5, column=3)

                cofinfo = Label(ft, font=('aria', 15, 'bold'), text="Capachuno ", fg="steel blue", anchor=W)
                cofinfo.grid(row=5, column=0)


                

                buinfo = Label(ft, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
                buinfo.grid(row=6, column=0)

                

                bucinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(c), fg="steel blue", anchor=W)
                bucinfo.grid(row=6, column=3)

                piinfo = Label(ft, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
                piinfo.grid(row=7, column=0)

               

                picinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(d), fg="steel blue", anchor=W)
                picinfo.grid(row=7, column=3)

                cbinfo = Label(ft, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
                cbinfo.grid(row=8, column=0)


                cbcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(e), fg="steel blue", anchor=W)
                cbcinfo.grid(row=8, column=3)

                drinfo = Label(ft, font=('aria', 15, 'bold'), text="Drinks:", fg="steel blue", anchor=W)
                drinfo.grid(row=9, column=0)

                drcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(f), fg="steel blue", anchor=W)
                drcinfo.grid(row=10, column=3)

                drinfo = Label(ft, font=('aria', 15, 'bold'), text="Coca Cola", fg="steel blue", anchor=W)
                drinfo.grid(row=10, column=0)

                drcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(pe), fg="steel blue", anchor=W)
                drcinfo.grid(row=11, column=3)

                drinfo = Label(ft, font=('aria', 15, 'bold'), text="Pepsi", fg="steel blue", anchor=W)
                drinfo.grid(row=11, column=0)

                drcinfo = Label(ft, font=('aria', 15, 'bold'), text=''+str(fa), fg="steel blue", anchor=W)
                drcinfo.grid(row=12, column=3)

                drinfo = Label(ft, font=('aria', 15, 'bold'), text="Fanta", fg="steel blue", anchor=W)
                drinfo.grid(row=12, column=0)



                

                lblinfo = Label(ft, font=('aria', 15,'bold'), text="              ", fg="white", anchor=W)
                lblinfo.grid(row=0, column=4)

                

                f=StringVar()
                txtf = Entry(ft,font=('ariel' ,16,'bold'), textvariable=f , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtf.grid(row=1,column=5)

                c=StringVar()
                txtc = Entry(ft,font=('ariel' ,16,'bold'), textvariable=c , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtc.grid(row=3,column=5)

                cold=StringVar()
                txtco = Entry(ft,font=('ariel' ,16,'bold'), textvariable=cold , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtco.grid(row=4,column=5)

                hotc=StringVar()
                txtch = Entry(ft,font=('ariel' ,16,'bold'), textvariable=hotc , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtch.grid(row=5,column=5)


                b=StringVar()
                txtb = Entry(ft,font=('ariel' ,16,'bold'), textvariable=b , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtb.grid(row=6,column=5)

                p=StringVar()
                txtp = Entry(ft,font=('ariel' ,16,'bold'), textvariable=p , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtp.grid(row=7,column=5)

                cb=StringVar()
                txtcb = Entry(ft,font=('ariel' ,16,'bold'), textvariable=cb , bd=6,insertwidth=4,bg="white" ,justify='left')
                txtcb.grid(row=8,column=5)

                d=StringVar()
                txtd = Entry(ft,font=('ariel' ,16,'bold') , textvariable=d,bd=6,insertwidth=4,bg="white" ,justify='left')
                txtd.grid(row=10,column=5)

                dcp=StringVar()
                txtdcp = Entry(ft,font=('ariel' ,16,'bold') , textvariable=dcp,bd=6,insertwidth=4,bg="white" ,justify='left')
                txtdcp.grid(row=11,column=5)

                dcf=StringVar()
                txtdcf = Entry(ft,font=('ariel' ,16,'bold') , textvariable=dcf,bd=6,insertwidth=4,bg="white" ,justify='left')
                txtdcf.grid(row=12,column=5)

                

                def save():
                    backend.rate(txtf.get(),txtc.get(),txtco.get(),txtch.get(),txtb.get(),txtp.get(),txtcb.get(),txtd.get(),txtdcp.get(),txtdcf.get())
                    

                btns=Button(ft,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SAVE", bg="steel blue",command=save)
                btns.grid(row=13, column=5)
                if usern == 'admin':
                    btns.config(state=NORMAL)
                else:
                    btns.config(state=DISABLED)


                rootz.mainloop()

            btnprice=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="steel blue",command=price)
            btnprice.grid(row=8, column=0) 
            

            def database():
                import backend
                rootd = Tk()
                rootd.geometry("914x647+0+0")
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

            btndb=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SHOW DB", bg="steel blue",command=database)
            btndb.grid(row=10,column=0 )
            if usern == 'admin':
                btndb.config(state=NORMAL)
            else:
                btndb.config(state=DISABLED)

            def search():
                import backend
                roots = Tk()
                roots.geometry("914x647+0+0")
                roots.title("Data Base Search Results")

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

                def disp():
                    
                    rec_listt.delete(0,END)
                    for row in backend.search(sr.get()):
                        rec_listt.insert(END,row,str(" "))
                disp()

            sr = StringVar()
            txtsearch = Entry(f1,font=('ariel' ,16,'bold'), textvariable=sr , bd=6,insertwidth=4,bg="white" ,justify='left')
            txtsearch.grid(row=6,column=3)
            if usern == 'admin':
                txtsearch.config(state=NORMAL)
            else:
                txtsearch.config(state=DISABLED)
            lblsearch = Label(f1, font=( 'aria' ,16, 'bold' ),text="S.B.D",fg="red",bd=10,anchor='w')
            lblsearch.grid(row=6,column=2)

            btnsearch=Button(f1,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SEARCH", bg="steel blue",command=search)
            btnsearch.grid(row=8, column=3)
            if usern == 'admin':
                btnsearch.config(state=NORMAL)
            else:
                btnsearch.config(state=DISABLED)
        

            root.mainloop()

    else:
        qexit=messagebox.askretrycancel("Login Error","Wrong Username Or Password!!")
        
        

username=StringVar()
User=Label(ff, font=( 'aria' ,16, 'bold' ),text="Username",fg="blue",bd=10,anchor='w').pack()
Userent=Entry(ff,font=('ariel' ,16,'bold'), textvariable=username , bd=6,insertwidth=4,bg="white" ,justify='left').pack()



password=StringVar()
Pass=Label(ff, font=( 'aria' ,16, 'bold' ),text="Password",fg="blue",bd=10,anchor='w').pack()
Passent=Entry(ff,font=('ariel' ,16,'bold'), textvariabl=password , bd=6,insertwidth=4,bg="white",show='*' ,justify='left').pack()


mid=Label(ff, font=( 'aria' ,16, 'bold' ),text="________",fg="white",bd=10,anchor='w').pack()

btnlogin=Button(ff,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text='LOGIN', bg="steel blue",command=veri).pack()

mid=Label(ff, font=( 'aria' ,16, 'bold' ),text="________",fg="white",bd=10,anchor='w').pack()

btnlogin=Button(ff,padx=0,pady=0, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text='SIGNUP', bg="steel blue",command=signup).pack()

rots.mainloop()



        
