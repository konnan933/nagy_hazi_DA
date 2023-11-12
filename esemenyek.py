import uuid
import esemeny
import consoleKezeles
from datetime import datetime
class Esemenyek:
    def __init__(self):
        self.esemeny_tomb = []
        self.esemenyek_import()

    def __str__(self):
        kiiratas= ""
        for esemeny in self.esemeny_tomb:
            kiiratas  += str(esemeny) + "\n"
        return kiiratas
    
    def idGeneration(self):
        new_id = uuid.uuid4()
        taken_id = True
        while(taken_id):
            if(new_id in [esemeny.getId() for esemeny in self.esemeny_tomb]):
                new_id = uuid.uuid4()
            else:
                taken_id = False
                    
        return new_id
    
    def addEsemeny(self, felhasznaloId):
        self.esemeny_tomb.append(esemeny.Esemeny(self.idGeneration(), felhasznaloId, self.inputNev(), self.inputDatum(), self.inputHely(), self.inputMegjegyzes()))

    def inputNev(self):
        nev = input("Kérem adja meg az esemény nevét:")
        while nev == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a név, adjon újjat!")
            nev = input("Kérem adja meg az esemény nevét:")
        return nev
    
    def inputHely(self):
        hely = input("Kérem adja meg az esemény helyét:")
        while hely == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a hely, adjon újjat!")
            hely = input("Kérem adja meg az esemény helyét:")
        return hely
    
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
                print("Hibás formátum! Kérlek, próbáld újra.")

    def esemenyek_export(self):
        file = open("esemenyek.txt", "w", encoding="utf-8") # file név be van égetve más nem lehet
        for esemeny in self.esemeny_tomb:
            file.write(esemeny.exportView())
        file.close()
  
    def esemenyek_import(self):
        adatok= []
        file = open("esemenyek.txt", "r", encoding="utf-8") # file név be van égetve más nem lehet
        sorok = file.readlines()
        for sor in sorok:
            stripped = sor.strip()
            splitted = stripped.split(";")
            adatok.append(esemeny.Esemeny(splitted[0], splitted[1], splitted[2], self.datum_string_to_datetime(splitted[3]), splitted[4], splitted[5] ))
        file.close()
        self.esemeny_tomb = adatok

    def datum_string_to_datetime(self, datum_string):
        return datetime.strptime(datum_string, "%Y-%m-%d %H:%M:%S")
