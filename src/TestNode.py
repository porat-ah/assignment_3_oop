import unittest
from src.Node import Node


class TestNode(unittest.TestCase):
	def testGetId(self):
		n1 = Node(0)
		n2 = Node(0)
		self.assertEqual(n1.getId(), n2.getId())
		self.assertEqual(n1.getId(), 0)
		n2 = Node(1)
		self.assertNotEqual(n1.getId(), n2.getId())
	
	def testInfo(self):
		n1 = Node(0)
		n2 = Node(0)
		self.assertEqual(n1.getInfo(), n2.getInfo())
		n1.setInfo(5)
		self.assertNotEqual(n1.getInfo(), n2.getInfo())
	
	def testStatus(self):
		n1 = Node(0)
		n2 = Node(0)
		self.assertEqual(n1.getStatus(), n2.getStatus())
		n2.setStatus(True)
		self.assertNotEqual(n1.getStatus(), n2.getStatus())
	
	def testPos(self):
		n1 = Node(0)
		n2 = Node(0)
		self.assertEqual(n1.getPos(), n2.getPos())
		n1.setPos((0, 0, 1))
		self.assertNotEqual(n1.getPos(), n2.getPos())
		n2.setPos((0, 0, 1))
		self.assertEqual(n1.getPos(), n2.getPos())
		n1.incPos(5)
		self.assertEqual(n1.getPos(), (0, 0, 50))
	
	def testConnections(self):
		n1 = Node(0)
		n2 = Node(1)
		self.assertEqual(n1.getStart(), n2.getStart())
		n1.setEnd(n2, 1)
		n2.setStart(n1, 1)
		self.assertNotEqual(n1.getStart(), n2.getStart())
		self.assertNotEqual(n1.getEnd(), n2.getEnd())
	
	def testJson(self):
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		n2.setStart(n1.getId(), 12)
		n2.setEnd(n3.getId(), 23)
		self.assertEqual(n2.toJson(), {'id': 2})
	
	def testPrint(self):
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		n2.setStart(n1.getId(), 12)
		n2.setEnd(n3.getId(), 23)
		self.assertEqual(n2.__repr__(), "2: |edges out| 1 |edges in| 1")


if __name__ == '__main__':
	unittest.main()
