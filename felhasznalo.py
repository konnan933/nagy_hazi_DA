
import hashlib

class Felhasznalo:
    def __init__(self, id, felhasznaloNev, jelszo):
        self.id = id
        self.felhasznaloNev = felhasznaloNev
        self.jelszo = "" 
        self.setJelszo(jelszo)

    def __str__(self):
        return f"ID: {self.id} Név: {self.felhasznaloNev}, jelszó(titkósítva): {self.jelszo}"
    
    def getfelhasznaloNev(self):
        return self.felhasznaloNev
    
    def getId(self):
        return self.id
    
    def getJelszo(self):
        return self.jelszo
    
    def setNev(self, felhasznaloNev):
        self.felhasznaloNev = felhasznaloNev

    def setJelszo(self, jelszo):

        if len(jelszo) == 32:
            self.jelszo = jelszo
        else:
            self.jelszo = titkositas(jelszo)

    def exportView(self):
        return  f"{self.id};{self.felhasznaloNev};{self.jelszo}\n"

def titkositas(jelszo):
    return hashlib.md5(jelszo.encode()).hexdigest()