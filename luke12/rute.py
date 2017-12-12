class Rute():
    def __init__(self, xVerdi, yVerdi):
        self._xVerdi = xVerdi
        self._yVerdi = yVerdi
        self._verdi = self._xVerdi*10 + self._yVerdi
        self._farge = True #Hvit
    
    def hentVerdi(self):
        return self._verdi

    def hentFarge(self):
        return self._farge #False = svart, True = hvit

    