class Node:
    def __init__(self, i: int):
        self.id = i
        self.pos = (0.0, 0.0, 0.0)
        self.dest = {}  # a dict of all edges where this node is in the end of the edge
        self.src = {}  # a dict of all edges where this node is in the start of the edge

    def setPos(self, x):
        if (type(x) == tuple and len(x) == 3):
            self.pos = x
        else:
            raise TypeError()

    def getId(self):
        return self.id

    def getPos(self):
        return self.pos

    def setCrc(self, id, w):
        self.src.update({id: w})

    def setDest(self, id, w):
        self.dest.update({id: w})

    def getSrc(self):
        return self.src

    """
    @return the neighbors that this node is their src
    """

    def getDest(self):
        return self.dest

    """
    @return the neighbors that this node is their target
    """
