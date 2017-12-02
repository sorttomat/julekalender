
def lesInnFil(filename):
    infile = open(filename, "r")
    ordbok = infile.readlines()
    infile.close()
    return ordbok

def filTilListe(fil):
    listeMedOrd = []
    for elem in fil:
        o = elem.strip("\n")
        o = o.strip("-")
        o = o.lower()
        o = "".join(x for x in o if x.isalpha())
        listeMedOrd.append(o)
    return listeMedOrd

def sjekkLikhet(ord1, ord2):
    return ord1 == ord2

def sjekkSet(ord1, ord2):
    return set(ord1) == set(ord2)

def sjekkLen(ord1, lengde):
    return len(ord1) == lengde
    

def lagGram(ordet, gram):
    nyttOrd = []
    for i in range(0, len(ordet) - 4):
        nyttOrd.append(ordet[i:(i+gram)])
    return "".join(x for x in nyttOrd if x.isalpha())


if __name__ == '__main__':

    fasit = "aeteesasrsssstaesersrrsse"

    ordbok = lesInnFil("wordlist.txt")
    print(len(ordbok))
    listeMedOrd = filTilListe(ordbok)

    for elem in listeMedOrd:
        if sjekkLen(elem, 9) and sjekkSet(elem, fasit):
            nyttOrd = lagGram(elem, 5)
            nyttOrdSortert = "".join(sorted(nyttOrd))
            fasitSortert = "".join(sorted(fasit))
            print(elem)

            if sjekkLikhet(nyttOrdSortert, fasitSortert):
                print("JOHO!!!", elem, fasit)
    