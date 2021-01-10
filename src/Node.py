class Node:
    def __init__(self,i:int):
        self.id = i
        self.pos = (0.0,0.0,0.0)
        self.dest = {} # a dict of all edges where this node is in the end of the edge
        self.src = {} # a dict of all edges where this node is in the start of the edge
    def setpos(self,x):
        if(type(x) == tuple and len(x) == 3 ):
             self.pos = x
        else:
            raise TypeError()
    
    def getid(self):
        return self.id

    def getpos(self):
        return self.pos
    
    def setsrc(self,id,w):
        self.src.update({id:w})
        
    def setdest(self,id,w):
        self.dest.update({id:w})
    
    def getsrc(self):
        return self.src
    """
    @return the neighbors that this node is their src
    """
    
    def getdest(self):
        return self.dest
    """
    @return the neighbors that this node is their target
    """
    