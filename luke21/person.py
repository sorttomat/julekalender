class Person():
    def __init__(self, navn):
        self._navn = navn
        self._relasjonTilMeg = None
        self._alleredeTelt = False
        self._relasjoner = []
       
    
    def endreRelasjon(self, relasjon):
        self._relasjonTilMeg = relasjon
    
    def hentNavn(self):
        return self._navn

    def hentRelasjon(self):
        return self._relasjonTilMeg

    def hentRelasjoner(self):
        return self._relasjoner

    def erTelt(self):
        return self._alleredeTelt

    def tell(self):
        self._alleredeTelt = True
    
    def leggTilRelasjon(self, person, bol):
        self._relasjoner.append([(person.hentNavn()), person, bol])
    
    def erIRelasjoner(self, person):
        for relasjon in self._relasjoner:
            if person.hentNavn() == relasjon[0]:
                return True
        return False

    def sjekkRelasjoner(self):
        return [relasjon for relasjon in self._relasjoner if not relasjon[1].erTelt()]
