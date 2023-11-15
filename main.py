import datetime
import pyconio
import consoleKezeles
import esemeny
import felhasznalok
import esemenyek

def main():
    consoleKezeles.setOutputColor()
    fiokok = felhasznalok.Felhasznalok()
    bejelentkezett_fiok = consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)


main()