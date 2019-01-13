class vertex:
    def __init__(self, key):
        self.id = key
        self.connTo = {}

    def addNbr(self, nbr, weight):
        self.connTo[nbr] = weight

    def getConn(self):
        return self.connTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connTo[nbr]

    def __str__(self):
        return f'{self.id} is connected to {[x.id for x in self.connTo]}'


class graph:
    def __init__(self):
        self.vertlist = {}
