from tkinter import *
from queue import Queue
import copy
import random
import matplotlib.pyplot as plt


def FIFO(pages, n, capacity, txt):

    s = set()
    indexes = Queue()
    page_faults = 0
    fault = []
    matrix = []
    for i in range(n):
        a = []
        if (len(s) < capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults += 1
                fault.append(True)
                indexes.put(pages[i])
            else:
                fault.append(False)
        else:
            if (pages[i] not in s):
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
                fault.append(True)
            else:
                fault.append(False)
        dummy = indexes
        while(dummy.empty()!=False):
            val1 = dummy.queue(0)
            dummy.get()
            a.append(val1)
            print(val1)
        while(len(a)<capacity):
            a.append(-1)
        a.reverse()
        matrix.append(a)

    anime(capacity, n, txt, pages, matrix, fault)

def anime(noFrame, N, txt, refString, matrix, fault_list):
    Visual = Tk()
    Visual.title("Visualisation Of Algorithms: "+txt)
    Visual.geometry("811x700+0+0")
    #Frame1 = Frame(Visual, bd="7")
    #Frame1.grid(row=0, column=0)
    # row1=0
    # col1=0

    for j in range(N):
        Label2 = Label(Visual, text=refString[j], font=("Century Gothic", 12), width="5")
        Label2.grid(row=0, column=j)
        for i in range(1, noFrame+1):
            if(matrix[j][i] != -1):
                Label2 = Label(Visual, text=matrix[j][i], font=("Century Gothic", 12), width="5", relief="groove")
                Label2.grid(row=i, column=j, padx=5, pady=2)
            else:
                Label2 = Label(Visual, text=" ", font=("Century Gothic", 12), width="5", relief="groove")
                Label2.grid(row=i, column=j, padx=5, pady=2)
                #col1 += 1
            #row1 += 1

    Visual.mainloop()

def Visualise(option,noFrame,refString):

    noF = (int)(noFrame)
    pageR = list(map(int, refString.split(" ")))
    N = len(pageR)

    txt = "0"
    if option == "FIFO":
        txt = "First In First Out"
        FIFO(pageR, N, noF, txt)

    elif option == "LIFO":
        txt = "Last In First Out"
    elif option == "LRU":
        txt = "Least Recently Used"
    elif option == "Optimal PRA":
        txt = "Optimal PRA"
    elif option == "Random PRA":
        txt = "Random PRA"

    # showRow(noF, N, txt, pageR)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Page
Menu = Tk()
Menu.title("Page Replacement Algorithm")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("811x700+0+0")
Menu.resizable(False, False)

L1 = Label(bg="black", text="Page Replacement Algorithm", fg="white", font=("Century Gothic", 30), width="900", height="2").pack()

F1 = Frame(bg="white").pack()

L2 = Label(F1, text="Choose Algorithm:", font=("Century Gothic", 18)).pack(pady="15")

variable = StringVar()
variable.set("FIFO") # default value
dropDown = OptionMenu(F1, variable, "FIFO", "LIFO", "LRU", "Optimal PRA", "Random PRA")
dropDown.configure(borderwidth="0", width="12", bg="#e8e8e8", fg="green", font=("Century Gothic", 12), activeforeground ="black", activebackground="#bbbfca")
dropDown.pack(pady="5")

L3 = Label(F1, text="Enter the no. of frames:", font=("Century Gothic", 18)).pack(pady="20")

# take input
noFrames = Entry(F1, width="15", bg="#e8e8e8", fg="green",font=("Century Gothic", 15), bd="0", justify="center")
noFrames.pack()

L4 = Label(F1, text="Enter Page Reference: ", font=("Century Gothic", 18)).pack(pady="30")

#take input
pageRef = Entry(F1, bg="#e8e8e8", fg="green",font=("Century Gothic", 15), bd="0", justify="center")
pageRef.pack()

L5 = Button(F1, borderwidth="0", text="Visualise", bg="#e8e8e8", fg="green", font=("Century Gothic", 18), activeforeground = "black", activebackground="#bbbfca", command=lambda: Visualise(variable.get(), noFrames.get(), pageRef.get())).pack(pady="30")

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green",font=("Century Gothic", 18), activeforeground = "black", activebackground="#bbbfca", command=lambda: graph(noF, pageR)).pack()
Menu.mainloop()