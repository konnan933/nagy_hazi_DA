import datetime
class Esemeny:
    def __init__(self, id, felhasznaloId, nev, datum, hely, megjegyzes):
        self.id = id
        self.felhasznaloId = felhasznaloId
        self.setNev(nev)
        self.setDatum(datum[0], datum[1], datum[2], datum[3], datum[4], datum[5])
        self.setHely(hely)
        self.setMegjegyzes(megjegyzes)



    def __str__(self):
        return f"ID: {self.getId} felhasznaló ID: {self.getFelhasznaloId}, nev: {self.getNev}, datum: {self.getDatum}, hely: {self.getHely}, megjegyzes: {self.getMegjegyzes}"
    
    def getFelhasznaloId(self):
        return self.felhasznaloId
    
    def getId(self):
        return self.id
    
    def getNev(self):
        return self.nev
    
    def getDatum(self):
        return self.datum.strftime("%X") +" "+ self.datum.strftime("%x")
    
    def getHely(self):
        return self.hely 
    
    def getMegjegyzes(self):
        return self.megjegyzes 
    
    def setNev(self, nev):
        self.nev = nev

    def setDatum(self, ev, honap, nap, ora = 0, perc = 0, mp = 0):
            self.datum = datetime.datetime(ev, honap, nap, ora, perc, mp)

    def setHely(self, hely):
        self.hely = hely

    def setMegjegyzes(self, megjegyzes):
        self.megjegyzes = megjegyzes

    def exportView(self):
        return  f"{self.getId};{self.getFelhasznaloId};{self.getNev};{self.getDatum};{self.getHely};{self.getMegjegyzes}\n"
