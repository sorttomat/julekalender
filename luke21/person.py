class Person():
    def __init__(self, navn):
        self._navn = navn
        self._relasjonTilMeg = None
        self._alleredeTelt = False
        self._relasjoner = []
       
    
    def settRelasjonTilMeg(self, relasjon):
        self._relasjonTilMeg = relasjon
    
    def hentNavn(self):
        return self._navn

    def hentRelasjonTilMeg(self):
        return self._relasjonTilMeg

    def hentRelasjoner(self):
        return self._relasjoner

    def erTelt(self):
        return self._alleredeTelt

    def tell(self):
        self._alleredeTelt = True
    
    def leggTilRelasjon(self, person, bol):
        self._relasjoner.append([person, bol])
    
    def erIRelasjoner(self, person):
        for relasjon in self._relasjoner:
            if person.hentNavn() == relasjon[0].hentNavn():
                return True
        return False

    def relasjonerSomIkkeErTelt(self):
        return [relasjon for relasjon in self._relasjoner if not relasjon[0].erTelt()]
