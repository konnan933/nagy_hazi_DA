import pyconio  
import felhasznalok

def sendErrorMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.RED)
    print(text, end="")
    setOutputColor()
    print("")

def setOutputColor():
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.BLUE)

def sendConfirmMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.GREEN)
    print(text, end="")
    setOutputColor()
    print("")

def bejelntkezes_folyamat():
    setOutputColor()
    fiokok = felhasznalok.Felhasznalok()
    nevek = fiokok.log_in_nev_input()
    succesful_log_in = fiokok.log_in(nevek)
    while not succesful_log_in: 
        succesful_log_in = fiokok.log_in(nevek)
    return True