import felhasznalo
import uuid

class Felhasznalok:
    def __init__(self, felhasznalo_tomb):
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

    def felhasznalok_export():
        file = open("felhasznalok.txt", "w", encoding="utf-8")
        for sor in sorok:
            stripped = sor.strip()
            splitted = stripped.split(";")
            adatok.append(felhasznalo(splitted[0], splitted[1], splitted[2]))
        file.close()
  
    def felhasznalok_import():
        adatok= []
        file = open("felhasznalok.txt", "r", encoding="utf-8")
        sorok = file.readlines()
        for sor in sorok:
            stripped = sor.strip()
            splitted = stripped.split(";")
            adatok.append(felhasznalo(splitted[0], splitted[1], splitted[2]))
        file.close()
        return adatok

