import tkinter as tk
from tkinter import *
    
def main(rate):
            
        cash = float(input("Insert your money: "))
        resum = cash * rate
        sresum = str(resum)
        print(sresum)

def Gui():
    
        buttonwin = tk.Tk()
        name = buttonwin.title("EXCHANGE")
        buttonwin.geometry("200x200")
    
        b1 = tk.Button(buttonwin, text="CZK -> $", command=lambda:main(0.039804)).place(x=10, y=20)
        b2 = tk.Button(buttonwin, text="$ --> CZK", command=lambda:main(24.512)).place(x=110, y=20)
        b3 = tk.Button(buttonwin, text="CZK --> €", command=lambda:main(24.485)).place(x=10, y=80)
        b4 = tk.Button(buttonwin, text="€ --> CZK", command=lambda:main(0.40841)).place(x=110, y=80)
        b5 = tk.Button(buttonwin, text="$ --> €", command=lambda:main(1.008)).place(x=18, y=130)
        b6 = tk.Button(buttonwin, text="€ --> $", command=lambda:main(0.998898)).place(x=118, y=130)
        b7 = tk.Button(buttonwin, text="Exit", command=buttonwin.destroy).place(x=75, y=165)
        buttonwin.mainloop()
    
Gui()
