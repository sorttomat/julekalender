def regnKvadrat(tall):
    return tall ** 2

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
    return sumJul
   
tak = 10000000
sumJuletall= kjor(tak)

print(sumJuletall)



