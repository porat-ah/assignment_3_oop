class Node:
    def __init__(self, i: int):
        self.id = i
        self.pos = None
        self.end_of_edge = {}  # a dict of all edges where this node is in the end of the edge
        self.start_of_edge = {}  # a dict of all edges where this node is in the start of the edge
        self.info = -1
        self.status = False

    def setInfo(self, nInfo):
        self.info = nInfo
        pass

    def getInfo(self):
        return self.info

    def setStatus(self, nStatus):
        self.status = nStatus
        pass

    def getStatus(self):
        return self.status

    def setPos(self, x):
        if (self.pos == None):
            self.pos = x

    """
    set the position of the node
    """

    def incPos(self,size):
        pos = self.pos
        x = pos[0] * size*10
        y = pos[1] * size*10
        z = pos[2] * size*10
        self.pos = (x, y, z)

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


    def setStart(self, id, w):
        self.start_of_edge.update({id: w})
    """
    add an edge to the list of all edges where this node is their src
    """


    def setEnd(self, id, w):
        self.end_of_edge.update({id: w})
    """
    add an edge to the list of all edges where this node is their dest
    """


    def removeStart(self, id):
        del self.start_of_edge[id]


    """
    remove an edge where the given id is in the end of it and this object at the start
    """


    def removeEnd(self, id):
        del self.end_of_edge[id]


    """
    remove an edge where this object is in the end of it and the given id at the start
    """


    def getStart(self):
        return self.start_of_edge


    """
    @return the neighbors that this node is their src
    """


    def getEnd(self):
        return self.end_of_edge


    """
    @return the neighbors that this node is their target
    """


    def getDisToStart(self, key: int):
        return self.start_of_edge[key]


    """
    @returns the weight of the edge between this node and the node whom key is @param key.
    """


    def getDisToEnd(self, key: int):
        return self.end_of_edge[key]


    """
    @returns the weight of the edge between node whom key is @param key and this node .
    """


    def toJson(self):
        pos = self.pos
        try:
            json_obj = {'pos': "{},{},{}".format(pos[0], pos[1], pos[2]), 'id': self.id}
        except:
            json_obj = {'id': self.id}
        return json_obj


    """
    @return a dict for json
    """


    def __repr__(self):
        return "%s: |edges out| %s |edges in| %s" % (self.id, len(self.start_of_edge), len(self.end_of_edge))
