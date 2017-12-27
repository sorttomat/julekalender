class Person():
    def __init__(self, name):
        self._name = name
        self._relationToMe = None
        self._relations = []
       
    def setRelationToMe(self, relation):
        self._relationToMe = relation
    
    def getName(self):
        return self._name

    def getRelationToMe(self):
        return self._relationToMe

    def getRelations(self):
        return self._relations

    def addRelation(self, person, bol):
        self._relations.append([person, bol])
    
    def isInRelations(self, person):
        for relation in self._relations:
            if person.getName() == relation[0].getName():
                return True
        return False
