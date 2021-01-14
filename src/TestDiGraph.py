import unittest
from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):
	
	def test_v_size(self):
		g = DiGraph()
		self.assertEqual(0, g.v_size())
		g.add_node(0)
		self.assertEqual(1, g.v_size())
		self.assertEqual(1, g.get_mc())
		g.add_node(0)
		self.assertEqual(1, g.v_size())
		self.assertEqual(1, g.get_mc())
	
	def test_e_size(self):
		g = DiGraph()
		self.assertEqual(0, g.e_size())
		g.add_node(0)
		g.add_node(1)
		g.add_edge(0, 1, 1)
		self.assertEqual(1, g.e_size())
		self.assertEqual(3, g.get_mc())
		g.add_edge(1, 0, 1)
		self.assertEqual(2, g.e_size())
		self.assertEqual(4, g.get_mc())
		g.add_edge(1, 0, 1)
		g.add_edge(1, 1, 1)
		g.add_edge(10, 0, 1)
		g.add_edge(1, 10, 1)
		g.add_edge(10, 10, 1)
		g.add_edge(10, 100, 1)
		self.assertEqual(2, g.e_size())
		self.assertEqual(4, g.get_mc())
	
	def test_remove_node(self):
		g = DiGraph()
		self.assertEqual(0, g.v_size())
		g.add_node(0)
		self.assertEqual(1, g.get_mc())
		self.assertTrue(g.remove_node(0))
		self.assertEqual(2, g.get_mc())
		self.assertFalse(g.remove_node(0))
		self.assertEqual(2, g.get_mc())
		g.add_node(0)
		g.add_node(1)
		g.add_edge(0, 1, 1)
		g.add_edge(1, 0, 1)
		self.assertTrue(g.remove_node(0))
		self.assertEqual(7, g.get_mc())
	
	def test_remove_edge(self):
		g = DiGraph()
		self.assertEqual(0, g.e_size())
		g.add_node(0)
		self.assertEqual(1, g.get_mc())
		g.remove_edge(0, 1)
		self.assertEqual(1, g.get_mc())
		g.add_node(1)
		g.add_edge(0, 1, 1)
		self.assertTrue(g.remove_edge(0, 1))
		self.assertEqual(4, g.get_mc())
	
	def test_get_all_v(self):
		g = DiGraph()
		self.assertEqual({}, g.get_all_v())
		g.add_node(0)
		self.assertEqual(1, len(g.get_all_v()))
	
	def test_all_in_edges_of_node(self):
		g = DiGraph()
		g.add_node(0)
		g.add_node(1)
		g.add_edge(0, 1, 1)
		self.assertEqual(0, len(g.all_out_edges_of_node(1)))
		self.assertEqual(1, len(g.all_in_edges_of_node(1)))
	
	def test_all_out_edges_of_node(self):
		g = DiGraph()
		g.add_node(0)
		g.add_node(1)
		g.add_edge(1, 0, 1)
		self.assertEqual(0, len(g.all_in_edges_of_node(1)))
		self.assertEqual(1, len(g.all_out_edges_of_node(1)))


if __name__ == '__main__':
	unittest.main()
