from person import Person

class Tre():
    def __init__(self, filnavn):
        self._filnavn = filnavn
        self._personer = []
        self._antallVenner = 1
        self._antallFiender = 0
        self._navn = []
        self.leggTilAllePersoner()
        self.leggTilAlleRelasjoner()

    def hentAllePersoner(self):
        return self._personer

    def printMineRelasjoner(self):
        nøytrale = self.finnAntallNøytrale()
        print("Venner: {}\nFiender: {}\nNøytrale: {}\n".format(self._antallVenner, self._antallFiender, nøytrale))

    def leggTilAllePersoner(self):
        with open(self._filnavn, "r") as infile:
            for line in infile:
                relasjon, person1, person2 = line.split()
                if person1 not in self._navn:
                    self._personer.append(Person(person1))
                    self._navn.append(person1)
                if person2 not in self._navn:
                    self._personer.append(Person(person2))
                    self._navn.append(person2)
        print("lagt til alle personer!")
        infile.close()
    
    def leggTilAlleRelasjoner(self):
        infile = open(self._filnavn)
        lines = infile.readlines()
        for person in self._personer:
            for line in lines:
                relasjon, person1, person2 = line.split()
                if relasjon == "fiendskap":
                    relasjon = False
                else:
                    relasjon = True
                if person1 == person.hentNavn():
                    if person.erIRelasjoner(self.finnPersonObjekt(person2)) == False:
                        person.leggTilRelasjon(self.finnPersonObjekt(person2), relasjon)
                        
                if person2 == person.hentNavn():
                    if person.erIRelasjoner(self.finnPersonObjekt(person1)) == False:
                        person.leggTilRelasjon(self.finnPersonObjekt(person1), relasjon)     
        infile.close()
        print("Lagt til alle relasjoner")

    def finnAntallNøytrale(self):
        totaltAntallPersoner = len(self._personer)
        vennerOgFiender = self._antallVenner + self._antallFiender
        return totaltAntallPersoner - vennerOgFiender  

    def finnPersonObjekt(self, navn):
        for person in self._personer:
            if person.hentNavn() == navn:
                return person

    def gå(self, person): #Personen man går fra
        relasjonTilMeg = person.hentRelasjonTilMeg()
        relasjoner = person.relasjonerSomIkkeErTelt()

        for nyRelasjon in relasjoner:          
            nyPerson = nyRelasjon[0]
            nyRelasjon = nyRelasjon[1] 
            if relasjonTilMeg == False:
                if nyRelasjon == True:
                    nyPerson.settRelasjonTilMeg(False)
                    self._antallFiender += 1
                else:
                    nyPerson.settRelasjonTilMeg(True)
                    self._antallVenner += 1
            else:
                if nyRelasjon == True:
                    nyPerson.settRelasjonTilMeg(True)
                    self._antallVenner += 1

                else:
                    nyPerson.settRelasjonTilMeg(False)
                    self._antallFiender += 1
            nyPerson.tell()
            self.gå(nyPerson)  

            
    def start(self):
        startPerson1 = self.finnPersonObjekt("Asgeir")
        startPerson1.endreRelasjon(True)
        startPerson1.tell()
        self.gå(startPerson1)                

import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(5000)
tre = Tre("etterretningsrapport.txt")

tre.start()

tre.printMineRelasjoner()
                    
                    
                    
