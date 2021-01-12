import unittest
from GraphAlgo import *
from DiGraph import *
import json


class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        ag = GraphAlgo()
        g = DiGraph()
        ag.init(g)
        self.assertEqual(g, ag.get_graph())
        g.add_node(0)
        self.assertEqual(g, ag.get_graph())

    def test_load_json(self):
        ag = GraphAlgo()
        self.assertTrue(ag.load_from_json("A0"))

    def test_save_json(self):
        ag = GraphAlgo()
        self.assertTrue(ag.load_from_json("A0"))
        self.assertTrue(ag.save_to_json("test.json"))
        with open("A0") as f:
            json_obj1 = json.load(f)
        with open("test.json") as f:
            json_obj2 = json.load(f)
        self.assertEqual(json_obj1, json_obj2)

    def test_shortest_path(self):
        g = DiGraph()
        ag = GraphAlgo(g)
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 4, 1)
        g.add_edge(1, 3, 3)
        g.add_edge(3, 0, 1)
        g.add_edge(4, 3, 1)
        self.assertEqual((3, [0, 2, 4, 3]), ag.shortest_path(0, 3))

    def test_connected_component(self):
        g = DiGraph()
        ag = GraphAlgo(g)
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 4, 1)
        g.add_edge(1, 3, 3)
        g.add_edge(3, 0, 1)
        g.add_edge(4, 3, 1)
        self.assertEqual([0, 1, 2, 3, 4], ag.connected_component(0))
        g.remove_edge(2, 4)
        self.assertEqual([0, 1, 3], ag.connected_component(0))

    def test_connected_component(self):
        g = DiGraph()
        ag = GraphAlgo(g)
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 4, 1)
        g.add_edge(1, 3, 3)
        g.add_edge(3, 0, 1)
        g.add_edge(4, 3, 1)
        self.assertEqual([[0, 1, 2, 3, 4]], ag.connected_components())
        g.remove_edge(2, 4)
        self.assertEqual([[0, 1, 3], [2], [4]], ag.connected_components())

    def test_plot_graph(self):
        ag = GraphAlgo()
        #ag.load_from_json("G_1000_8000_1.json")
        #ag.load_from_json("G_10_80_0.json")
        #ag.load_from_json("A0")
        ag.plot_graph()


if __name__ == '__main__':
    unittest.main()
