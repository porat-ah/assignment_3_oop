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
	
	"""
	*Sets this node info parameter to the given value.
	"""
	
	def getInfo(self):
		return self.info
	
	"""
	*Returns the info parameter of this node.
	"""
	
	def setStatus(self, nStatus):
		self.status = nStatus
		pass
	
	"""
	*Sets this node status parameter to the given value.
	"""
	
	def getStatus(self):
		return self.status
	
	"""
	*Returns the status parameter of this node.
	"""
	
	def setPos(self, x):
		if (self.pos == None):
			self.pos = x
	
	"""
	*Sets the position of the node .
	"""
	
	def incPos(self, size):
		pos = self.pos
		x = pos[0] * size * 10
		y = pos[1] * size * 10
		z = pos[2] * size * 10
		self.pos = (x, y, z)
	
	"""
	*Increases each parameter in the tuple by 10*[inputted parameter]size .
	"""
	
	def getId(self):
		return self.id
	
	"""
	*Returns the id of the node .
	"""
	
	def getPos(self):
		return self.pos
	
	"""
	*Returns the position of the node .
	"""
	
	def setStart(self, id, w):
		self.start_of_edge.update({id: w})
	
	"""
	*Adds an edge to the list of all edges where this node is their src .
	"""
	
	def setEnd(self, id, w):
		self.end_of_edge.update({id: w})
	
	"""
	*Adds an edge to the list of all edges where this node is their dest.
	"""
	
	def removeStart(self, id):
		del self.start_of_edge[id]
	
	"""
	*Removes an edge where the given id is in the end of it and this object at the start.
	"""
	
	def removeEnd(self, id):
		del self.end_of_edge[id]
	
	"""
	*Removes an edge where this object is in the end of it and the given id at the start.
	"""
	
	def getStart(self):
		return self.start_of_edge
	
	"""
	*Returns the neighbors that this node is their src.
	"""
	
	def getEnd(self):
		return self.end_of_edge
	
	"""
	*Returns the neighbors that this node is their target.
	"""
	
	def getDisToStart(self, key: int):
		return self.start_of_edge[key]
	
	"""
	*Returns the weight of the edge between this node and the node whom key is key parameter.
	"""
	
	def getDisToEnd(self, key: int):
		return self.end_of_edge[key]
	
	"""
	*Returns the weight of the edge between node whom key is key parameter and this node .
	"""
	
	def toJson(self):
		pos = self.pos
		try:
			json_obj = {'pos': "{},{},{}".format(pos[0], pos[1], pos[2]), 'id': self.id}
		except:
			json_obj = {'id': self.id}
		return json_obj
	
	"""
	*Retruns a JSON which represents this node.
	"""
	
	def __repr__(self):
		return "%s: |edges out| %s |edges in| %s" % (self.id, len(self.start_of_edge), len(self.end_of_edge))
	
	"""
	*Returns a repr for print function .
	"""
