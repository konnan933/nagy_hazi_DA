import felhasznalo
import consoleKezeles
import hashlib
import uuid

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
        nev = input("Adja meg kérem a felhasználó nevét: ")
        jelszo = input("Adja meg kérem a jelszót: ")

        for felhasznalo in self.felhasznalo_tomb:
            if nev == felhasznalo.getfelhasznaloNev():
                self.felhasznalo_tomb.append(felhasznalo(self.idGeneration() ,nev, jelszo))
            else:
                consoleKezeles.sendErrorMessage("Ez a felhasználó név már foglalt, kérem adjon újjatt!")
                self.addFelhasznalo
        

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
    
    def log_in(self):
        for felhasznalo in self.log_in_nev_input():
            jelszo = input("Adja meg kérem a jelszót: ")
            print(hashlib.md5(jelszo.encode()).hexdigest())
            print(felhasznalo.getJelszo())
            if hashlib.md5(jelszo.encode()).hexdigest() == felhasznalo.getJelszo():
                consoleKezeles.sendConfirmMessage("Sikeres bejelentkezés")
                return True
            else:
                return False
        
    def log_in_nev_input(self):
        nev = input("Adja meg kérem a felhasználó nevét: ")

        eselyes_felhasznalok = []

        for felhasznalo in self.felhasznalo_tomb:
            if felhasznalo.getfelhasznaloNev() == nev:
                eselyes_felhasznalok.append(felhasznalo)

        if(len(eselyes_felhasznalok) == 0):
            consoleKezeles.sendErrorMessage("Hibás felhasználó név!")
            self.log_in_nev_input()
        
        return eselyes_felhasznalok
    
    


