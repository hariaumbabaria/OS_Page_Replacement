from tkinter import *
import random
import matplotlib.pyplot as plt

def Initialize(N):
    global Frame
    global index
    global L_End
    global L_Total_Faults       #LIFO algorithm Total Faults
    global F_Total_Faults       #FIFO algorithm Total Faults
    global R_Total_Faults       #Random page replacement algorithm Total Faults
    global LRU_Total_Faults     #LRU algorithm Total Faults
    global OPT_Total_Faults     #Optimal page replacement algorithm Total Faults
    global front
    global Fault
    global column
    global count
    global temp_array
    global temp_index
    front=0
    temp_array=[]
    temp_index= 0
    R_Total_Faults=0
    OPT_Total_Faults=0
    LRU_Total_Faults=0
    count=0
    column=0
    Frame=[None]*N
    L_End=N-1
    index=0
    F_Total_Faults=0
    L_Total_Faults=0
    Fault=False

def build_Label(frame,RefString):
    global column
    row_index= len(frame)
    row_index=row_index+1
    for i in frame:
        if i!= None:
            MyLabel= Label(root,text=i,padx=20,pady=10,bd=1,fg="green",bg="white",relief=SOLID,anchor="center")
            MyLabel.grid(row=row_index,column=column)
            row_index-=1

def build_EmptyLabel():
    global column
    MyLabel1= Label(root,text=" ",padx=20,pady=10,bg="white")
    MyLabel1.grid(row=1,column=column+1)
    column+=1

def Faults(fault,N):
    global column
    if(fault==False):
         flagLabel= Label(root,text="HIT",bg='white',fg='green',font=('RALEWAY 10 bold')).grid(row=N+3,column=column)
    else:
         flagLabel= Label(root,text="FAULT",bg='white',fg='red',font=('HELVETICA 10 bold')).grid(row=N+3,column=column)

def Print_RefString(number):
    global column
    RefString_Label = Label(root,text=number, bg='white', fg='green', font=('RALEWAY 10 bold')).grid(row=1,column=column,padx=20,pady=10)

def builtFaults(frame1,FaultRatio):
    HitRatio= 1-FaultRatio
    myLabel4=Label(frame1,text=" Hit Ratio:   =",fg="green",bg="white",bd=1,padx=10,pady=15,relief=FLAT,font="bold 10")
    myLabel4.grid(row=1,column=0)
    myLabel5=Label(frame1,text="Miss Ratio: =",fg="red",bg="white",bd=1,padx=10,pady=15,relief=FLAT,font="bold 10")
    myLabel5.grid(row=2,column=0)
    e2=Label(frame1,text=str(HitRatio),borderwidth=3, bg="white")
    e2.grid(row=1,column=1)
    e3=Label(frame1,text= str(FaultRatio),borderwidth=3, bg="white")
    e3.grid(row=2,column=1)

def Basic_design(N,RefString):
    k=N

    RefStringLabel= Label(root,text="Reference String", bg="white").grid(row=1,column=0,padx=20,pady=10)
    for i in range(N):
        mylabel= Label(root,text="Frame "+str(k),pady=10,padx=20,bg="white",fg="black").grid(row=i+2,column=0)
        k-=1
    FaultStringLabel= Label(root,text="Page Faults", bg="white").grid(row=N+3,column=0,padx=20,pady=10)

def getFrame(b,value):
    a=Frame
    b=b[count+1:]
    max_index=0
    max=0
    for i in a:
        if b.count(i)==0:
            b.append(i)
        if max < (b.index(i)):
            max=b.index(i)
            max_index=i
    temp=a.index(max_index)
    a[temp]=value
    return a

def FIFO(N,RefString,root):
    global Frame
    global index
    global front
    global F_Total_Faults
    global Fault
    global column
    global count
    i=0
    FaultRatio=0
    if count!=len(RefString):
        i=RefString[count]
        column+=1
        #IN CASE OF A HIT
        if None in Frame:
            if i not in Frame:
                Frame[index]=i
                index+=1
                Fault=True
                F_Total_Faults+=1
            else:
                Fault=False
        elif i in Frame:
            Fault=False
        #IN CASE OF A FAULT
        else:
            Fault=True
            F_Total_Faults+=1
            Frame[front]=i
            front+=1
            if(front>N-1):
                front=0
        count+=1
        if root!=None:
            build_Label(Frame,RefString)
            Print_RefString(i)
            Faults(Fault,N)
            build_EmptyLabel()
            root.after(1000,lambda: FIFO(N,RefString,root))
        else:
            FIFO(N,RefString,root)
    else:
        #Fault and hit ratio
        FaultRatio = float(F_Total_Faults/(len(RefString)))
        lenCol= int(len(RefString)/2)
        if root!=None:
            frame1=LabelFrame(root,text=" FIFO Page Fault Ratio ",fg="black",bg="white",padx=50,pady=60)
            frame1.grid(row=N+4,column= lenCol,columnspan=int(len(RefString)))
            builtFaults(frame1,FaultRatio)


def FirstInFirstOut(N1, RefString, txt):
    global root
    root = Tk()
    root.title('Visualization of Algorithm: '+txt)
    FIFONameLabel = Label(root, text="First In First Out Algorithm", bg="white").grid(row=0, column=0, padx=20, pady=10)
    root.geometry("1366x654")
    root.config(bg="white")
    N = int(N1)

    #initializing the variables
    Initialize(N)
    # Basic design layout
    Basic_design(N, RefString)
    # Algorithm implementation
    FIFO(N, RefString, root)
    root.mainloop()


def LIFO(N, RefString, root):
    global Frame
    global index
    global L_End
    global L_Total_Faults
    global Fault
    global column
    global count
    i = 0
    FaultRatio = 0
    if count != len(RefString):
        i = RefString[count]
        column += 1
        # IN CASE OF A HIT
        if None in Frame:
            if i not in Frame:
                Frame[index] = i
                index += 1
                Fault = True
                L_Total_Faults += 1
            else:
                Fault = False
        elif i in Frame:
            Fault = False
        # IN CASE OF A FAULT
        else:
            Fault = True
            L_Total_Faults += 1
            Frame[L_End] = i
        count += 1
        if root != None:
            build_Label(Frame, RefString)
            Print_RefString(i)
            Faults(Fault, N)
            build_EmptyLabel()

            root.after(1000, lambda: LIFO(N, RefString, root))
        else:
            LIFO(N, RefString, root)
    else:
        # Hit and Fault Ratio
        FaultRatio = float(L_Total_Faults / (len(RefString)))
        lenCol = int(len(RefString) / 2)
        if root != None:
            frame1 = LabelFrame(root, text=" LIFO Page Fault Ratio ", fg="black", bg="white", padx=50, pady=60)
            frame1.grid(row=N + 4, column=lenCol, columnspan=int(len(RefString)))
            builtFaults(frame1, FaultRatio)


def LastInFirstOut(N1, RefString, txt):
    global root
    root = Tk()
    root.title('Visualization of Algorithm: '+txt)
    LIFONameLabel = Label(root, text="Last In First Out Algorithm", bg="white").grid(row=0, column=0, padx=20, pady=10)
    root.geometry("1366x654")
    root.config(bg="white")
    N = int(N1)

    # Initializing the variables
    Initialize(N)
    # Basic design layout
    Basic_design(N, RefString)
    # Algorithm implementation
    LIFO(N, RefString, root)
    # FaultRatio()
    root.mainloop()


def LRU(N, RefString, root):
    global Frame
    global index
    global LRU_Total_Faults
    global Fault
    global column
    global count
    global temp_array  # a[]
    global temp_index  # 0
    i = 0
    FaultRatio = 0
    temp = 0
    if count != len(RefString):
        i = RefString[count]
        column += 1
        # IN CASE OF A HIT
        if None in Frame:
            if i not in Frame:
                Frame[index] = i
                index += 1
                Fault = True
                temp_array.append(i)
                LRU_Total_Faults += 1
            else:
                Fault = False
                temp_array.remove(i)
                temp_array.append(i)
        elif i in Frame:
            Fault = False
            temp_array.remove(i)
            temp_array.append(i)
        # IN CASE OF A FAULT
        else:
            Fault = True
            LRU_Total_Faults += 1
            temp = temp_array[temp_index]
            Frame_index = Frame.index(temp)
            Frame[Frame_index] = i
            temp_index += 1
            temp_array.append(i)

        count += 1
        if root != None:
            build_Label(Frame, RefString)
            Print_RefString(i)
            Faults(Fault, N)
            build_EmptyLabel()
            root.after(1000, lambda: LRU(N, RefString, root))

        else:
            LRU(N, RefString, root)
    else:
        # Hit and fault ratio
        FaultRatio = float(LRU_Total_Faults / (len(RefString)))
        lenCol = int(len(RefString) / 2)
        if root != None:
            frame1 = LabelFrame(root, text=" LIFO Page Fault Ratio ", fg="black", bg="white", padx=50, pady=60)
            frame1.grid(row=N + 4, column=lenCol, columnspan=int(len(RefString)))
            builtFaults(frame1, FaultRatio)

def LeastRecentlyUsed(N1, RefString, txt):
    global root
    root = Tk()
    root.title('Visualization of Algorithm: '+txt)
    LIFONameLabel = Label(root, text="Least Recently Used Out Algorithm", bg="white").grid(row=0, column=0, padx=20, pady=10)
    root.geometry("1366x654")
    root.config(bg="white")
    N = int(N1)

    # Initialize the variables
    Initialize(N)
    # Basic layout
    Basic_design(N, RefString)
    # Algorithm Implementation
    LRU(N, RefString, root)
    root.mainloop()


def Optimal_Algo(N, RefString, root):
    global Frame
    global index
    global L_End
    global OPT_Total_Faults
    global Fault
    global column
    global count
    global temp_array
    global temp_index
    i = 0
    FaultRatio = 0
    temp = 0
    if count != len(RefString):
        i = RefString[count]
        column += 1
        # IN CASE OF A HIT
        if None in Frame:
            if i not in Frame:
                Frame[index] = i
                index += 1
                Fault = True
                OPT_Total_Faults += 1
            else:
                Fault = False
        elif i in Frame:
            Fault = False
        # IN CASE OF A FAULT
        else:
            Fault = True
            OPT_Total_Faults += 1
            Frame = getFrame(RefString, i)  # Get the frame in case of a fault

        count += 1
        if root != None:
            build_Label(Frame, RefString)
            Print_RefString(i)
            Faults(Fault, N)
            build_EmptyLabel()
            root.after(1000, lambda: Optimal_Algo(N, RefString, root))
        else:
            Optimal_Algo(N, RefString, root)
    else:
        # Hit and fault ratio
        FaultRatio = float(OPT_Total_Faults / (len(RefString)))
        lenCol = int(len(RefString) / 2)
        if root != None:
            frame1 = LabelFrame(root, text=" Optimal Page Fault Ratio ", fg="black", bg="white", padx=50, pady=60)
            frame1.grid(row=N + 4, column=lenCol, columnspan=int(len(RefString)))
            builtFaults(frame1, FaultRatio)


def Optimal(N1, RefString, txt):
    global root
    root = Tk()
    root.title('Visualization of Algorithm: '+txt)
    LIFONameLabel = Label(root, text="Optimal Page Replacement Algorithm", bg="white").grid(row=0, column=0, padx=20, pady=10)
    root.geometry("1366x654")
    root.config(bg="white")
    N = int(N1)

    # initializing the variables
    Initialize(N)
    # Basic design layout
    Basic_design(N, RefString)
    # Algorithm implementation
    Optimal_Algo(N, RefString, root)
    root.mainloop()

def Random_Algo(N,RefString,root):
    global Frame
    global index
    global R_Total_Faults
    global Fault
    global column
    global count
    randomIndex= random.randint(0,N-1)
    i=0
    FaultRatio=0
    if count!=len(RefString):
        i=RefString[count]
        column+=1
        #IN CASE OF A HIT
        if None in Frame:
            if i not in Frame:
                Frame[index]=i
                index+=1
                Fault=True
                R_Total_Faults+=1
            else:
                Fault=False
        elif i in Frame:
            Fault=False
        #IN CASE OF A FAULT
        else:
            Fault=True
            R_Total_Faults+=1
            Frame[randomIndex]=i
        count+=1
        if root!=None:
            build_Label(Frame,RefString)
            Print_RefString(i)
            Faults(Fault,N)
            build_EmptyLabel()
            root.after(1000,lambda: Random_Algo(N,RefString,root))
        else:
            Random_Algo(N,RefString,root)
    else:
        #Hit and fault ratio
        FaultRatio = float(R_Total_Faults/(len(RefString)))
        lenCol= int(len(RefString)/2)
        if root!=None:
            frame1=LabelFrame(root,text=" Random Page Fault Ratio ",fg="black",bg="white",padx=50,pady=60)
            frame1.grid(row=N+4,column= lenCol,columnspan=int(len(RefString)))
            builtFaults(frame1,FaultRatio)


def Random(N1, RefString, txt):
    global root
    root = Tk()
    root.title('Visualization of Algorithm: '+txt)
    LIFONameLabel = Label(root, text="Random Page Replacement Algorithm", bg="white").grid(row=0, column=0, padx=20, pady=10)
    root.geometry("1366x654")
    root.config(bg="white")
    N = int(N1)

    # Initializing the variables
    Initialize(N)
    # Basic layout design
    Basic_design(N, RefString)
    # Algorithm implementation
    Random_Algo(N, RefString, root)
    root.mainloop()

def Visualise(option,noFrame,refString):

    noF = (int)(noFrame)
    pageR = list(map(int, refString.split(" ")))

    txt = "0"
    if option == "FIFO":
        txt = "First In First Out"
        FirstInFirstOut(noF, pageR, txt)

    elif option == "LIFO":
        txt = "Last In First Out"
        LastInFirstOut(noF, pageR, txt)

    elif option == "LRU":
        txt = "Least Recently Used"
        LeastRecentlyUsed(noF, pageR, txt)

    elif option == "Optimal PRA":
        txt = "Optimal PRA"
        Optimal(noF, pageR,txt)

    elif option == "Random PRA":
        txt = "Random PRA"
        Random(noF, pageR, txt)

def graph(refString, noF):
    plot_list=[]
    algos=["FIFO","LIFO","LRU","Optimal","Random"]
    dummy=0
    N = int(noF)
    pageR = list(refString.split(" "))

    Initialize(N)
    FIFO(N, pageR, None)
    dummy=F_Total_Faults/len(pageR)
    plot_list.append(dummy)

    Initialize(N)
    LIFO(N, pageR, None)
    dummy=L_Total_Faults/len(pageR)
    plot_list.append(dummy)

    Initialize(N)
    LRU(N, pageR, None)
    dummy=LRU_Total_Faults/len(pageR)
    plot_list.append(dummy)

    Initialize(N)
    Optimal_Algo(N, pageR, None)
    dummy=OPT_Total_Faults/len(pageR)
    plot_list.append(dummy)

    Initialize(N)
    Random_Algo(N, pageR, None)
    dummy=R_Total_Faults/len(pageR)
    plot_list.append(dummy)

    fig = plt.figure()
    plt.bar(algos, plot_list)
    plt.show()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Page
Menu = Tk()
Menu.title("Page Replacement Algorithm")
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

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green",font=("Century Gothic", 18), activeforeground = "black", activebackground="#bbbfca", command=lambda: graph(pageRef.get(), noFrames.get())).pack()
Menu.mainloop()