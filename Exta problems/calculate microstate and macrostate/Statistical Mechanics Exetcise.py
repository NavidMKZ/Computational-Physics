#Navid Markazi
from tkinter import *
from tkinter import ttk
import tkinter
import matplotlib.pyplot as plt
window = Tk()
window.title("Exercise Of Statistical Mechanics")
window.geometry('350x230')
lbl1 = Label(window,text="Number Of Particles A:")
lbl1.grid(column=0,row=0)
txt1 = Entry(window,width=10)
txt1.grid(column=1,row=0)
lbl2 = Label(window,text="Number Of Particles B:")
lbl2.grid(column=0,row=3)
txt2 = Entry(window,width=10)
txt2.grid(column=1,row=3)
lbl3 = Label(window,text="Total Energy:")
lbl3.grid(column=0,row=5)
txt3 = Entry(window,width=10)
txt3.grid(column=1,row=5)

lbl4 = Label(window,text="Note:It is best not to enter numbers\n\tgreater than 370,it will probably crash")
lbl4.grid(column=0,row=7)

def clicked():
    Num_A=int(txt1.get())
    Num_B=int(txt2.get())
    Total_energy=int(txt3.get())

    def factorial(n):
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
    list_Ω=list()
    list_ΩA=list()
    list_ΩB=list()
    list_qa=list()
    list_qb=list()
    for energy in range(0,Total_energy+1):
        list_qa.append(energy)
        list_qb.append(Total_energy-energy)
        A1=factorial(energy+Num_A-1)
        A2=factorial(energy)*factorial(Num_A-1)
        B1=factorial(Total_energy-energy+Num_B-1)
        B2=factorial(Total_energy-energy)*factorial(Num_B-1)
        list_ΩA.append(A1/A2)
        list_ΩB.append(B1/B2)
        list_Ω.append((B1/B2)*(A1/A2))
    inf=list()
    for i in range(0,Total_energy+1):
        inf.append((list_qa[i],list_ΩA[i],list_qb[i],list_ΩB[i],list_Ω[i]))

    def show():
        for i,(qa,ΩA,qb,ΩB,Ω_Total) in enumerate(inf, start=1):
            listBox.insert("","end",values=(qa,ΩA,qb,ΩB,Ω_Total))
    Microstates = tkinter.Tk() 
    label=tkinter.Label(Microstates,text="Macrostates",font=("Arial",30)).grid(row=0,columnspan=3)
    colums=('qa','ΩA','qb','ΩB','Ω_Total')
    listBox = ttk.Treeview(Microstates,columns=colums,show='headings')
    for col in colums:
        listBox.heading(col,text=col)    
    listBox.grid(row=1,column=0,columnspan=2)
    show_microstate=tkinter.Button(Microstates,text="Show Microstates", width=13, command=show).grid(row=4, column=0)
    closeButton=tkinter.Button(Microstates,text="Close",width=13,command=exit).grid(row=4, column=1)

    fig1,ax1=plt.subplots()
    height,y1=list_Ω,list_Ω
    rects1=ax1.bar(list_qa,height)
    ax1.plot(list_qa,y1,'--',color="red")
    ax1.set_xlabel('qa')
    ax1.set_ylabel('Ω_Total')
    ax1.set_title(r'Multiplicities_Units Of Energy')

    fig2,ax2=plt.subplots()
    height,y2=list_Ω,list_Ω
    rects2=ax2.bar(list_qb,height)
    ax2.plot(list_qb,y2,'--',color="red")
    ax2.set_xlabel('qb')
    ax2.set_ylabel('Ω_Total')
    ax2.set_title(r'Multiplicities_Units Of Energy')

    fig1.tight_layout()
    fig2.tight_layout() 
    plt.show()

btn=Button(window,text="Calculate",command=clicked)
btn.grid(column=0, row=6)
window.mainloop()