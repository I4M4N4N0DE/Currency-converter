import tkinter as tk
from tkinter import *

class Main:
    
        def czktodollar():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 0.040796
            presum = str(resum)
            print("Your result is: " + presum + " $")
            Gui()
    
        def dollartoczk():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 24.512
            presum = str(resum)
            print("Your result is: " + presum + " CZK")
            Gui()
        
        def czktoeuro():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 24.485
            presum = str(resum)
            print("Your result is: " + presum + " €")
            Gui()
            
        def eurotoczk():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 0.40841
            presum = str(resum)
            print("Your result is: " + presum + " CZK")
            Gui()
        
        def dollartoeuro():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 1.008
            presum = str(resum)
            print("Your result is: " + presum + " €")
            Gui()
        
        def eurotodollar():
            
            cash = int(input("Insert your money: "))
            # This part of the code can be changed by you - simply rewrite the number shown after "resum = cash *" -  the function will change it's exchange rate
            resum = cash * 0.998898
            presum = str(resum)
            print("Your result is: " + presum + " $")
            
            Gui()
            
def Gui():
    
    buttonwin = tk.Tk()
    name = buttonwin.title("EXCHANGE")
    buttonwin.geometry("200x200")
    
    b1 = tk.Button(buttonwin, text="CZK -> $", command=Main.czktodollar).place(x=10, y=20)
    b2 = tk.Button(buttonwin, text="$ --> CZK", command=Main.dollartoczk).place(x=110, y=20)
    b3 = tk.Button(buttonwin, text="CZK --> €", command=Main.czktoeuro).place(x=10, y=80)
    b4 = tk.Button(buttonwin, text="€ --> CZK", command=Main.eurotoczk).place(x=110, y=80)
    b5 = tk.Button(buttonwin, text="$ --> €", command=Main.dollartoeuro).place(x=18, y=130)
    b6 = tk.Button(buttonwin, text="€ --> $", command=Main.eurotodollar).place(x=118, y=130)
    b7 = tk.Button(buttonwin, text="Exit", command=buttonwin.destroy).place(x=75, y=165)
    buttonwin.mainloop()
    
Gui()