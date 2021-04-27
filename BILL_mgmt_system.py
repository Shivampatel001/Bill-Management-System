from tkinter import*
import math
import random
from tkinter import messagebox
import os

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("BILL SYSTEM")
        self.root.geometry('1350x700+0+0') #width,height,position start,end
        bg_color='#1b1775'
        title=Label(self.root,text="BILLING SYSTEM",bg=bg_color,bd=12,fg='white',relief=GROOVE,font=("cursive",30,"bold"),pady=15).pack(pady=3,fill=X)

        #================================Varaible declatarion=====================================================================================================
        #----Costumer details frame---------------------------------
        self.cus_name=StringVar()
        self.cus_number=StringVar()
        self.billno=StringVar()
        self.x=random.randint(1111,9999)

        
        
        #----------------Items frame-----------------------------------------
        self.Item1=IntVar()
        self.Item2=IntVar()
        self.Item3=IntVar()
        self.Item4=IntVar()
        self.Item5=IntVar()
        self.Item6=IntVar()
        self.Item7=IntVar()
        self.Item8=IntVar()
        self.Item9=IntVar()
        self.Item10=IntVar()
        self.Item11=IntVar()
        self.Item12=IntVar()
        self.Item13=IntVar()
        self.Item14=IntVar()
        self.Item15=IntVar()
        self.Item16=IntVar()
        self.Item17=IntVar()
        self.Item18=IntVar()

        #-----------------------footer frame---------------------------------------
        self.grocery_price=StringVar()
        self.grocery_tax=StringVar()
        self.cosmetic_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.colddrink_price=StringVar()
        self.colddrink_tax=StringVar()

        #=========================================================================


        #-----------------COSTUMER SERVICE----------------------------------------------------------------------------------------------------------------------
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Costumer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=100,relwidth=1)

        cname_label=Label(F1,text="Costumer Name",bg=bg_color,fg='white',font=("thimes new roman",15,"bold"),pady=10).grid(row=0,column=0,padx=30)
        cname_text=Entry(F1,width=15,textvariable=self.cus_name,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cname_phone=Label(F1,text="Costumer Phone No.",bg=bg_color,fg='white',font=("thimes new roman",15,"bold")).grid(row=0,column=2,padx=35)
        cname_phntxt=Entry(F1,width=15,textvariable=self.cus_number,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cname_billsearch=Label(F1,text="Bill No.",bg=bg_color,fg='white',font=("thimes new roman",15,"bold")).grid(row=0,column=4,padx=35)
        cname_bill=Entry(F1,width=15,textvariable=self.billno,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        bill_button=Button(F1,text="Search",command=self.search_bill,bd=7,width=20,font=("times new roman",12,"bold")).grid(row=0,column=6,padx=34,pady=5)


        #--------------------------------------Cosmetics Frame----------------------------------------------------------------------------------------------------
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=188,width=310,height=390)

        Item1_lbl=Label(F2,text="Item1",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=15)
        Item1_ent=Entry(F2,width=13,textvariable=self.Item1,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10)

        Item2_lbl=Label(F2,text="Item2",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=15)
        Item2_ent=Entry(F2,width=13,textvariable=self.Item2,font=("arial",15),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10)

        Item3_lbl=Label(F2,text="Item3",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=15)
        Item3_ent=Entry(F2,width=13,textvariable=self.Item3,font=("arial",15),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10)

        Item4_lbl=Label(F2,text="Item4",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=15)
        Item4_ent=Entry(F2,width=13,textvariable=self.Item4,font=("arial",15),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10)

        Item5_lbl=Label(F2,text="Item5",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=15)
        Item5_ent=Entry(F2,width=13,textvariable=self.Item5,font=("arial",15),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10)

        Item6_lbl=Label(F2,text="Item6",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=15)
        Item6_ent=Entry(F2,width=13,textvariable=self.Item6,font=("arial",15),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10)

                
        #---------------------------------drinks--------------------------------------------------------------------------------------------------------------
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=315,y=188,width=310,height=390)

        Item7_lbl=Label(F2,text="Item7",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=15)
        Item7_ent=Entry(F2,width=13,textvariable=self.Item7,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10)

        Item8_lbl=Label(F2,text="Item8",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=15)
        Item8_ent=Entry(F2,width=13,textvariable=self.Item8,font=("arial",15),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10)

        Item9_lbl=Label(F2,text="Item9",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=15)
        Item9_ent=Entry(F2,width=13,textvariable=self.Item9,font=("arial",15),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10)

        Item10_lbl=Label(F2,text="Item10",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=15)
        Item10_ent=Entry(F2,width=13,textvariable=self.Item10,font=("arial",15),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10)

        Item11_lbl=Label(F2,text="Item11",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=15)
        Item11_ent=Entry(F2,width=13,textvariable=self.Item11,font=("arial",15),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10)

        Item12_lbl=Label(F2,text="Item12",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=15)
        Item12_ent=Entry(F2,width=13,textvariable=self.Item12,font=("arial",15),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10)


        #------------------------------------------------------Meals----------------------------------------------------------------------------------
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Colddrinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=625,y=188,width=310,height=390)

        Item13_lbl=Label(F3,text="Item13",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=15)
        Item13_ent=Entry(F3,width=13,textvariable=self.Item13,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10)

        Item14_lbl=Label(F3,text="Item14",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=15)
        Item14_ent=Entry(F3,width=13,textvariable=self.Item14,font=("arial",15),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10)

        Item15_lbl=Label(F3,text="Item15",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=15)
        Item15_ent=Entry(F3,width=13,textvariable=self.Item15,font=("arial",15),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10)

        Item16_lbl=Label(F3,text="Item16",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=15)
        Item16_ent=Entry(F3,width=13,textvariable=self.Item16,font=("arial",15),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10)

        Item17_lbl=Label(F3,text="Item17",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=15)
        Item17_ent=Entry(F3,width=13,textvariable=self.Item17,font=("arial",15),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10)

        Item18_lbl=Label(F3,text="Item18",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=15)
        Item18_ent=Entry(F3,width=13,textvariable=self.Item18,font=("arial",15),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10)
    

    #------------------------------------------------calc----------------------------------------------------------------------------------------------------------
        self.str1=""
        v=StringVar()
        def clear_data():
            self.str1=""
            v.set("")
        def btnpress(value):
            global str1
            self.str1=self.str1+str(value)
            v.set("")
            v.set(self.str1)
        def equals1():
            global str1
            x=eval(self.str1)        
            v.set(str(x))


        F4=LabelFrame(self.root,text="Calculator",bg=bg_color,bd=10,relief=GROOVE,fg='gold',font=("times new roman",15,"bold"))
        F4.place(x=935,y=188,width=280,height=390)
        calc_ent=Entry(F4,width=40,bd=5,textvariable=v,relief=SUNKEN,font=("arial",8)).grid(row=0,rowspan=1,columnspan=5,padx=5,pady=15)

        but_7=Button(F4,height=1,width=3,bd=3,bg="white",fg="black",text='7',font=("bold"),command=lambda:btnpress(7)).grid(row=1,column=0,pady=15,padx=0)
        but_8=Button(F4,height=1,width=3,bd=3,bg="white",fg="black",text='8',font=("bold"),command=lambda:btnpress(8)).grid(row=1,column=1,pady=15,padx=0)
        but_9=Button(F4,height=1,width=3,bd=3,bg="white",fg="black",text='9',font=("bold"),command=lambda:btnpress(9)).grid(row=1,column=2,pady=15,padx=0)
        but_div=Button(F4,height=1,width=3,bd=3,bg="white",fg="black",text='/',font=("bold"),command=lambda:btnpress('/')).grid(row=1,column=3,pady=15,padx=0)
        but_mul=Button(F4,height=1,width=3,bd=3,bg="white",fg="black",text='*',font=("bold"),command=lambda:btnpress('*')).grid(row=1,column=4,pady=15,padx=0)

        but_4=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='4',font=("bold"),command=lambda:btnpress(4)).grid(row=2,column=0,pady=10,padx=0)
        but_5=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='5',font=("bold"),command=lambda:btnpress(5)).grid(row=2,column=1,pady=10,padx=0)
        but_6=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='6',font=("bold"),command=lambda:btnpress(6)).grid(row=2,column=2,pady=10,padx=0)
        but_add=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='+',font=("bold"),command=lambda:btnpress('+')).grid(row=2,column=3,pady=10,padx=0)
        but_sub=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='-',font=("bold"),command=lambda:btnpress("-")).grid(row=2,column=4,pady=10,padx=0)

        but_1=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='1',font=("bold"),command=lambda:btnpress(1)).grid(row=3,column=0,pady=10,padx=0)
        but_2=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='2',font=("bold"),command=lambda:btnpress(2)).grid(row=3,column=1,pady=10,padx=0)
        but_3=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='3',font=("bold"),command=lambda:btnpress(3)).grid(row=3,column=2,pady=10,padx=0)
        but_0=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='0',font=("bold"),command=lambda:btnpress(0)).grid(row=3,column=3,pady=10,padx=0)
        but_dot=Button(F4,height=1,width=3,bd=5,bg="white",fg="black",text='.',font=("bold"),command=lambda:btnpress('.')).grid(row=3,column=4,pady=10,padx=0)
        
        but_cancel=Button(F4,height=1,width=27,bd=5,bg="white",fg="black",text='Cancel',font=("bold"),command=lambda:clear_data()).grid(row=4,columnspan=5,pady=10,padx=0)
        but_equals=Button(F4,height=1,width=27,bd=5,bg="white",fg="black",text='Enter',font=("bold"),command=lambda:equals1()).grid(row=5,columnspan=5,pady=8,padx=0)

        #---------------------------------------------------------------Bill Area-----------------------------------------------------

        F5=Frame(self.root,bd=10,bg="white",relief=GROOVE)
        F5.place(x=1215,y=188,width=385,height=391)
        lbl_bill=Label(F5,text="BILL AREA",bg="white",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.configure(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH)

       #--------------------------------Footer part-------------------------------------------------------------------------------------
        F6=LabelFrame(self.root,text="Tax",bg=bg_color,bd=10,relief=GROOVE,fg='gold',font=("times new roman",15,"bold"))
        F6.place(x=0,y=579,relwidth=1,height=259)



        Grocery_price=Label(F6,text="Grocery Price",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=0,column=0,padx=29,pady=20)
        Grocery_ent=Entry(F6,width=13,textvariable=self.grocery_price,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10)

        Cosmetic_price=Label(F6,text="Cosmetic Price",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=1,column=0,padx=30,pady=15)
        Cosmetic_ent=Entry(F6,width=13,textvariable=self.cosmetic_price,font=("arial",15),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10)

        Colddrink_price=Label(F6,text="Colddrink Price",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=2,column=0,padx=30,pady=15)
        Colddrink_ent=Entry(F6,width=13,textvariable=self.colddrink_price,font=("arial",15),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10)

        Grocery_tex=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=0,column=3,padx=30,pady=20)
        Grocerytax_ent=Entry(F6,width=13,textvariable=self.grocery_tax,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=4,padx=2)

        Cosmetic_tax=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=1,column=3,padx=30,pady=15)
        Cosmetictax_ent=Entry(F6,width=13,textvariable=self.cosmetic_tax,font=("arial",15),bd=5,relief=SUNKEN).grid(row=1,column=4,padx=2)

        Colddrink_tax=Label(F6,text="Colddrink Tax",bg=bg_color,fg="white",font=("arial",15,"bold")).grid(row=2,column=3,padx=30,pady=15)
        Colddrinktax_ent=Entry(F6,width=13,textvariable=self.colddrink_tax,font=("arial",15),bd=5,relief=SUNKEN).grid(row=2,column=4,padx=2)

        #-----------------------------------------------Button Layout---------------------------------------------------------------
        button_frame=Frame(F6,bg="white",bd=10,relief=GROOVE)
        button_frame.place(x=883,y=17,width=640,height=190)

        total_button=Button(button_frame,bd=4,text='Total',command=self.totalamt,relief=GROOVE,bg=bg_color,fg="white",width=20,height=3,font=("arial",10,"bold")).grid(row=0,column=0,padx=70,pady=5)
        clear_button=Button(button_frame,bd=4,text='Clear',command=self.clear_records,relief=GROOVE,bg=bg_color,fg="white",width=20,height=3,font=("arial",10,"bold")).grid(row=0,column=1,padx=70)
        bill_button=Button(button_frame,bd=4,text='Bill',command=self.bill_area,relief=GROOVE,bg=bg_color,fg="white",width=20,height=3,font=("arial",10,"bold")).grid(row=1,column=0,padx=70,pady=25)
        exit_button=Button(button_frame,bd=4,text='Exit',command=self.exit_but,relief=GROOVE,bg=bg_color,fg="white",width=20,height=3,font=("arial",10,"bold")).grid(row=1,column=1,padx=70)
        self.bill_start()
    def totalamt(self):
        #Total prices of Items for grocery
        self.Item1_price=self.Item1.get()*10                     #ASSIGNING price of item to variable     10=price of one item
        self.Item2_price=self.Item2.get()*10
        self.Item3_price=self.Item3.get()*10
        self.Item4_price=self.Item4.get()*10
        self.Item5_price=self.Item5.get()*10
        self.Item6_price=self.Item6.get()*10


        self.grocery_amount=(float(
                            (self.Item1_price)+
                            (self.Item2_price)+
                            (self.Item3_price)+
                            (self.Item4_price)+
                            (self.Item5_price)+
                            (self.Item6_price)                
                            ))

        self.grocery_price.set("Rs. "+str(self.grocery_amount))
        self.g_tax=round((self.grocery_amount*0.05),2)
        self.grocery_tax.set("Rs. "+ str(self.g_tax))               #Grocery tax=0.05

        #Total amount of prices for cosmetics
        self.Item7_price=self.Item7.get()*10
        self.Item8_price=self.Item8.get()*10
        self.Item9_price=self.Item9.get()*10
        self.Item10_price=self.Item10.get()*10
        self.Item11_price=self.Item11.get()*10
        self.Item12_price=self.Item12.get()*10
        self.cosmetics_amount=(float(
                                    (self.Item7_price)+
                                    (self.Item8_price)+
                                    (self.Item9_price)+
                                    (self.Item10_price)+
                                    (self.Item11_price)+
                                    (self.Item12_price)      
                                    ))

        self.cosmetic_price.set("Rs. "+str((self.cosmetics_amount)))
        self.c_tax=round((self.cosmetics_amount*0.05),2)
        self.cosmetic_tax.set("Rs. "+ str(self.c_tax))                 #Cosmetic tax=0.05

        #Total Item prices for colddrinks
        self.Item13_price=self.Item13.get()*10
        self.Item14_price=self.Item14.get()*10
        self.Item15_price=self.Item15.get()*10
        self.Item16_price=self.Item16.get()*10
        self.Item17_price=self.Item17.get()*10
        self.Item18_price=self.Item18.get()*10
        self.colddrinks_amount=(float(
                                    (self.Item13_price)+
                                    (self.Item14_price)+
                                    (self.Item15_price)+
                                    (self.Item16_price)+
                                    (self.Item17_price)+
                                    (self.Item18_price)   
                            
                            ))

        self.colddrink_price.set("Rs. "+str(self.colddrinks_amount))
        self.cd_tax=round((self.colddrinks_amount*0.05),2)
        self.colddrink_tax.set("Rs. "+ str(self.cd_tax))                    #Colddrink tax=0.05

    def bill_start(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome To Planet C53")
        self.textarea.insert(END,f"\nBill Bumber : {self.x}")
        self.textarea.insert(END,f"\nCostumer Name:{self.cus_name.get()}")
        self.textarea.insert(END,f"\nPhone no. :{self.cus_number.get()}")
        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,"\nProduct\t\t    QTY\t\t    Price")
        self.textarea.insert(END,"\n===========================================")
    def bill_area(self):
        if(self.cus_name.get()=="" or self.cus_number.get()==""):
            messagebox.showerror("Error","Costumer details are empty")

    
        elif(self.grocery_price.get()=="Rs. 0.0" and self.cosmetic_price.get()=="Rs. 0.0" and self.colddrink_price.get()=="Rs. 0.0"):
            messagebox.showerror("Error","No Product selected ")
        else:

            self.bill_start()
            if(self.Item1.get()!=0):
                self.textarea.insert(END,f"\nItem1:\t\t      {self.Item1.get()}\t\t     {self.Item1_price}")
            if(self.Item2.get()!=0):
                self.textarea.insert(END,f"\nItem2:\t\t      {self.Item2.get()}\t\t     {self.Item2_price}")
            if(self.Item3.get()!=0):
                self.textarea.insert(END,f"\nItem3:\t\t      {self.Item3.get()}\t\t     {self.Item3_price}")
            if(self.Item4.get()!=0):
                self.textarea.insert(END,f"\nItem4:\t\t      {self.Item4.get()}\t\t     {self.Item4_price}")
            if(self.Item5.get()!=0):
                self.textarea.insert(END,f"\nItem5:\t\t      {self.Item5.get()}\t\t     {self.Item5_price}")
            if(self.Item6.get()!=0):
                self.textarea.insert(END,f"\nItem6:\t\t      {self.Item6.get()}\t\t     {self.Item6_price}")
            if(self.Item7.get()!=0):
                self.textarea.insert(END,f"\nItem7:\t\t      {self.Item7.get()}\t\t     {self.Item7_price}")
            if(self.Item8.get()!=0):
                self.textarea.insert(END,f"\nItem8:\t\t      {self.Item8.get()}\t\t     {self.Item8_price}")
            if(self.Item9.get()!=0):
                self.textarea.insert(END,f"\nItem9:\t\t      {self.Item9.get()}\t\t     {self.Item9_price}")
            if(self.Item10.get()!=0):
                self.textarea.insert(END,f"\nItem10:\t\t      {self.Item10.get()}\t\t     {self.Item10_price}")
            if(self.Item11.get()!=0):
                self.textarea.insert(END,f"\nItem11:\t\t      {self.Item11.get()}\t\t     {self.Item11_price}")
            if(self.Item12.get()!=0):
                self.textarea.insert(END,f"\nItem12:\t\t      {self.Item12.get()}\t\t     {self.Item12_price}")
            if(self.Item13.get()!=0):
                self.textarea.insert(END,f"\nItem13:\t\t      {self.Item13.get()}\t\t     {self.Item13_price}")
            if(self.Item14.get()!=0):
                self.textarea.insert(END,f"\nItem14:\t\t      {self.Item14.get()}\t\t     {self.Item14_price}")
            if(self.Item15.get()!=0):
                self.textarea.insert(END,f"\nItem15:\t\t      {self.Item15.get()}\t\t     {self.Item15_price}")
            if(self.Item16.get()!=0):
                self.textarea.insert(END,f"\nItem16:\t\t      {self.Item16.get()}\t\t     {self.Item16_price}")
            if(self.Item17.get()!=0):
                self.textarea.insert(END,f"\nItem17:\t\t      {self.Item17.get()}\t\t     {self.Item17_price}")
            if(self.Item18.get()!=0):
                self.textarea.insert(END,f"\nItem18:\t\t      {self.Item18.get()}\t\t     {self.Item18_price}")

            self.textarea.insert(END,"\n-------------------------------------------")

            if(self.grocery_tax.get()!= "Rs. 0.0"):
                self.textarea.insert(END,f"\nGrocery Tax\t\t\t\t{self.grocery_tax.get()}")
            if(self.cosmetic_tax.get()!= "Rs. 0.0"):
                self.textarea.insert(END,f"\nCosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
            if(self.colddrink_tax.get()!= "Rs. 0.0"):
                self.textarea.insert(END,f"\nColddrink Tax\t\t\t\t{self.colddrink_tax.get()}")
            
            self.total_price=(
                                float(
                                    self.grocery_amount +
                                    self.cosmetics_amount +
                                    self.colddrinks_amount +
                                    self.g_tax +
                                    self.c_tax +
                                    self.cd_tax
                                )
                            )
            self.textarea.insert(END,f"\nTOTAL PRICE\t\t\t\tRs. {self.total_price}")
            self.bill()
    def bill(self):
        var=messagebox.askyesno("Save Bill","Do you want to save the bill")    #if yes then var will be assigned True
        if(var>0):
            self.bill_content=self.textarea.get("1.0",END)
            file1=open("E:/prjct/bills/"+ str(self.x)+".txt","w")           #CHANGE YOUR DIRECTORY HERE FOR BILLS FOLDER
            file1.write(self.bill_content)
            file1.close()
            messagebox.showinfo("Saved","Saved Sucessfully")
        else:
            return
    def exit_but(self):
        x=messagebox.askyesno("Exit","Do you want to exit")
        if(x>0):
            exit(0)

    def search_bill(self):
        var="NO"
        if(self.billno.get()==""):
                self.textarea.delete("1.0",END)
                self.bill_start()
        else:
            for i in os.listdir("E:/prjct/bills/"):
                if(i.split(".")[0]==self.billno.get()):     # 1724.txt split with "." [1724,txt]    searching with index[0] i.e 1724(bill no.)
                    file1=open(f"E:/prjct/bills/{i}","r")
                    self.textarea.delete("1.0",END)
                    for x in file1:
                        self.textarea.insert(END,x)
                    file1.close()
                    var="YES"
        if(var!="YES"):
            messagebox.showerror("Error","Invalid bill no")

    def clear_records(self):
        self.Item1.set(0)
        self.Item2.set(0)
        self.Item3.set(0)
        self.Item4.set(0)
        self.Item5.set(0)
        self.Item6.set(0)
        self.Item7.set(0)
        self.Item8.set(0)
        self.Item9.set(0)
        self.Item10.set(0)
        self.Item11.set(0)
        self.Item12.set(0)
        self.Item13.set(0)
        self.Item14.set(0)
        self.Item15.set(0)
        self.Item16.set(0)
        self.Item17.set(0)
        self.Item18.set(0)
        self.cus_name.set("")
        self.cus_number.set("")
        self.billno.set("")
        self.grocery_price.set("")
        self.grocery_tax.set("")
        self.cosmetic_price.set("")
        self.cosmetic_tax.set("")
        self.colddrink_price.set("")
        self.colddrink_tax.set("")
        self.textarea.delete("1.0",END)
        self.x=random.randint(1111,9999)
        self.bill_start()


       
root=Tk()                   #object of class tkinter
obj=Bill_App(root)          #passing root to class Bill_App
root.mainloop()
