import time


def regnKvadrat(tall):
    kvadrat = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    return kvadrat[tall]

def finnNesteTall(tall):
    nyttTall = 0
    siffere = str(tall)
    for i in range(len(siffere)):
        nyttTall += regnKvadrat(int(siffere[i]))
    return nyttTall

def sjekkJuletall(tall):
    listeSekvenser = []
    while tall not in listeSekvenser:
        listeSekvenser.append(tall)
        tall = finnNesteTall(tall)
    if 1 in listeSekvenser:    
        return True
    return False
        
def kjor(tak):
    sumJul = 0
    for i in range(tak + 1):
        if (sjekkJuletall(i)):
            sumJul += i
            print(i)
    return sumJul
   
tak = 10000000

start_time = time.clock()
sumJuletall= kjor(tak)
print (time.clock() - start_time, "seconds")

print(sumJuletall)



