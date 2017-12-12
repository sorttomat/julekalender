def finnSammensetninger(tak):
    verdi = 0
    for i in range(2, tak + 1):
        ver = summerStartStopp(i)
        verdi += ver
        print(ver, i)
    return verdi

def summerStartStopp(stopp):
    sm = 0
    i = 0
    antall = 0
    start = 0
    while start < stopp//2 + 3:
        sm += i
        i += 1
        if sm > stopp:
            sm = 0
            start += 1
            i = int(start)
        if sm == stopp:
            antall += 1
            start += 1
            i = int(start)
            

    return antall



            
            

print(finnSammensetninger(130000))