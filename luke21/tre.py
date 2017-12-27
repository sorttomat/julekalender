from person import Person

class Tree():
    def __init__(self, filnavn):
        self._people = []
        self._numberOfFriends = 1
        self._numberOfEnemies = 0
        self._countedPeople = set()
        self._names = []
        self.addAllPeople(filnavn)
        self.addAllRelations(filnavn)

    def isCounted(self, personObject):
        if personObject in self._countedPeople:
            return True
        return False

    def isAlreadyAdded(self, person):
        if person in self._names:
            return True
        return False

    def countPerson(self, personObject):
        self._countedPeople.add(personObject)
        
    def getAllPeople(self):
        return self._people

    def addPerson(self, navn):
        self._people.append(Person(navn))
        self._names.append(navn)

    def printMyRelations(self):
        neutrals = self.findAllNeutrals()
        print("Friends: {}\nEnemies: {}\nNeutrals: {}\n".format(self._numberOfFriends, self._numberOfEnemies, neutrals))

    def addAllPeople(self, filename):
        with open(filename, "r") as infile:
            for line in infile:
                relation, person1, person2 = line.split()
                if not self.isAlreadyAdded(person1):
                    self.addPerson(person1)
                if not self.isAlreadyAdded(person2):
                    self.addPerson(person2)
        print("Added all people!")
        infile.close()
    
    def addAllRelations(self, filename):
        infile = open(filename)
        lines = infile.readlines()
        for line in lines:
            relation, person1, person2 = line.split()
            person1 = self.findPersonObject(person1)
            person2 = self.findPersonObject(person2)
            if relation == "fiendskap":
                relation = False
            else:
                relation = True
            if not person1.isInRelations(person2):
                person1.addRelation(person2, relation)      
            if not person2.isInRelations(person1):
                person2.addRelation(person1, relation)     
        infile.close()
        print("Added all relations!")

    def findAllNeutrals(self):
        totalNumberOfPeople = len(self._people)
        friendsEnemies = self._numberOfFriends + self._numberOfEnemies
        return totalNumberOfPeople - friendsEnemies  

    def findPersonObject(self, name):
        for person in self._people:
            if person.getName() == name:
                return person

    def go(self, person): #Personen man går fra
        relationToMe = person.getRelationToMe()
        relations = person.getRelations()
        for relation in relations:          
            newPerson = relation[0]
            if self.isCounted(newPerson):
                continue

            newRelation = relation[1]
            if relationToMe == False:
                if newRelation == True:
                    newPerson.setRelationToMe(False)
                    self._numberOfEnemies += 1
                else:
                    newPerson.setRelationToMe(True)
                    self._numberOfFriends += 1
            else:
                if newRelation == True:
                    newPerson.setRelationToMe(True)
                    self._numberOfFriends += 1
                else:
                    newPerson.setRelationToMe(False)
                    self._numberOfEnemies += 1
            self.countPerson(newPerson)
            self.go(newPerson)  
   
    def start(self):
        startPerson = self.findPersonObject("Asgeir")
        startPerson.setRelationToMe(True)
        self.countPerson(startPerson)
        self.go(startPerson)         

import sys

sys.setrecursionlimit(5000)
tree = Tree("etterretningsrapport.txt")

tree.start()

tree.printMyRelations()
                    
                    
                    
