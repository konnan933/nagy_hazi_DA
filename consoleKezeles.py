import pyconio  
import felhasznalok

def sendErrorMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.RED)
    print(text, end="")
    setOutputColor()
    print("")

def sendImportantMessage(text):
    pyconio.textcolor(pyconio.BLACK)
    pyconio.textbackground(pyconio.YELLOW)
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

def bejelntkezes_folyamat(fiokok):
    nevek = fiokok.log_in_nev_input()
    succesful_log_in = fiokok.log_in(nevek)
    while succesful_log_in == None: 
        succesful_log_in = fiokok.log_in(nevek)
    return succesful_log_in

def bejenkezes_or_add_felhasznalo(fiokok):
    valasz = input(f"Bejelentkezéshez  (adja meg az 1-est)\nÚj fiók lértehozásához (adja meg az 2-est)")
        
    while valasz != 1 and valasz != 2:
        sendErrorMessage("Rossz billenytyűzetet nyomott meg")
        valasz = input(f"Bejelentkezéshez  (adja meg az 1-est)\nÚj fiók lértehozásához (adja meg az 2-est)")

    if(valasz == "1"):
        return bejelntkezes_folyamat(fiokok)
    elif(valasz == "2"):
        fiokok.addFelhasznalo()
        return bejelntkezes_folyamat(fiokok)

    