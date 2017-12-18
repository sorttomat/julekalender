from lampe import Lampe

class Nisse():
    def __init__(self, nissenummer):
        self._nissenummer = nissenummer
        self._skruddPåLampen = False
 
    def hentNissenummer(self):
        return self._nissenummer

    def skruPåLampen(self, lampe):
        self._skruddPåLampen = True
        lampe.skruPå()
    
    def harSkruddPåLampen(self):
        return self._skruddPåLampen