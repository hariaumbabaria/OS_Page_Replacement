from tkinter import *
import os

def one():
    file1 = 'DiskScheduling.py'
    os.system(file1)
def two():
    file2 = 'PageReplacement.py'
    os.system(file2)
def three():
    # put your scheduling file in same folder and rename 'file3' below
    file3 = 'your scheduling file.py'
    os.system(file3)
def four():
    # put your concurrency file in same folder and rename 'file4' below
    file4 = 'your concurrency file.py'
    os.system(file4)


Menu = Tk()

Menu.title("Team No:21 OS PROJECT")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("800x700+0+0")
Menu.resizable(False, False)

L1=Label(width="900", height="2", text="OS Lab Project", font=("Century Gothic", 30), bg="black", fg="white")
L1.pack()
f1=Frame(bg="white").pack()
l1=Label(text="Choose Algorithm: ", font=("Century Gothic", 15))
l1.pack(pady="40")
Button1=Button(f1, text="Disk Scheduling Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=one).pack()
Button2=Button(f1, text="Page Replacement Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=two).pack(pady="30")
Button3=Button(f1, text="Scheduling Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=three).pack()
Button4=Button(f1, text="Concurrency & Deadlock Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=four).pack(pady="30")

Menu.mainloop()
