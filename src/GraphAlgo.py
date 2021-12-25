import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Node import Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:

        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                g = DiGraph()
                for i in data['Nodes']:
                    if 'pos' in i.keys():
                        str_lst = i['pos'].split(',')
                        pos = (float(str_lst[0]), float(str_lst[1]))
                        g.add_node(i['id'], pos)
                    else:
                        g.add_node(i['id'])
                for i in data['Edges']:
                    g.add_edge(i['src'], i['dest'], i['w'])
                self.graph = g

        except Exception as e:
            print(e)
            return False

        return True

    def save_to_json(self, file_name: str) -> bool:

        newJson = dict()
        newJson["Edges"] = list()
        newJson["Nodes"] = list()

        for node in self.graph.get_all_v().values():
            if node.getPos() is None:
                pos = '0.0,0.0,0.0'
            else:
                pos = str(str(node.getPos()[0]) + ',' + str(node.getPos()[1]) + ',0.0')
            newJson["Nodes"].append({"pos": pos, "id": node.getId()})
            for edge in self.graph.all_out_edges_of_node(node.getId()).items():
                newJson["Edges"].append({"src": node.getId(), "w": edge[1], "dest": edge[0]})

        try:
            with open(file_name, 'w') as json_f:
                json.dump(newJson, json_f)
                return True

        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass
