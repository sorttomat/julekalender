from nisse import Nisse
from lampe import Lampe


def main():
    with open("prisoners.txt", "r") as infile:
        rekkefølge = [int(line.strip("\n")) for line in infile]

    nisser = [Nisse(x + 1) for x in range(100)]
    teller = 0
    antallGangerSkruddAv = 0
    lampe = Lampe()

    for nissenummer in rekkefølge:
        teller += 1
        nisse = nisser[nissenummer-1]
        if nissenummer == 1:
            if lampe.erPå():
                lampe.skruAv()
                antallGangerSkruddAv += 1
                if antallGangerSkruddAv == 99:
                    break
            continue

        elif not nisse.harSkruddPåLampen() and not lampe.erPå():
            nisse.skruPåLampen(lampe)

    print(teller)

main()

        

    

