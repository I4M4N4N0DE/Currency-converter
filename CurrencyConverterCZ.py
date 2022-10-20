import tkinter as tkin
    
def main(rate, money):
            
        cash = float(input("Zadejte částku: "))
        resum = cash * rate
        sresum = str(resum)
        print(sresum + money)

def Gui():
    
        buttonwin = tkin.Tk()
        name = buttonwin.title("SMĚNA")
        buttonwin.geometry("200x200")
    
        b1 = tkin.Button(buttonwin, text="CZK -> $", command=lambda:main(0.039804, " $")).place(x=10, y=20) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b2 = tkin.Button(buttonwin, text="$ --> CZK", command=lambda:main(24.512, " CZK")).place(x=110, y=20) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b3 = tkin.Button(buttonwin, text="CZK --> €", command=lambda:main(24.485, " €")).place(x=10, y=80) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b4 = tkin.Button(buttonwin, text="€ --> CZK", command=lambda:main(0.40841, " CZK")).place(x=110, y=80) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b5 = tkin.Button(buttonwin, text="$ --> €", command=lambda:main(1.008, " €")).place(x=18, y=130) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b6 = tkin.Button(buttonwin, text="€ --> $", command=lambda:main(0.99889, " $")).place(x=118, y=130) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        b7 = tkin.Button(buttonwin, text="Exit", command=buttonwin.destroy).place(x=75, y=165) # zde si můžete změnit aktuální měnový kurz pro daný převod (lambda:main(aktuální kurz v desetinném zápise))
        buttonwin.mainloop()
    
Gui()
