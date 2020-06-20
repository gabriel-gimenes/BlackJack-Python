class Card(object):
    def __init__(self,typ,value):
        self.type = typ
        self.value = value

    def setType(self,newtype):
        self.type = newtype

    def getType(self):
        return self.type

    def setValue(self,newvalue):
        self.value = newvalue

    def getValue(self):
        return self.value
