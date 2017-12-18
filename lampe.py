class Lampe():
    def __init__(self):
        self._tilstand = False #lampen er av
    
    def skruAv(self):
        self._tilstand = False
    
    def skruPå(self):
        self._tilstand = True
    
    def erPå(self):
        return self._tilstand