from person import Person

class Tre():
    def __init__(self, filnavn):
        self._filnavn = filnavn
        self._personer = []
        self._antallVenner = 1
        self._antallFiender = 1
        self._navn = []
        self.leggTilAllePersoner()
        self.leggTilRelasjoner()

    def hentAlleTelte(self):
        return [x.hentNavn() for x in self._personer if x.erTelt()]

    def hentAllePersoner(self):
        return self._personer

    def printMineRelasjoner(self):
        nøytrale = self.finnAntallNøytrale()
        print("Venner: {}\nFiender: {}\nNøytrale: {}\n".format(self._antallVenner, self._antallFiender, nøytrale))
    
    def sjekkRelasjoner(self, person):
        relasjoner = person.hentRelasjoner()
        return [relasjon for relasjon in relasjoner if not relasjon[0].erTelt()]

    def leggTilAllePersoner(self):
        with open(self._filnavn, "r") as infile:
            for line in infile:
                relasjon, person1, person2 = line.split()
                if relasjon == "fiendskap":
                    relasjon = False
                else:
                    relasjon = True

                if person1 not in self._navn:
                    self._personer.append(Person(person1))
                    self._navn.append(person1)
                if person2 not in self._navn:
                    self._personer.append(Person(person2))
                    self._navn.append(person2)

        print("Lagt til alle personer") 
        print(len(self._personer))  
        infile.close()
    
    def leggTilRelasjoner(self):
        infile = open(self._filnavn)
        lines = infile.readlines()
        for person in self._personer:
            print(person.hentNavn())
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

    def hentAlleNavn(self):
        return self._navn

    def finnPersonObjekt(self, navn):
        for person in self._personer:
            if person.hentNavn() == navn:
                return person


    def gå(self, person): #Personen man går fra
        relasjonTilMeg = person.hentRelasjon()
        muligheter = person.sjekkRelasjoner()
        if len(muligheter) == 0:
            return
        for person in muligheter: 
            nyPerson = person[1]
            relasjon = person[2]
            if relasjonTilMeg == False:
                if relasjon == True:
                    nyPerson.endreRelasjon(False)
                    self._antallFiender += 1
                else:
                    nyPerson.endreRelasjon(True)
                    self._antallVenner += 1

            if relasjonTilMeg == True:
                if relasjon == True:
                    nyPerson.endreRelasjon(True)
                    self._antallVenner += 1

                else:
                    nyPerson.endreRelasjon(False)
                    self._antallFiender += 1
            nyPerson.tell()
            self.gå(nyPerson)        
            
    def start(self):
        startPerson1 = self.finnPersonObjekt("Asgeir")
        startPerson1.endreRelasjon(True)
        startPerson1.tell()
        self.gå(startPerson1)

        startPerson2 = self.finnPersonObjekt("Beate")
        startPerson2.endreRelasjon(False)
        startPerson2.tell()
        self.gå(startPerson2)
                

tre = Tre("etterretningsrapport.txt")

tre.start()

tre.printMineRelasjoner()
                    
                    
                    
