import pyconio  
from esemenyek import Esemenyek 

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

    while valasz != "1" and valasz != "2":
        sendErrorMessage("Rossz számot adott meg")
        valasz = input(f"Bejelentkezéshez  (adja meg az 1-est)\nÚj fiók lértehozásához (adja meg az 2-est)")

    if(valasz == "1"):
        return bejelntkezes_folyamat(fiokok)
    elif(valasz == "2"):
        fiokok.addFelhasznalo()
        return bejelntkezes_folyamat(fiokok)


def fiok_esmenyei(fiok_id):
    esemenyek = Esemenyek(fiok_id)
    if(len(esemenyek.esemeny_tomb) == 0):
        sendImportantMessage("Még nincsen eseményed csinálj újjat!")
        esemenyek.addEsemeny(fiok_id)
    return esemenyek    

def esemeny_konzol_valasztasok():
    input_lista = ["1", "2", "3", "4", "5", "9"]
    valasz = input("Eseményeim megnézése (adja meg az 1-est)\n"+
                   "Új esemény hozzá adása (adja meg az 2-est)\n"+
                   "Esemény szerkeztése (adja meg az 3-est)"+
                   "Esemény törlése (adja meg az 4-est)\n"+
                   "Kijelentkezés (adja meg az 5-est)\n"+
                   "Kilépés (adja meg az 9-est)")
    while valasz not in input_lista:
        sendErrorMessage("Rossz számot adott meg")
        valasz = input("Eseményeim megnézése (adja meg az 1-est)\n"+
                   "Új esemény hozzá adása (adja meg az 2-est)\n"+
                   "Esemény szerkeztése (adja meg az 3-est)\n"+
                   "Esemény törlése (adja meg az 4-est)\n"+
                   "Kijelentkezés (adja meg az 5-est)\n"+
                   "Kilépés (adja meg az 9-est)")
    return valasz

def esemeny_konzol_eldontes(valasz,esemenyek):
    if(valasz == "1"):
        esemeny_megjelenites_valasztasok(esemenyek)
    elif(valasz == "2"):
        esemenyek.addEsemeny()
    elif(valasz == "3"):
        pass
    elif(valasz == "4"):
        esemenyek.deleteEsemeny(esemenyek.show_by_index_fiok())
    elif(valasz == "5"):
        pass
    elif(valasz == "9"): 
        pass

def esemeny_megjelenites_valasztasok(esemenyek):
    valasz = input(f"Idő szerinti sorrendben megnézni (adja meg az 1-est)\nFelvett sorrendben megnézni (adja meg az 2-est)\nNév alapján keresés (adja meg az 3-est)")

    while valasz != "1" and valasz != "2" and valasz != "3":
        sendErrorMessage("Rossz számot adott meg")
        valasz = input(f"Bejelentkezéshez  (adja meg az 1-est)\nÚj fiók lértehozásához (adja meg az 2-est)")

    if(valasz == "1"):
        for esemeny in esemenyek.sort_by_datum():
            print(str(esemeny))
    elif(valasz == "2"):
        for esemeny in esemenyek.fiok_esemenyei:
            print(str(esemeny))
    elif(valasz == "3"):
        print(esemenyek.seach_by_nev_fiok())