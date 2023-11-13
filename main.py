import datetime
import pyconio
import consoleKezeles
import esemeny
import felhasznalok
import esemenyek

def main():
    consoleKezeles.setOutputColor()
    pyconio.rawmode()
    fiokok = felhasznalok.Felhasznalok()
    consoleKezeles.bejenkezes_or_add_felhasznalo(fiokok)


main()