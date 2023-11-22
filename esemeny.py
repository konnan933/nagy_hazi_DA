class Esemeny:
    def __init__(self, id, felhasznaloId, nev, datum, hely, megjegyzes=""):
        self.id = id
        self.felhasznaloId = felhasznaloId
        self.setNev(nev)
        self.setDatum(datum)
        self.setHely(hely)
        self.setMegjegyzes(megjegyzes)



    def __str__(self):
        return f"ID: {self.getId()} felhasznaló ID: {self.getFelhasznaloId()}, név: {self.getNev()}, dátum: {self.getDatum()}, hely: {str(self.getHely())}, megjegyzés: {self.getMegjegyzes()}"
    
    def getFelhasznaloId(self):
        return self.felhasznaloId
    
    def getId(self):
        return self.id
    
    def getNev(self):
        return self.nev
    
    def getDatum(self):
        return str(self.datum)
    
    def getHely(self):
        return self.hely
    
    def getMegjegyzes(self):
        return self.megjegyzes 
    
    def setNev(self, nev):
        self.nev = nev

    def setDatum(self, datum):
        self.datum = datum

    def setHely(self, hely):
        self.hely = hely

    def setMegjegyzes(self, megjegyzes):
        self.megjegyzes = megjegyzes

    def exportView(self):
        return  f"{self.getId()};{self.getFelhasznaloId()};{self.getNev()};{self.getDatum()};{self.getHely().exportView()};{self.getMegjegyzes()}\n"
