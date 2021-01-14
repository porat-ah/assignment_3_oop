import networkx as nx


def load_from_json(file_name: str):
        graph = nx.DiGraph()
        with open(file_name) as f:
            json_obj = json.load(f)
        for node in json_obj['Nodes']:
            temp = []
            _id = node['id']
            try:
                for i in node['pos'].split(","):
                    temp.append((float)(i))
                pos = tuple(temp)
            except:
                pos = None
            graph.add_node(_id, pos=pos)
        for edge in json_obj['Edges']:
            graph.add_edge(edge['src'], edge['dest'], weight=edge['w'])
        return graph