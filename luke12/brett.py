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
                print(self._brett[x][y]._verdi, end=" ")
            print()


brett = Brett(10)

brett.printBrett()
                
