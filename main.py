import datetime
import pyconio
import consoleKezeles
import esemeny
import felhasznalok
import esemenyek

def main():
    felhasznalok_1 = felhasznalok.Felhasznalok()
    felhasznalok_1.addFelhasznalo()
    print(str(felhasznalok_1))
    #consoleKezeles.bejelntkezes_folyamat()

main()