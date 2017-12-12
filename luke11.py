

def erPrimtall(tall):
    for i in range(2, tall):
        if tall % i == 0:
            return False
    return True


def sjekkPalindrom(tall):
    strTall = str(tall)
    if strTall == strTall[::-1]:
        return True
    return False

def baklengs(tall):]
    return int(str(tall)[::-1])


def kjor(tak):
    teller = 0
    mirptall = []
    for i in range(10, tak):
        if erPrimtall(i) and erPrimtall(baklengs(i)) and not sjekkPalindrom(i):
            if i not in mirptall and baklengs(i) not in mirptall:
                mirptall.append(i)
                mirptall.append(baklengs(i))
                teller += 2
    return teller, mirptall


teller, mirptall = kjor(1000)
print(teller)

tall = 13
