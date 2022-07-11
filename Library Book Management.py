#importing Tkinter Module
from tkinter import *
import tkinter.messagebox as m
import mysql.connector as c
from tkinter import ttk
#Creating Costomize Window
r=Tk()
r.title('Library Book Management')
r.iconbitmap('studicon.ico')
r.minsize(width=1000,height=600)
r.eval("tk::PlaceWindow . center")
tab = ttk.Notebook(r) 
window1= Frame(r,bg='skyblue')
window2=Frame(r,bg='skyblue')
window3=Frame(r,bg='skyblue')
window4=Frame(r,bg='skyblue')
tab.add(window1, text ='Insert') 
tab.add(window2, text ='Update')
tab.add(window3, text ='Delete')
tab.add(window4, text ='View') 
tab.pack(expand = 1,fill='both')

#Connect to MySQL
def CreateConn():
    return c.connect(user='root',passwd='12345',host='localhost',database='venkydb')

#Insert data
def InsertData():
    n=bn.get()
    a=atr.get()
    p=pb.get()
    y=yr.get()
    if (n=='' or a=='' or p==''):
        m.showinfo("Insert status: ","All Fields are fill mandatory")
    else:
        conn=CreateConn()
        cursor=conn.cursor()
        args=(n,a,p,y)
        query="insert into Book_Details(Book_name,Author_name,Publication,year) values(%s,%s,%s,%s)"
        cursor.execute(query,args)
        conn.commit()
        m.showinfo("Insert Status: ","Data Inserted")
        conn.close()
    
            
#Update Data
def Check():
    n=bn2.get()
    a=atr2.get()
    p=pb2.get()
    y=yr2.get()
    w=wbn.get()
    if n=='' or w=='':
        #print("Update status: ","All Fields are fill mandatory")
        m.showinfo("Update status: ","Book Name and Book Name* Fields are fill mandatory")
    else:
        query="update Book_Details set Book_name='{}',Author_name='{}',Publication='{}',year='{}' where Book_name='{}'".format(n,a,p,y,w)
        Update(query)
        
def Update(a):
    conn=CreateConn()
    cursor=conn.cursor()
    cursor.execute(a)
    conn.commit()
    if cursor.rowcount>0:
        m.showinfo("Upadte Status: ","Data Update...")
        conn.close()
    else:
        m.showinfo("Upadte Status: ","Data Not Found...")
        
        
#Delete data
def Delete():
    n=bn3.get()
    conn=CreateConn()
    cursor=conn.cursor()
    query="Delete from Book_details where Book_name='{}'".format(n)
    cursor.execute(query)
    conn.commit()
    if cursor.rowcount>0:
        m.showinfo("Delete Status: ","Selected Data Delete...")
        conn.close()
    else:
        m.showinfo('Delete Status: ','Selected Data Not Found!!!')

#View
def View():
    conn=CreateConn()
    cursor=conn.cursor()
    query='Select * from Book_details'
    cursor.execute(query)
    rows=cursor.fetchall()
    viewing.config(state='normal')
    viewing.delete('1.75','end')
    
    for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+' | '
        allrows+='\n'
        viewing.insert(END,allrows)
    viewing.config(state='disabled')

#Clear 
def Clear():
    viewing.config(state='normal')
    viewing.delete('1.75','end')
    viewing.config(state='disabled')
  
#Adding Label in Windows
#Window 1
head=Label(window1,text='Library Book Management',relief='ridge',bd=10,font=('times new roman',20,'bold'))
head.place(x=300,y=20)

bn=Label(window1,text="Book Name ",bd=5,width=10,font=('times new roman',16,'bold'))
bn.place(x=200, y=100)

atr=Label(window1, text="Author Name ",bd=5,width=10,font=('times new roman',16,'bold'))
atr.place(x=200, y=170)

pb=Label(window1, text="Publication ",bd=5,width=10,font=('times new roman',16,'bold'))
pb.place(x=200, y=240)

yr=Label(window1, text="Year ",bd=5,width=10,font=('times new roman',16,'bold'))
yr.place(x=200, y=310)

#Window 2

head=Label(window2,text='Library Book Management',relief='ridge',bd=10,font=('times new roman',20,'bold'))
head.place(x=300,y=20)

bn2=Label(window2,text="Book Name* ",bd=5,width=10,font=('times new roman',16,'bold'))
bn2.place(x=200, y=100)

atr2=Label(window2, text="Author Name ",bd=5,width=10,font=('times new roman',16,'bold'))
atr2.place(x=200, y=170)

pb2=Label(window2, text="Publication ",bd=5,width=10,font=('times new roman',16,'bold'))
pb2.place(x=200, y=240)

yr2=Label(window2, text="Year ",bd=5,width=10,font=('times new roman',16,'bold'))
yr2.place(x=200, y=310)

wbn=Label(window2,text="Book Name* ",bd=5,width=10,font=('times new roman',16,'bold'))
wbn.place(x=200, y=380)

note=Label(window2,text='NOTE* - Both Book Name* Fields are Mandatory',bg='red',fg='white',bd=5,font=('times new roman',12,'bold'))
note.place(x=250,y=530)

#Window 3

head=Label(window3,text='Library Book Management',relief='ridge',bd=10,font=('times new roman',20,'bold'))
head.place(x=300,y=20)

bn3=Label(window3,text="Book Name ",bd=5,width=10,font=('times new roman',16,'bold'))
bn3.place(x=200, y=100)

#adding Entry Box 
#Window 1
bn=Entry(window1,width=40,bd=5,font=('times new roman',14,'bold'))
bn.place(x=350, y=100)

atr=Entry(window1,width=40,bd=5,font=('times new roman',14,'bold'))
atr.place(x=350, y=170)

pb=Entry(window1,width=40,bd=5,font=('times new roman',14,'bold'))
pb.place(x=350, y=240)

yr=Entry(window1,width=40,bd=5,font=('times new roman',14,'bold'))
yr.place(x=350, y=310)

#Window 2

bn2=Entry(window2,width=40,bd=5,font=('times new roman',14,'bold'))
bn2.place(x=350, y=100)

atr2=Entry(window2,width=40,bd=5,font=('times new roman',14,'bold'))
atr2.place(x=350, y=170)

pb2=Entry(window2,width=40,bd=5,font=('times new roman',14,'bold'))
pb2.place(x=350, y=240)

yr2=Entry(window2,width=40,bd=5,font=('times new roman',14,'bold'))
yr2.place(x=350, y=310)

wbn=Entry(window2,width=40,bd=5,font=('times new roman',14,'bold'))
wbn.place(x=350, y=380)

#Window 3

bn3=Entry(window3,width=40,bd=5,font=('times new roman',14,'bold'))
bn3.place(x=350, y=100)

#Window 4

head=Label(window4,text='Library Book Management',relief='ridge',bd=10,font=('times new roman',20,'bold'))
head.place(x=300,y=20)

viewing=Text(window4,width=75,height=22)
viewing.pack()
viewing.place(x=180,y=100)
viewing.insert(END,f"      Book Name    |     Author Name     |     Publication    |    Year    \n")
viewing.config(state='disabled')

#Adding Button
button=Button(window1,text="Insert",width=20,bg='white',command=InsertData,font=('times new roman',14,'bold'))
button.pack()
button.place(x=400,y=400)
button=Button(window2,text="Update",width=20,bg='white',command=Check,font=('times new roman',14,'bold'))
button.pack()
button.place(x=400,y=450)
button=Button(window3,text="Delete",width=20,bg='red',command=Delete,font=('times new roman',14,'bold'))
button.pack()
button.place(x=400,y=250)
button=Button(window4,text="View All",width=20,bg="pink",command=View,font=('times new roman',14,'bold'))
button.pack()
button.place(x=250,y=500)
button=Button(window4,text="Clear",width=20,bg="red",command=Clear,font=('times new roman',14,'bold'))
button.pack()
button.place(x=500,y=500)



r.mainloop()