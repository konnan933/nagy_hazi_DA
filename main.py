import datetime
import pyconio
import consoleKezeles
import esemeny
from felhasznalok import Felhasznalok
from esemenyek import Esemenyek

def main():
    consoleKezeles.setOutputColor()
    fiokok = Felhasznalok()
    bejelentkezett_fiok = consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)
    osszes_esemeny = Esemenyek()
    fiok_esemnyei = Esemenyek(osszes_esemeny.felhasznalo_esemenyei(bejelentkezett_fiok.getId()))
    valasz = consoleKezeles.esemeny_konzol_valasztasok()
    consoleKezeles.esemeny_konzol_eldontes(valasz, fiok_esemnyei)
    



main()