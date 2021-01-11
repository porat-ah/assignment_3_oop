from src.GraphInterface import GraphInterface
from src.Node import Node

class DiGraph(GraphInterface):
    def __init__(self):
        self.mc = 0
        self.edgeSize = 0
        self.nodes = {}
        self.transpose = False
        pass

    def getTranspose(self):
        return self.transpose

    # """
    #     @return transposition status.
    # """

    def setTranspose(self):
        self.transpose = not self.transpose
        pass

    # """
    #     *Set transposition status.
    # """

    def v_size(self) -> int:
        return len(self.nodes)

    # """
    #     @return: The number of vertices in this graph
    # """

    def e_size(self) -> int:
        return self.edgeSize

    # """
    #     @return: The number of edges in this graph
    # """

    def get_all_v(self) -> dict:
        return self.nodes

    # """
    #     @return a dictionary of all the nodes in the Graph
    # """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if (self.transpose):
            try:
                return self.nodes[id1].getSrc()
            except:
                raise ValueError
        else:
            try:
                return self.nodes[id1].getDest()
            except:
                raise ValueError

    # """
    #     @return a dictionary of all the nodes connected to (into) node_id
    # """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if (self.transpose):
            try:
                return self.nodes[id1].getDest()
            except:
                raise ValueError
        else:
            try:
                return self.nodes[id1].getSrc()
            except:
                raise ValueError

    # """
    #     @return a dictionary of all the nodes connected from node_id
    # """

    def get_mc(self) -> int:
        return self.mc

    # """
    #     Returns the current version of this graph,
    #     @return: The current version of this graph.
    # """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        try:
            if (self.nodes[id1].getDisToDest(id2) == weight):
                return False
            self.nodes[id1].setDest(id2, weight)
            self.mc += 1
            return True
        except:
            return False

    # """
    #     Adds an edge to the graph.
    #     @param id1: The start node of the edge
    #     @param id2: The end node of the edge
    #     @param weight: The weight of the edge
    #     @return: True if the edge was added successfully, False o.w.
    # """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if (node_id in self.nodes):
            return False
        node = Node(node_id)
        node.setPos(pos)
        self.nodes.update({node_id: node})
        self.mc += 1
        return True

    # """
    #     Adds a node to the graph.
    #     @param node_id: The node ID
    #     @param pos: The position of the node
    #     @return: True if the node was added successfully, False o.w.
    # """

    def remove_node(self, node_id: int) -> bool:
        if (node_id not in self.nodes):
            return False
        for edgeTo in self.all_in_edges_of_node(node_id):
            self.remove_edge(edgeTo, node_id)
        for edgeFrom in self.all_out_edges_of_node(node_id):
            self.remvoe_edge(edgeFrom, node_id)
        self.nodes.pop(node_id)
        return True

    # """
    #     Removes a node from the graph.
    #     @param node_id: The node ID
    #     @return: True if the node was removed successfully, False o.w.
    # """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 not in self.nodes or node_id2 not in self.nodes):
            return False
        if (node_id1 in self.nodes[node_id2].getSrc()):
            self.nodes[node_id1].getDest().pop(node_id2)
            self.nodes[node_id2].getSrc().pop(node_id1)
            return True
        return True

    # """
    #     Removes an edge from the graph.
    #     @param node_id1: The start node of the edge
    #     @param node_id2: The end node of the edge
    #     @return: True if the edge was removed successfully, False o.w.
    # """






















    