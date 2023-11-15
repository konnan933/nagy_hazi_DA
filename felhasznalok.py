import felhasznalo
import consoleKezeles
import hashlib
import uuid
import re

class Felhasznalok:
    def __init__(self):
        self.felhasznalo_tomb = []
        self.felhasznalok_import()

    def __str__(self):
        kiiratas= ""
        for felhasznalo in self.felhasznalo_tomb:
            kiiratas  += str(felhasznalo) + "\n"
        return kiiratas
    
    def idGeneration(self):
        new_id = uuid.uuid4()
        taken_id = True
        while(taken_id):
            if(new_id in [felhasznalo.getId() for felhasznalo in self.felhasznalo_tomb]):
                new_id = uuid.uuid4()
            else:
                taken_id = False
                    
        return new_id
    
    def addFelhasznalo(self):
       
        self.felhasznalo_tomb.append(felhasznalo.Felhasznalo(self.idGeneration() ,self.inputNev(), self.inputJelszo()))
        consoleKezeles.sendConfirmMessage("Sikeresen létre hozta az új foikját!\nMost jelentkezzen be!")
        self.felhasznalok_export()
                

    def inputNev(self):
        nev = input("Kérem adja meg a felhasználó nevét:")
        while nev == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a név, adjon újjat!")
            nev = input("Kérem adja meg a felhasználó nevét:")
 
        nevek = [felhasznalo.getfelhasznaloNev() for felhasznalo in self.felhasznalo_tomb]
        
        while nev in nevek:
            consoleKezeles.sendErrorMessage("Ez a felhasználó név már foglalt, kérem adjon újjatt!")
            nev = input("Kérem adja meg a felhasználó nevét:")

        return nev
        
    def inputJelszo(self):
        consoleKezeles.sendImportantMessage("A jelszónak kell nagybetüt, számot tartalmaznia és legalább 8 karakter hosszúnak kell lenni!")
        jelszo = input("Kérem adja meg jelszavát:")
        while jelszo == "":
            consoleKezeles.sendErrorMessage("Nem lehet üres a jelszava, adjon újjat!")
            jelszo = input("Kérem adja meg jelszavát:")

        while None == re.fullmatch(r'^(?=.*[A-Z])(?=.*\d).{8,}$', jelszo):
            consoleKezeles.sendImportantMessage("A jelszónak kell nagybetüt, számot és legalább 8 karaktert hosszúnak kell lenni!")
            jelszo = input("Kérem adja meg jelszavát:")

        return jelszo


    def felhasznalok_export(self):
        file = open("felhasznalok.txt", "w", encoding="utf-8") # file név be van égetve más nem lehet
        for felhasznalo in self.felhasznalo_tomb:
            file.write(felhasznalo.exportView())
        file.close()
  
    def felhasznalok_import(self):
        adatok= []
        file = open("felhasznalok.txt", "r", encoding="utf-8") # file név be van égetve más nem lehet
        sorok = file.readlines()
        for sor in sorok:
            stripped = sor.strip()
            splitted = stripped.split(";")
            adatok.append(felhasznalo.Felhasznalo(splitted[0], splitted[1], splitted[2]))
        file.close()
        self.felhasznalo_tomb = adatok
    
    def log_in(self, felhasznalok):
        for felhasznalo in felhasznalok:
            jelszo = input("Adja meg kérem a jelszót: ")
            if hashlib.md5(jelszo.encode()).hexdigest() == felhasznalo.getJelszo():
                consoleKezeles.sendConfirmMessage("Sikeres bejelentkezés")
                return felhasznalo
            else:
                consoleKezeles.sendErrorMessage("Hibás jelszó!")
                return None
        
    def log_in_nev_input(self):
        nev = input("Adja meg kérem a felhasználó nevét: ")

        eselyes_felhasznalok = []

        for felhasznalo in self.felhasznalo_tomb:
            if felhasznalo.getfelhasznaloNev() == nev:
                eselyes_felhasznalok.append(felhasznalo)

        if(len(eselyes_felhasznalok) == 0):
            consoleKezeles.sendErrorMessage("Hibás felhasználó név!")
            eselyes_felhasznalok = self.log_in_nev_input()
        
        return eselyes_felhasznalok
    
    


