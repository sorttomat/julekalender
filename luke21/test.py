class Vennskap():
    def __init__(self):
        self._medlemmerIVennskap = set()
        self._fiendskap = set()
    
    def hentMedlemmer(self):
        return self._medlemmerIVennskap

    def leggTilMedlem(self, person):
        self._medlemmerIVennskap.add(person)
    
    def erMedlem(self, person):
        for venn in self._medlemmerIVennskap:
            if venn == person:
                return True
        return False

    def leggTilFiendskap(self, vennegruppe):
        self._fiendskap.add(vennegruppe)
            
class Relasjoner():
    def __init__(self, filename):
        self._filename = filename
        self._vennskap = []
    
    def erPersonMedlemIVennskap(self, person):
        for vennskap in self._vennskap:
            if vennskap.erMedlem(person):
                return True
        return False
                   
    def hvilketVennskapErPersonMedlemI(self, person):
        for vennskap in self._vennskap:
            if vennskap.erMedlem(person):
                return vennskap

    def opprettVennskap(self, person):
        vennskap = Vennskap()
        self._vennskap.append(vennskap)
        vennskap.leggTilMedlem(person)

    def slåSammenVennskap(self, vennskap1, vennskap2):
        sammenslått = Vennskap()
        for venn in vennskap2.hentMedlemmer():
            sammenslått.leggTilMedlem(venn)
        for venn in vennskap1.hentMedlemmer():
            sammenslått.leggTilMedlem(venn)
        fiendskap1 = vennskap1._fiendskap
        fiendskap2 = vennskap2._fiendskap
        sammenslåttFiendskap = Vennskap()

        for fiendskap in fiendskap1:
            for fiende in fiendskap.hentMedlemmer():
                sammenslåttFiendskap.leggTilMedlem(fiende)
        for fienskap in fiendskap2:
            for fiende in fiendskap.hentMedlemmer():
                sammenslåttFiendskap.leggTilMedlem(fiende)
        
        sammenslått.leggTilFiendskap(sammenslåttFiendskap)
        sammenslåttFiendskap.leggTilFiendskap(sammenslått)
        self._vennskap.remove(fiendskap1)
        self._vennskap.remove(fiendskap2)
        self._vennskap.remove(vennskap1)
        self._vennskap.remove(vennskap2)
        self._vennskap.append(sammenslåttFiendskap)
        self._vennskap.append(sammenslått)
        
    def lesInnPersoner(self):
        infile = open(self._filename)
        for line in infile:
            relasjon, person1, person2 = line.split()
            if relasjon == "vennskap":
                if self.erPersonMedlemIVennskap(person1) and self.erPersonMedlemIVennskap(person2):
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe2 = self.hvilketVennskapErPersonMedlemI(person2)
                    if gruppe != gruppe2:
                        self.slåSammenVennskap(gruppe, gruppe2)
                
                elif self.erPersonMedlemIVennskap(person1):
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe.leggTilMedlem(person2)
                
                elif self.erPersonMedlemIVennskap(person2):
                    gruppe = self.hvilketVennskapErPersonMedlemI(person2)
                    gruppe.leggTilMedlem(person1)
                
                else:
                    self.opprettVennskap(person1)
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe.leggTilMedlem(person2)
            
            else:
                if self.erPersonMedlemIVennskap(person1) and self.erPersonMedlemIVennskap(person2):
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe2 = self.hvilketVennskapErPersonMedlemI(person2)
                    gruppe.leggTilFiendskap(gruppe2)
                    gruppe2.leggTilFiendskap(gruppe)
                
                elif self.erPersonMedlemIVennskap(person1):
                    self.opprettVennskap(person2)
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe2 = self.hvilketVennskapErPersonMedlemI(person2)

                    gruppe.leggTilFiendskap(gruppe2)
                    gruppe2.leggTilFiendskap(gruppe)
                
                elif self.erPersonMedlemIVennskap(person2):
                    self.opprettVennskap(person1)
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe2 = self.hvilketVennskapErPersonMedlemI(person2)

                    gruppe.leggTilFiendskap(gruppe2)
                    gruppe2.leggTilFiendskap(gruppe)
                
                else:
                    self.opprettVennskap(person1)
                    self.opprettVennskap(person2)
                    gruppe = self.hvilketVennskapErPersonMedlemI(person1)
                    gruppe2 = self.hvilketVennskapErPersonMedlemI(person2)

                    gruppe.leggTilFiendskap(gruppe2)
                    gruppe2.leggTilFiendskap(gruppe)

    def printRelasjoner(self):
        for vennskap in self._vennskap:
            print()
            print(vennskap.hentMedlemmer())
            print("fiender:")
            for fiendskap in vennskap._fiendskap:
                print(fiendskap.hentMedlemmer())
        print()
    
    def kjør(self):
        gruppe = self.hvilketVennskapErPersonMedlemI("Asgeir")
        fiendegrupper = gruppe._fiendskap
        for fiendegruppe in fiendegrupper:
            fienderAvFiender = fiendegruppe._fiendskap
            for fgruppe in fienderAvFiender:
                self.slåSammenVennskap(gruppe, fgruppe)
            
            








relasjoner = Relasjoner("vennerFiender.txt")
relasjoner.lesInnPersoner()
relasjoner.lesInnPersoner()
relasjoner.lesInnPersoner()
relasjoner.lesInnPersoner()
relasjoner.lesInnPersoner()
relasjoner.lesInnPersoner()

#relasjoner.kjør()

relasjoner.printRelasjoner()
                
                


