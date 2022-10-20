import tkinter as tkin
    
def main(rate, money):
            
        cash = float(input("Insert your money: "))
        resum = cash * rate
        sresum = str(resum)
        print(sresum + money)

def Gui():
    
        buttonwin = tkin.Tk()
        name = buttonwin.title("EXCHANGE")
        buttonwin.geometry("200x200")
    
        b1 = tkin.Button(buttonwin, text="CZK -> $", command=lambda:main(0.039804, " $")).place(x=10, y=20) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b2 = tkin.Button(buttonwin, text="$ --> CZK", command=lambda:main(24.512, " CZK")).place(x=110, y=20) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b3 = tkin.Button(buttonwin, text="CZK --> €", command=lambda:main(24.485, " €")).place(x=10, y=80) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b4 = tkin.Button(buttonwin, text="€ --> CZK", command=lambda:main(0.40841, " CZK")).place(x=110, y=80) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b5 = tkin.Button(buttonwin, text="$ --> €", command=lambda:main(1.008, " €")).place(x=18, y=130) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b6 = tkin.Button(buttonwin, text="€ --> $", command=lambda:main(0.998898, " $")).place(x=118, y=130) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
        b7 = tkin.Button(buttonwin, text="Exit", command=buttonwin.destroy).place(x=75, y=165) # here you can change the actual exchange rate for this current exchange (lambda:main(current_rate))
    
Gui()
