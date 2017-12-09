kryptertFasit = "OTUJNMQTYOQOVVNEOXQVAOXJEYA"

alfa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

røtter = []
for bokstav in alfa:
    røtter.append(ord(bokstav) + alfa.index(bokstav))

nyAlfa = []
for a, r in zip(alfa, røtter):
    index = alfa.index(a)
    nyIndex = index + r + 1
    while nyIndex >= len(alfa):
        nyIndex -= len(alfa)
    else:
        nyAlfa.append(alfa[nyIndex])
        
        
nyttOrd = []
for fasit, gammel, ny in zip(kryptertFasit, alfa, nyAlfa):
    indexNy = nyAlfa.index(fasit)
    nyttOrd.append(alfa[indexNy])

nyttOrd = "".join(nyttOrd)

print(nyttOrd)

        
        


        