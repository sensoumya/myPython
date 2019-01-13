class Vertex:
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


class Graph:
    def __init__(self):
        self.vertlist = {}
        self.vertCount = 0

    def addVertex(self, key):
        newVert = vertex(key)
        self.vertlist[key] = newVert
        self.vertCount += 1

    def getVertex(self, n):
        if n in self.vertlist:
            return self.vertlist[key]
        else:
            return None

    def addEdge(self, f, t, wt=0):
        if f not in self.vertlist:
            nv = self.addVertex(f)
        if t not in self.vertlist:
            nv = self.addVertex(t)
        self.vertlist[f].addNbr(self.vertlist[t], wt)

    def getVert(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

    def __contains__(self, n):
        return n in self.vertlist


# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# g.vertlist
# g.addEdge(0, 1, 2)
# for vertex in g:
#     print(vertex)
#     print(vertex.getConn(), end='\n')
