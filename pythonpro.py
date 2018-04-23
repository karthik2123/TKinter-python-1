from tkinter import*
import os

w=Tk("myproject")
l1=Label(w,text="Book Name")
l2=Label(w,text="Author")
l3=Label(w,text="Id")
l4=Label(w,text="arrival date")
l5=Label(w,text="Available")

count=0

s1=StringVar()
t1=Entry(w,textvariable=s1)
s2=StringVar()
t2=Entry(w,textvariable=s2)
s3=StringVar()
t3=Entry(w,textvariable=s3)
s4=StringVar()
t4=Entry(w,textvariable=s4)
s5=StringVar()
t5=Entry(w,textvariable=s5)

def addrec():
    f=open("pydatabase.txt",'a+')
    
    a=t1.get()
    b=t2.get()
    c=t3.get()
    d=t4.get()
    e=t5.get()
    f.writelines(a+""+b+""+c+""+d+""+e+""+"\n")
    f.close
    
    
    



def nextrec():
    f=open("pydatabase.txt",'r')
    global count
    i=0
    
    while(i<=count):
        
        l=f.readline()
        i=i+1
        l=l.split()
    

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=count+1
    
def prevrec():
    f=open("pydatabase.txt",'r')
    global count
    i=count
    
    while(i>0):
        
        l=f.readline()
        i=i-1
        l=l.split()
    

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=count-1
def firstrec():
    f=open("pydatabase.txt",'r')
    global count
    i=count
    l=f.readline()
    i=i-i
    l=l.split()
    

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=count-count
'''def lastrec():
    f=open("pydatabase.txt",'r')
    global count
    i=0
    l=f.readline()
    i=i+total
    l=l.split()
    

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=total'''
def delrec():
     f=open("pydatabase.txt",'a+')
     d=f.readlines()
     a=t1.get()
     b=t2.get()
     c=t3.get()
     x=t4.get()
     y=t5.get()
     
     
     if d==(a+b+c+x+y):
        f.write("")
        s1.set("")
        
     #f.truncate()
     f.close()
def search():
    f=open("pydatabase.txt",'r')
    global count
    i=0
    
    while(i<=count):
        
        l=f.readline()
        i=i+1
        l=l.split()
    c=t3.get()
    s3.find(c)

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=count+1
   
    
    
b1=Button(w,text="|<",command=firstrec)
b2=Button(w,text="<",command=prevrec)
b3=Button(w,text=">",command=nextrec)
b4=Button(w,text=">|")
b5=Button(w,text="ADD",command=addrec)
b6=Button(w,text="DELETE",command=delrec)
b7=Button(w,text="UPDATE")
b8=Button(w,text="SEARCH",command=search)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)

t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
t3.grid(row=3,column=2)
t4.grid(row=4,column=2)
t5.grid(row=5,column=2)

b1.grid(row=6,column=1,columnspan=2,padx=5,pady=5)
b2.grid(row=6,column=2,columnspan=2,padx=5,pady=5)
b3.grid(row=6,column=3)
b4.grid(row=6,column=5)
b5.grid(row=7,column=1,columnspan=2)
b6.grid(row=7,column=2,columnspan=2)
b7.grid(row=7,column=3,padx=5,pady=5)
b8.grid(row=7,column=5,padx=5,pady=5)


w.mainloop()
