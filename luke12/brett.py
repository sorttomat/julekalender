from rute import Rute

class Brett():
    def __init__(self, gridSize):
        self._gridSize = gridSize
        self._brett = []

        for x in range(self._gridSize):
            rad = []
            for y in range(self._gridSize):
                rad.append(Rute(x, y))
            self._brett.append(rad)
    
    def printBrett(self):
        for y in range(len(self._brett)):
            for x in range(len(self._brett)):
                farge = self._brett[x][y].hentFarge()
                if farge == True:
                    print("O", end=" ")
                else:
                    print("#", end=" ")
            print()

    def _erInnenforGrid(self, x, y):
        if 0 <= x < self._gridSize and 0 <= y < self._gridSize:
            return True
        return False

    def _finnMulige(self, x, y):
        mulige = []
        trekk = [[x-2, y-1], [x-2, y+1], [x-1, y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x+2, y-1], [x+2, y+1] ]

        for elem in trekk:
            if self.erInnenforGrid(elem[0], elem[1]):
                mulige.append(self._brett[elem[0]][elem[1]])
        return mulige
    
    def tellSorte(self):
        teller = 0
        for xRad in self._brett:
            for rute in xRad:
                if rute.hentFarge() == False:
                    teller += 1
        return teller

    def spill(self, antallFlytt):
        x = 0
        y = 0
        trekk = 0
        while trekk < antallFlytt:
            mulige = self.finnMulige(x, y)
            for destinasjon in mulige:
                if destinasjon.hentFarge() == self._brett[x][y].hentFarge():
                    self._brett[x][y].endreFarge()
                    x = destinasjon.hentX()
                    y = destinasjon.hentY()
                    break
            else:
                self._brett[x][y].endreFarge()
                x = mulige[-1].hentX()
                y = mulige[-1].hentY()
            
            trekk += 1            



def main():
        
    brett = Brett(10)

    brett.spill(200)

    print(brett.tellSorte())

main()


