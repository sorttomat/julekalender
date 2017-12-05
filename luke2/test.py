

class Labyrint():
    def __init__(self, size):
        self._size = size
        self._fotspor = self._initFotspor()
    

    def _initFotspor(self):
        fotspor = []
        for x in range(self._size):
            row = []
            for y in range(self._size):
                row.append(False)
            fotspor.append(row)
        return fotspor

    def _countOnes(self, number):
        binary = bin(number)
        num = 0
        for elem in binary:
            if elem == "1":
                num += 1
        return num
    

    def _isOpen(self, x, y):
        kalk = self._kalkuler(x+1, y+1)
        ones = self._countOnes(kalk)
        return self._erPartall(ones)
    
    def _sjekkFotspor(self, x, y):
        return self._fotspor[x][y]

    def _kalkuler(self, x, y):
        return ((x**3) + (12 * x * y) + (5 * x * (y**2)))

    def _erPartall(self, num):
        return num % 2 == 0

    def _canGoUp(self, x, y):
        return  y - 1 >= 0 and self._isOpen(x, y-1)

    def _canGoDown(self, x, y):
        return  y + 1 < self._size and self._isOpen(x, y+1)
        

    def _canGoRight(self, x, y):
        return  x + 1 < self._size and self._isOpen(x+1, y)


    def _canGoLeft(self, x, y):
        return  x - 1 >= 0 and self._isOpen(x-1, y)

    def _upFrom(self, x, y):
        return x, y-1
            
    def _downFrom(self, x, y):
        return x, y+1

    def _rightFrom(self, x, y):
        return x+1, y

    def _leftFrom(self, x, y):
        return x-1, y

    def _gå(self, x, y):
        self._fotspor[x][y] = True

        if self._canGoRight(x, y):
            nyX, nyY = self._rightFrom(x, y)
            if self._sjekkFotspor(nyX,nyY) == False:
                self._gå(nyX, nyY)

        if self._canGoDown(x, y):
            nyX, nyY = self._downFrom(x, y)
            if self._sjekkFotspor(nyX,nyY) == False:
                self._gå(nyX, nyY)

        if self._canGoLeft(x, y):
            nyX, nyY = self._leftFrom(x, y)
            if self._sjekkFotspor(nyX,nyY) == False:
                self._gå(nyX, nyY)

        if self._canGoUp(x, y):
            nyX, nyY = self._upFrom(x, y)
            if self._sjekkFotspor(nyX,nyY) == False:
                self._gå(nyX, nyY)
    
    def printLabyrint(self):
        for y in range(self._size):
            for x in range(self._size):
                if self._sjekkFotspor(x,y):
                    print("$", end="")

                elif self._isOpen(x, y):
                    print("-", end="")
                else:
                    print("#", end="")
            print()

    def startEventyr(self):
        x = 0
        y = 0
        self._gå(x, y)
    