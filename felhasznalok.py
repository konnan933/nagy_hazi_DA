import felhasznalo
import hashlib
import uuid

class Felhasznalok:
    def __init__(self):
        self.felhasznalo_tomb = felhasznalok_import()

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
        nev = input("Adja meg kérem a nevét: ")
        jelszo = input("Adja meg kérem a jelszót: ")

        self.felhasznalo_tomb.append(felhasznalo(self.idGeneration() ,nev, jelszo))

    def felhasznalok_export(self):
        file = open("felhasznalok.txt", "w", encoding="utf-8") # file név be van égetve más nem lehet
        for felhasznalo in self.felhasznalo_tomb:
            file.write(felhasznalo.exportView())
        file.close()
  
    def felhasznalok_import():
        adatok= []
        file = open("felhasznalok.txt", "r", encoding="utf-8") # file név be van égetve más nem lehet
        sorok = file.readlines()
        for sor in sorok:
            stripped = sor.strip()
            splitted = stripped.split(";")
            adatok.append(felhasznalo(splitted[0], splitted[1], splitted[2]))
        file.close()
        return adatok
    
    def log_in(self):
        

        jelszo = input("Adja meg kérem a jelszót: ")
        
        for felhasznalo in eselyes_felhasznalok:
            if hashlib.md5(jelszo.encode()).hexdigest() == felhasznalo.getJelszo():
                return True
            else:
                pass
        
    def log_in_nev_input(self):
        nev = input("Adja meg kérem a felhasználó nevét: ")

        eselyes_felhasznalok = []

        for felhasznalo in self.felhasznalo_tomb:
            if felhasznalo.getNev() == nev:
                eselyes_felhasznalok.append(felhasznalo)

        if(len(eselyes_felhasznalok) == 0):
            return self.log_in_nev_input()
        
        return eselyes_felhasznalok



