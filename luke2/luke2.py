
def makeGrid(gridSize):
    grid = []
    for x in range(gridSize):
        row = []
        for y in range(gridSize):
            row.append(False)
        grid.append(row)
    return grid

def makeFotspor(gridSize):
    fotspor = []
    for x in range(gridSize):
        row = []
        for y in range(gridSize):
            row.append(False)
        fotspor.append(row)
    return fotspor


def kalkuler(x, y):
    return ((x**3) + (12 * x * y) + (5 * x * (y**2)))


def printGrid2(grid, gridSize):
    for y in range(gridSize):
        for x in range(gridSize):
            if grid[x][y]:
                print("#", end="")
            else:
                print("-", end="")
        print()

def countOnes(number):
    binary = finnBitRepresentasjon(number)
    num = 0
    for elem in binary:
        if elem == "1":
            num += 1
    return num

def erPartall(num):
    return num % 2 == 0

def lukk(x, y, grid):
    grid[x][y] = True
    
def kalkulerGrid(grid, gridSize):
    for x in range(gridSize):
        for y in range(gridSize):
            kalk = kalkuler(x+1, y+1)
            num = countOnes(kalk)
            if not erPartall(num):
                lukk(x, y, grid)



def finnBitRepresentasjon(tall):
    binary = ""
    while tall != 0:
        if tall % 2 == 0:
            binary += "0"
            tall = tall/2.0
        else:
            binary += "1"
            tall = int(tall/2.0)
    return binary[::-1]
    
def canGoUp(grid, x, y):
    return  y - 1 >= 0 and (grid[x][y-1] == False)

def canGoDown(grid, x, y):
    return y + 1 < len(grid) and (grid[x][y+1] == False)

def canGoRight(grid, x, y):
    return x + 1 < len(grid) and (grid[x + 1][y] == False)

def canGoLeft(grid, x, y):
    return x - 1 >= 0 and (grid[x - 1][y] == False)

def upFrom(x, y):
    return x, y-1
        
def downFrom(x, y):
    return x, y+1

def rightFrom(x, y):
    return x+1, y

def leftFrom(x, y):
    return x-1, y

def gå(grid, fotspor, x, y):
    fotspor[x][y] = True

    if canGoRight(grid, x, y):
        nyX, nyY = rightFrom(x, y)
        if fotspor[nyX][nyY] == False:
            gå(grid, fotspor, nyX, nyY)

    if canGoDown(grid, x, y):
        nyX, nyY = downFrom(x, y)
        if fotspor[nyX][nyY] == False:
            gå(grid, fotspor, nyX, nyY)

    if canGoLeft(grid, x, y):
        nyX, nyY = leftFrom(x, y)
        if fotspor[nyX][nyY] == False:
            gå(grid, fotspor, nyX, nyY)

    if canGoUp(grid, x, y):
        nyX, nyY = upFrom(x, y)
        if fotspor[nyX][nyY] == False:
            gå(grid, fotspor, nyX, nyY)

def startEventyr(grid, fotspor, gridSize):
    x = 0
    y = 0
    gå(grid, fotspor, x, y)

def printFotspor(fotspor, gridSize):
    for y in range(gridSize):
        for x in range(gridSize):
            if fotspor[x][y] == True:
                print("$", end="")
            else:
                print("-", end="")
        print()
    
def printBegge(labyrint, fotspor, gridSize):
    for y in range(gridSize):
        for x in range(gridSize):
            if fotspor[x][y] == True:
                print("$", end="")
            elif labyrint[x][y] == True:
                print("#", end="")
            else:
                print("-", end="")
        print()
        
def tellUbesøkt(labyrint, fotspor, gridSize):
    antall = 0
    for y in range(gridSize):
        for x in range(gridSize):
            if fotspor[x][y] == True:
                pass
            elif labyrint[x][y] == True:
                pass
            else:
                antall += 1
    return antall
    

gridSize = 10           


fotspor = makeFotspor(gridSize)          

labyrint = makeGrid(gridSize)

kalkulerGrid(labyrint, gridSize)

startEventyr(labyrint, fotspor, gridSize)

printGrid2(labyrint, gridSize)
print()
printFotspor(fotspor, gridSize)
print()
printBegge(labyrint, fotspor, gridSize)

print(tellUbesøkt(labyrint, fotspor, gridSize))
