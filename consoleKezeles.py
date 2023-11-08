import pyconio  
import felhasznalok

def sendErrorMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.RED)
    print(text)
    setOutputColor()

def setOutputColor():
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.BLUE)

def sendConfirmMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.GREEN)
    print(text)
    setOutputColor()

def bejelntkezes_folyamat():
    setOutputColor()
    fiokok = felhasznalok.Felhasznalok()
    while not fiokok.log_in(): 
        fiokok.log_in()
    return True