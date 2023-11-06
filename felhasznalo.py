
import hashlib

class Felhasznalo:
    def __init__(self, id, nev, jelszo):
        self.id = id
        self.nev = nev
        self.jelszo = titkositas(jelszo)

    def __str__(self):
        return f"ID: {self.id} Név: {self.nev}, jelszó(titkósítva): {self.jelszo}"
    
    def getNev(self):
        return self.nev
    
    def getId(self):
        return self.id
    
    def getJelszo(self):
        return self.jelszo
    
    def setNev(self, nev):
        self.nev = nev

    def setJelszo(self, jelszo):
        self.jelszo = titkositas(jelszo)

    def exportView(self):
        return  f"{self.id};{self.nev};{self.jelszo}"

def titkositas(jelszo):
    return hashlib.md5(jelszo.encode()).hexdigest()