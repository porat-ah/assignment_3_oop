class Node:
    def __init__(self, i: int):
        self.id = i
        self.pos = (0.0, 0.0, 0.0)
        self.dest = {}  # a dict of all edges where this node is in the end of the edge
        self.src = {}  # a dict of all edges where this node is in the start of the edge

    def setPos(self, x):
        self.pos = x
    """
    set the position of the node
    """
    def getId(self):
        return self.id
    """
    @return the id of the node
    """

    def getPos(self):
        return self.pos
    """
    @return the position of the node
    """

    def setSrc(self, id, w):
        self.src.update({id: w})
        """
        add an edge to the list of all edges where this node is their src
        """

    def setDest(self, id, w):
        self.dest.update({id: w})
        """
        add an edge to the list of all edges where this node is their dest
        """

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
    
    def toJson(self):
        pos = self.pos
        return {'pos':"{},{},{}".format(pos[0],pos[1],pos[2]),'id':self.id}
    """
    @return a dict for json 
    """
