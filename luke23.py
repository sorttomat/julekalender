def delOppRunde(runde):
    """
    Deler opp runden i hver person sine trekk.
    """
    personX = [runde[x] for x in range(0, len(runde), 2)]
    personO = [runde[x] for x in range(1, len(runde), 2)]
    return personX, personO

def sjekkTallISekvens(listeTall, listeSekvens):
    """
    Sjekker at alle tall i sekvensen finnes i listen med tall.
    """
    for tall in listeSekvens:
        if tall not in listeTall:
            return False
    return True

def sjekkVinnerRunde(listeTall, vinnendeSekvenser):
    """
    Sjekker om alle tallene i én av vinnersekvensene er i listen med tall.
    """
    for sekvens in vinnendeSekvenser:
        if sjekkTallISekvens(listeTall, sekvens) == True:
            return True
    return False

def delSpillOppIRunder(trekk, vinnendeSekvenser):
    """
    Deler opp trekkene i runder.
    """
    runder = []
    i = 0
    runde = []
    while i < len(trekk):
        runde.append(trekk[i])
        personX, personO = delOppRunde(runde)
        if len(runde) >= 3 and (sjekkVinnerRunde(personX, vinnendeSekvenser) or sjekkVinnerRunde(personO, vinnendeSekvenser)):
            runder.append(runde)
            runde = []
        if len(runde) == 9:
            runder.append(runde)  
            runde = []
        i += 1
    return runder

def regnUtVinner(runder, vinnendeSekvenser):
    """
    Sjekker hver runde for vinner eller uavgjort. Summerer antall runder vunnet per person.
    Returnerer antall runder vinneren av spillet vant.
    """
    x = False #False = Xena, True = Ophelia
    antallXenaVinner = 0
    antallOpheliaVinner = 0
    uavgjort = 0
    for runde in runder:
        personX, personO = delOppRunde(runde)
        if sjekkVinnerRunde(personX, vinnendeSekvenser):
            if not x:
                antallXenaVinner += 1   
            else:
                antallOpheliaVinner += 1
            x = not x
            uavgjort = 0    
        elif sjekkVinnerRunde(personO, vinnendeSekvenser):
            if not x:
                antallOpheliaVinner += 1
            else:
                antallXenaVinner += 1  
            uavgjort = 0 
        else:
            uavgjort += 1
            if uavgjort == 3:
                x = not x
                uavgjort = 0
    return max([antallXenaVinner, antallOpheliaVinner])


if __name__ == "__main__":  
    trekk = []

    infile = open("moves.txt")
    for line in infile:
        line = line.strip()
        for elem in line:
            trekk.append(int(elem))
    infile.close()

    vinnendeSekvenser = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


    runder = delSpillOppIRunder(trekk, vinnendeSekvenser)
    vinner = regnUtVinner(runder, vinnendeSekvenser)            
    print(vinner)
                
                
                
                


