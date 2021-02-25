from tkinter import *                          #Tkinter library
import random                                  #Used in Random Page Replacement Algorithm
import matplotlib.pyplot as plt                #Plotted graph using matplotlib

def Initialize():
    global root
    global row
    global col
    row = 0
    col = 1


def FIFO(pages, n, capacity, txt):
    Initialize()
    global col
    s = set()
    front = 0
    indexes = []
    page_faults = 0
    fault = []
    new_window(txt, capacity)

    for i in range(n):
        if (len(s) < capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults += 1
                fault.append(True)
                indexes.append(pages[i])
            else:
                fault.append(False)
        else:
            if (pages[i] not in s):
                s.remove(indexes[front])
                s.add(pages[i])
                indexes[front] = pages[i]
                page_faults += 1
                fault.append(True)
                front+=1
                if(front>capacity-1):
                    front=0
            else:
                fault.append(False)
        FaultRatio = float((page_faults) / n)
        dummy = indexes
        anime(capacity, pages[i], dummy, fault[i], FaultRatio, txt, n)
        col += 1
    root.mainloop()

def LRU(processList, n, capacity, txt):
    Initialize()
    global col
    s = []
    fault = []
    st = []
    pageFaults = 0
    new_window(txt, capacity)
    j = 0
    for i in processList:

        if i not in s:

            if (len(s) < capacity):
                s.append(i)
                st.append(len(s)-1)

            else:
                ind = st.pop(0)
                s[ind] = i
                st.append(ind)

            pageFaults += 1
            fault.append(True)
        else:
            fault.append(False)
            st.append(st.pop(st.index(s.index(i))))
        FaultRatio = float((pageFaults)/n)
        dummy = s
        anime(capacity, processList[j], dummy, fault[j], FaultRatio, txt, n)
        j+=1
        col += 1

def Optimal(processList, n, capacity, txt):
    Initialize()
    global col
    s = []
    fault = []
    pageFaults = 0
    new_window(txt, capacity)
    occurance = [None for i in range(capacity)]
    for i in range(n):
        if processList[i] not in s:
            if len(s) < capacity:
                s.append(processList[i])
            else:
                for x in range(len(s)):
                    if s[x] not in processList[i + 1:]:
                        s[x] = processList[i]
                        break
                    else:
                        occurance[x] = processList[i + 1:].index(s[x])
                else:
                    s[occurance.index(max(occurance))] = processList[i]
            pageFaults += 1
            fault.append(True)
        else:
            fault.append(False)
        FaultRatio = float((pageFaults)/n)
        dummy = s
        anime(capacity, processList[i], dummy, fault[i], FaultRatio, txt, n)
        col += 1


def new_window(txt, capacity):
    global root
    root = Tk()
    Basic_design(capacity)
    root.title("Visualisation Of Algorithms: " + txt)
    root.geometry("1366x654")


def empty_space():
    global root
    global row
    global col
    L = Label(root, text=" ", height="1", width="1")
    L.grid(row=row, column=col)
    row += 1

def build_EmptyLabel():
    global col
    global row
    MyLabel1= Label(root,text=" ",padx=15,pady=10)
    MyLabel1.grid(row=1,column=col+1)
    col+=1

def Basic_design(N):
    k=N

    RefStringLabel= Label(root,text="Reference String")
    RefStringLabel.configure(font=("Century Gothic", 15))
    RefStringLabel.grid(row=0,column=0,padx=20,pady=10)
    for i in range(N):
        mylabel= Label(root,text="Frame "+str(k),pady=10,padx=20,fg="black")
        mylabel.configure(font=("Century Gothic", 15))
        mylabel.grid(row=i+1,column=0)
        k-=1
    FaultStringLabel= Label(root,text="Page Faults")
    FaultStringLabel.configure(font=("Century Gothic", 15))
    FaultStringLabel.grid(row=N+1,column=0,padx=20,pady=10)

def cell(element):
    global root
    global row
    global col
    L = Label(root, text=element, padx=20,pady=10,bd=1,fg="green",relief=SOLID,anchor="center")
    L.configure(font=("Century Gothic", 12))
    L.grid(row=row, column=col)
    row += 1

def FrameRatio(FaultRatio, Frames, txt):
    lenCol = int(Frames / 2)
    frame1 = LabelFrame(root, text=" "+txt+" Page Fault Ratio ", pady=15, padx=10)
    frame1.configure(font=("Century Gothic", 11))
    frame1.grid(row=Frames + 4, column=lenCol, columnspan=int(Frames))
    HitRatio = 1 - FaultRatio
    myLabel4 = Label(frame1, text=" Hit Ratio:   =", fg="green", bd=1, padx=10, pady=15, relief=FLAT)
    myLabel4.configure(font=("Century Gothic", 10, 'bold'))
    myLabel4.grid(row=1, column=0)
    myLabel5 = Label(frame1, text="Miss Ratio: =", fg="red", bd=1, padx=10, pady=15, relief=FLAT)
    myLabel5.configure(font=("Century Gothic", 10, 'bold'))
    myLabel5.grid(row=2, column=0)
    e2 = Label(frame1, text=str(HitRatio), borderwidth=3)
    e2.grid(row=1, column=1)
    e3 = Label(frame1, text=str(FaultRatio), borderwidth=3)
    e3.grid(row=2, column=1)

def anime(Frames, Page, Q, faultOrHit, FaultRatio, txt, n):
    global root
    global row
    global col
    row = 0
    L = Label(root, text=Page, pady=10, fg="green")
    L.configure(font=("Century Gothic", 15))
    L.grid(row=row, column=col)
    row += 1
    ls = []
    ls = Q
    for i in range(Frames - len(ls)):
        empty_space()

    for i in reversed(ls):
        cell(i)

    build_EmptyLabel()

    if (faultOrHit == True):
        FaultOrHit1 = "Fault"
        L1 = Label(root, text=FaultOrHit1, fg="red")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=row, column=col - 1)
        row += 1
    else:
        FaultOrHit1 = "Hit"
        L1 = Label(root, text=FaultOrHit1, font="Questrial", fg="green")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=row, column=col - 1)
        row += 1
    FrameRatio(FaultRatio, n, txt)



def Visualise(option, noFrame, refString):
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
        LRU(pageR, N, noF, txt)

    elif option == "Optimal PRA":
        txt = "Optimal PRA"
        Optimal(pageR, N, noF, txt)

    elif option == "Random PRA":
        txt = "Random PRA"

    # showRow(noF, N, txt, pageR)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Page
Menu = Tk()
Menu.title("Page Replacement Algorithm")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("811x700+0+0")
Menu.resizable(False, False)

L1 = Label(bg="black", text="Page Replacement Algorithm", fg="white", font=("Century Gothic", 30), width="900",
           height="2").pack()

F1 = Frame(bg="white").pack()

L2 = Label(F1, text="Choose Algorithm:", font=("Century Gothic", 18)).pack(pady="15")

variable = StringVar()
variable.set("FIFO")  # default value
dropDown = OptionMenu(F1, variable, "FIFO", "LIFO", "LRU", "Optimal PRA", "Random PRA")
dropDown.configure(borderwidth="0", width="12", bg="#e8e8e8", fg="green", font=("Century Gothic", 12),
                   activeforeground="black", activebackground="#bbbfca")
dropDown.pack(pady="5")

L3 = Label(F1, text="Enter the no. of frames:", font=("Century Gothic", 18)).pack(pady="20")

# take input
noFrames = Entry(F1, width="15", bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
noFrames.pack()

L4 = Label(F1, text="Enter Page Reference: ", font=("Century Gothic", 18)).pack(pady="30")

# take input
pageRef = Entry(F1, bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
pageRef.pack()

L5 = Button(F1, borderwidth="0", text="Visualise", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca",
            command=lambda: Visualise(variable.get(), noFrames.get(), pageRef.get())).pack(pady="30")

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=lambda: graph(noF, pageR)).pack()
Menu.mainloop()
