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
    valasz = "5" # 5 ös kijelentkezés és alap állapotból ezzel kezdjük eggyböl bejelentkezzenek
    while valasz != "9":
        if valasz == "5":
            bejelentkezett_fiok = consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)
            osszes_esemeny.getFelhasznalo_esemenyei(bejelentkezett_fiok.getId())
        valasz = consoleKezeles.esemeny_konzol_valasztasok()
        consoleKezeles.esemeny_konzol_eldontes(valasz, osszes_esemeny, bejelentkezett_fiok.getId())
    osszes_esemeny.esemenyek_export()
                


    print(str(osszes_esemeny))
    



main()