import uuid
from esemeny import Esemeny
import consoleKezeles
from datetime import datetime
from hely import Hely
class Esemenyek:
    def __init__(self):
        self.osszes_esemeny = []
        self.fiok_esemenyei = []
        self.esemenyek_import()

    def __str__(self):
        kiiratas= ""
        for esemeny in self.osszes_esemeny:
            kiiratas  += str(esemeny) + "\n"
        return kiiratas
    
    def idGeneration(self):
        new_id = uuid.uuid4()
        taken_id = True
        while(taken_id):
            if(new_id in [esemeny.getId() for esemeny in self.osszes_esemeny]):
                new_id = uuid.uuid4()
            else:
                taken_id = False
                    
        return new_id
    
    def addEsemeny(self, felhasznaloId):
        id = self.idGeneration()
        nev = self.inputNev()
        datum = self.inputDatum()
        hely = self.inputHely()
        megjegyzes = self.inputMegjegyzes()
        self.osszes_esemeny.append(Esemeny(id, felhasznaloId, nev, datum, hely, megjegyzes))
        self.fiok_esemenyei.append(Esemeny(id, felhasznaloId, nev, datum, hely, megjegyzes))

    def deleteEsemeny(self, kivalasztott_index):
        keresendo = self.fiok_esemenyei[kivalasztott_index].getId()
        i = 0
        while i < len(self.osszes_esemeny) and not (self.osszes_esemeny[i].getId() == keresendo):
            i += 1
        index_osszes = i
        self.osszes_esemeny.pop(index_osszes)
        self.fiok_esemenyei.pop(kivalasztott_index) # azért nem keressük ennek az indexét mert show_by_index_fiok függvény ebböl keresi ki

    def inputNev(self):
        nev = input("Kérem adja meg az esemény nevét:")
        while nev == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a név, adjon újjat!")
            nev = input("Kérem adja meg az esemény nevét:")
        return nev
    
    def inputHely(self):
        return Hely(self.inputHelyISzam(), self.inputHelyVaros(), self.inputHelyUtca(), self.inputHelyHazSzam())

    def inputHelyVaros(self):
        varos = input("Kérem adja meg a város nevét:")
        while varos == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a város, adjon újjat!")
            varos = input("Kérem adja meg a város nevét:")
        return varos

    def inputHelyISzam(self):
        
        while True:
            try:
                iSzam = int(input("Kérem adja meg az irányító számot:"))
                while len(str(iSzam)) != 4:                    
                    consoleKezeles.sendErrorMessage("Az irányító szám 4db számbol áll.")
                    iSzam = int(input("Kérem adja meg az irányító számot:"))
                return iSzam
            except ValueError:
                consoleKezeles.sendErrorMessage("Nem lehet karakter az írányító számban.")
                continue
    
    def inputHelyUtca(self):
        utca = input("Kérem adja meg az utca nevét:")
        while utca == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres az utca neve, adjon újjat!")
            utca = input("Kérem adja meg az utca nevét:")
        return utca
    
    def inputHelyHazSzam(self):
        hazSzam = input("Kérem adja meg a ház számot:")
        while hazSzam == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a ház szám, adjon újjat!")
            hazSzam = input("Kérem adja meg a ház számot:")
        return hazSzam
    
    def inputMegjegyzes(self):
        megjegyzest = input("Kérem adja az eseményhez megjegyzést(nem kötelező):")
        return megjegyzest
        

    def inputDatum(self):
        while True:
            datum = input("Kérem adja meg az esemény dátumát(ÉÉÉÉ-HH-NN ÓÓ:PP:MP formátummal): ")
            try:
            # Dátum ellenőrzése és formátumra alakítása
                datum = self.datum_string_to_datetime(datum)
                return datum
            except ValueError:
                consoleKezeles.sendErrorMessage("Hibás formátum! Kérlek, próbáld újra.")

    def esemenyek_export(self):
        file = open("esemenyek.txt", "w", encoding="utf-8") # file név be van égetve más nem lehet
        for esemeny in self.osszes_esemeny:
            file.write(esemeny.exportView())
        file.close()

    def fiok_esemenyek_export(self, fajl_nev):
        file = open(fajl_nev+".txt", "w", encoding="utf-8") # file név be van égetve más nem lehet
        for esemeny in self.fiok_esemenyei:
            file.write(esemeny.exportView())
        file.close()
  
    def esemenyek_import(self):
        if(len(self.osszes_esemeny) == 0):
            adatok= []
            file = open("esemenyek.txt", "r", encoding="utf-8") # file név be van égetve más nem lehet
            sorok = file.readlines()
            for sor in sorok:
                stripped = sor.strip()
                splitted = stripped.split(";")
                hely = Hely(splitted[4], splitted[5], splitted[6], splitted[7])
                adatok.append(Esemeny(splitted[0], splitted[1], splitted[2], self.datum_string_to_datetime(splitted[3]), hely, splitted[8] ))
            file.close()
            self.osszes_esemeny = adatok
    def datum_string_to_datetime(self, datum_string):
        return datetime.strptime(datum_string, "%Y-%m-%d %H:%M:%S")
    
    def sort_by_datum(self):
        return sorted(self.fiok_esemenyei, key=lambda r: r.datum)
    
    def getFelhasznalo_esemenyei(self, fiok_id):
        for esemeny in self.osszes_esemeny:
            if esemeny.getFelhasznaloId() == fiok_id:
                self.fiok_esemenyei.append(esemeny)

    def show_by_index_fiok(self):
        for i in range(0, len(self.fiok_esemenyei)):
            print(f"{i+1}. {str(self.fiok_esemenyei[i])}")

        while True:
            try:
                valasztott_index = int(input("Irja be az esemény elött lévő számot: "))

                while not valasztott_index in range(1,len(self.fiok_esemenyei)+1):
                    consoleKezeles.sendErrorMessage("Rossz számot adott meg")
                    valasztott_index = int(input("Irja be az esemény elött lévő számot: "))
                    consoleKezeles.line_separator()
                return valasztott_index-1 

            except ValueError:
                consoleKezeles.sendErrorMessage("Nem számot adott meg")
                continue


    def search_by_nev_fiok(self):
        nev = input("Adja meg milyen név alapján keressünk!")

        while nev == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a hely, adjon újjat!")
            nev = input("Adja meg milyen név alapján keressünk!")

        consoleKezeles.sendImportantMessage(f"A(Z) {nev} név alapján talált események:")
        nev_talalatok = ""
        for esemeny in self.fiok_esemenyei:
            if nev.lower() in esemeny.getNev().lower():
                nev_talalatok += str(esemeny)+"\n"
        return nev_talalatok if len(nev_talalatok) != 0 else "Nincs ilyen nevü esemény"
    
    def search_by_week_fiok(self, ev, het_szam):
        ez_ev_esemenyek = []
        for esemeny in self.fiok_esemenyei:
            if esemeny.datum.isocalendar()[1] == het_szam and ev == esemeny.datum.year:
                ez_ev_esemenyek.append(esemeny)

        return ez_ev_esemenyek
    
    def search_by_month_fiok(self, ev, honap_szam):
        ez_ev_esemenyek = []
        for esemeny in self.fiok_esemenyei:
            if esemeny.datum.month == honap_szam and ev == esemeny.datum.year:
                ez_ev_esemenyek.append(esemeny)

        return ez_ev_esemenyek
    
    def search_by_day_fiok(self, ev, honap_szam, nap):
        ez_ev_esemenyek = []
        for esemeny in self.fiok_esemenyei:
            if esemeny.datum.month == honap_szam and ev == esemeny.datum.year and esemeny.datum.day == nap:
                ez_ev_esemenyek.append(esemeny)

        return ez_ev_esemenyek

