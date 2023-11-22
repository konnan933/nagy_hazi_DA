
class Hely:
    def __init__(self, iranyitoSzam = "", varos = "", utca = "" , hazSzam = ""):
        self.setIranyitoSzam(iranyitoSzam)
        self.setVaros(varos)
        self.setUtca(utca)
        self.setHazSzam(hazSzam)

    def __str__(self):
        return f"{self.getIranyitoSzam()} {self.getVaros()} {self.getUtca()} {self.getHazSzam()}"
    
    def getIranyitoSzam(self):
        return self.iranyitoSzam
    
    def getVaros(self):
        return self.varos
    
    def getUtca(self):
        return self.utca    
    
    def getHazSzam(self):
        return self.hazSzam
    
    def setIranyitoSzam(self, iranyitoSzam):
        self.iranyitoSzam = iranyitoSzam

    def setVaros(self, varos):
        self.varos = varos
        
    def setUtca(self, utca):
        self.utca = utca

    def setHazSzam(self, hazSzam):
        self.hazSzam = hazSzam


    def exportView(self):
        return  f"{self.iranyitoSzam};{self.varos};{self.utca};{self.hazSzam}"

