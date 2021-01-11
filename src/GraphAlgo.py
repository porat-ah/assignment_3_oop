import json
import matplotlib.pyplot as plt
from typing import List
import numpy as np
from queue import PriorityQueue
from queue import Queue
import pandas as pd
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph

class GraphAlgo (GraphAlgoInterface):
    def __init__(self,g = None):
        self.graph = g

    def init(self, g):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph
        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as f:
            json_obj = json.load(f)
        graph = DiGraph()
        for node in json_obj['Nodes']:
            temp = []
            for i in node['pos'].split(",") :
                temp.append((float)(i))
            pos = tuple(temp)
            _id = node['id']
            graph.add_node(_id,pos)
        for edge in json_obj['Edges']:
            graph.add_edge(edge['src'],edge['dest'],edge['w'])
        self.graph = graph
        return True
        
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

    def save_to_json(self, file_name: str) -> bool:
        graph = self.graph
        Nodes = []
        Edges = []
        nodes = list(graph.get_all_v().values())
        for node  in nodes:
            Nodes.append(node.toJson())
            src = node.id
            for _id,w in node.getStart().items():
                edge = {'src':src,'w':w,'dest':_id}
                Edges.append(edge)
        json_object = {'Edges':Edges,'Nodes':Nodes}
        
        with open(file_name,'w') as f:
            json.dump(json_object,f)
        return True
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        graph = self.graph
        try:
            graph.get_node(id1)
            graph.get_node(id2)
            if(graph.v_size() != 2):
                q = PriorityQueue()
                q.put((0, id1))
                prev = {}
                prev.update({id1:id1})
                weight = {}
                weight.update({id1:0})
                visited = set([])
                while(not q.empty()):
                    _id = q.get()[1]
                    if(not visited.__contains__(_id)):
                        visited.add(_id)
                    if(_id == id2):
                        curr_id = _id
                        path = [curr_id]
                        while(curr_id != id1):
                            curr_id = prev.get(curr_id)
                            path.append(curr_id)
                        path.reverse()
                        output = (weight[id2],path)
                        return output
                    edges = graph.all_out_edges_of_node(_id)
                    for i,w in edges.items():
                        dist = weight[_id]
                        dist += w
                        if(weight.__contains__(i)):
                            if(weight[i] > dist):
                                prev.update({i:_id})
                                weight.update({i:dist})
                                q.put((dist,i))
                        else:
                            prev.update({i: _id})
                            weight.update({i:dist})
                            q.put((dist, i))
        except:
            return (float('inf'),[])
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

    def connected_component(self, id1: int) -> list:
        graph = self.graph
        try:
            s1 = self.BFS(id1)
            self.graph.setTranspose()
            s2 = self.BFS(id1)
            output = []
            for i in list(s1):
                for j in list(s2):
                    if(i == j):
                        output.append(i)
            return output
        except:
            return []
        """
            Finds the Strongly Connected Component(SCC) that node id1 is a part of.
            @param id1: The node id
            @return: The list of nodes in the SCC
        """
    def BFS(self,id1):
        q = Queue()
        q.put(id1)
        prev = {}
        prev.update({id1:id1})
        while(not q.empty()):
            _id = q.get()
            edges = self.graph.all_out_edges_of_node(_id)
            for i in edges:
                if(prev.get(i) == None):
                    q.put(i)
                    prev.update({i:_id})
        output = set(prev.keys())
        return output

    def connected_components(self) -> List[list]:
        graph = self.graph
        try:
            nodes = graph.get_all_v()
            s = set([])
            output = []
            for i in nodes:
                if(not s.__contains__(i)):
                    s.add(i)
                    l = self.connected_component(i)
                    output.append(l)
                    for j in l:
                        s.add(j)
            return output
        except:
            return []

        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
    # todo finish the function
    def plot_graph(self) -> None:
        graph = self.graph
        size = self.graph.v_size()
        np.random.seed(0)
        normal_dis1 = size*np.abs(np.random.randn(size))
        normal_dis2 = size*np.abs(np.random.randn(size))
        ax = plt.gca()
        plt.axis("scaled")
        nodes = list(graph.get_all_v().values())
        i = 0
        for node in nodes:
            pos = (normal_dis1[i],normal_dis2[i],0.0)
            node.setPos(pos)
        max_x = nodes[0].getPos()[0]
        min_x = max_x
        max_y = nodes[0].getPos()[1]
        min_y = max_y
        for node in nodes:
            for _id in node.getStart():
                node2 = graph.get_node(_id)
                pos1 = node.getPos()
                pos2 = node2.getPos()
                dis = self.distance(pos1,pos2)
                a = plt.Arrow(x = pos1[0],y = pos1[1],dx = dis[0],dy = dis[1],width = 1,color = 'k')
                ax.add_patch(a)
            pos = node.getPos()
            if(max_x < pos[0]):
                max_x = pos[0]
            elif(min_x > pos[0]):
                min_x = pos[0]
            if (max_y < pos[1]):
                max_y = pos[1]
            elif (min_y > pos[1]):
                min_y = pos[1]

            c = plt.Circle((pos[0],pos[1]),1)
            plt.text(pos[0]+1, pos[1]+1, node.getId(), fontsize=10)
            ax.add_patch(c)
        ax.xaxis.zoom(-(max_x)*10)
        ax.yaxis.zoom(-(max_y)*10)
        plt.show()








        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

    def distance (self,pos1,pos2):
        return (pos2[0]-pos1[0],pos2[1]-pos1[1],pos2[2]-pos1[2])