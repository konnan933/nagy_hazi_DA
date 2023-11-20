import datetime
import pyconio
import consoleKezeles
import esemeny
from felhasznalok import Felhasznalok
from esemenyek import Esemenyek

def main():
    consoleKezeles.setOutputColor()
    fiokok = Felhasznalok()
    osszes_esemeny = Esemenyek()
    valasz = "6" # 6 ös kijelentkezés és alap állapotból ezzel kezdjük eggyböl bejelentkezzenek
    bejelentkezett_fiok = consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)
    bejelentkezett_fiok != "9"
    if bejelentkezett_fiok != None:
        osszes_esemeny.getFelhasznalo_esemenyei(bejelentkezett_fiok.getId())
    while valasz != "9" and bejelentkezett_fiok != None:
        valasz = consoleKezeles.esemeny_konzol_valasztasok()
        consoleKezeles.esemeny_konzol_eldontes(valasz, osszes_esemeny, bejelentkezett_fiok.getId())
        if valasz == "6":
            bejelentkezett_fiok = consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)
            if bejelentkezett_fiok != None:
                osszes_esemeny.getFelhasznalo_esemenyei(bejelentkezett_fiok.getId())
        
    osszes_esemeny.esemenyek_export()
                

main()