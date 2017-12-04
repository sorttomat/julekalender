class Grid():
    def __init__(self, gridSize):
        self._gridSize = gridSize
        self._grid = self._makeGrid()
        self._fotspor = self._makeFotspor()
        self._kalkulerGrid()
    

    def _makeGrid(self):
        grid = []
        for x in range(self._gridSize):
            row = []
            for y in range(self._gridSize):
                row.append(False)
            grid.append(row)
        return grid

    def _makeFotspor(self):
        fotspor = []
        for x in range(self._gridSize):
            row = []
            for y in range(self._gridSize):
                row.append(False)
            fotspor.append(row)
        return fotspor


    def _kalkuler(self, x, y):
        return ((x**3) + (12 * x * y) + (5 * x * (y**2)))


    def printGrid(self):
        for y in range(self._gridSize):
            for x in range(self._gridSize):
                if self._grid[x][y]:
                    print("#", end="")
                else:
                    print("-", end="")
            print()

    def _countOnes(self, number):
        binary = self._finnBitRepresentasjon(number)
        num = 0
        for elem in binary:
            if elem == "1":
                num += 1
        return num

    def _erPartall(self, num):
        return num % 2 == 0

    def _lukk(self, x, y):
        self._grid[x][y] = True
        
    def _kalkulerGrid(self):
        for x in range(self._gridSize):
            for y in range(self._gridSize):
                kalk = self._kalkuler(x+1, y+1)
                num = self._countOnes(kalk)
                if not self._erPartall(num):
                    self._lukk(x, y)



    def _finnBitRepresentasjon(self, tall):
        binary = ""
        while tall != 0:
            if tall % 2 == 0:
                binary += "0"
                tall = tall/2.0
            else:
                binary += "1"
                tall = int(tall/2.0)
        return binary[::-1]
        
    def _canGoUp(self, x, y):
        return  y - 1 >= 0 and (self._grid[x][y-1] == False)

    def _canGoDown(self, x, y):
        return y + 1 < self._gridSize and (self._grid[x][y+1] == False)

    def _canGoRight(self, x, y):
        return x + 1 < self._gridSize and (self._grid[x + 1][y] == False)

    def _canGoLeft(self, x, y):
        return x - 1 >= 0 and (self._grid[x - 1][y] == False)

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
            if self._fotspor[nyX][nyY] == False:
                self._gå(nyX, nyY)

        if self._canGoDown(x, y):
            nyX, nyY = self._downFrom(x, y)
            if self._fotspor[nyX][nyY] == False:
                self._gå(nyX, nyY)

        if self._canGoLeft(x, y):
            nyX, nyY = self._leftFrom(x, y)
            if self._fotspor[nyX][nyY] == False:
                self._gå(nyX, nyY)

        if self._canGoUp(x, y):
            nyX, nyY = self._upFrom(x, y)
            if self._fotspor[nyX][nyY] == False:
                self._gå(nyX, nyY)

    def startEventyr(self):
        x = 0
        y = 0
        self._gå(x, y)

    def printFotspor(self):
        for y in range(self._gridSize):
            for x in range(self._gridSize):
                if self._fotspor[x][y] == True:
                    print("$", end="")
                else:
                    print("-", end="")
            print()
        
    def printBegge(self):
        for y in range(self._gridSize):
            for x in range(self._gridSize):
                if self._fotspor[x][y] == True:
                    print("$", end="")
                elif self._grid[x][y] == True:
                    print("#", end="")
                else:
                    print("-", end="")
            print()
            
    def tellUbesøkt(self):
        antall = 0
        for y in range(self._gridSize):
            for x in range(self._gridSize):
                if self._fotspor[x][y] == True:
                    pass
                elif self._grid[x][y] == True:
                    pass
                else:
                    antall += 1
        return antall
        
