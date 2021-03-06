import unittest
from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_load_save_json(self):
        file_path = '../data/A5.json'
        test_path = "../data/testSave.json"
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))
        g = ga.get_graph()
        ga.save_to_json(test_path)
        ga1 = GraphAlgo()
        self.assertTrue(ga1.load_from_json(test_path))
        g1 = ga1.get_graph()
        self.assertEqual(g.__str__(), g1.__str__())

    def test_shortest_path(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        self.assertEqual((3.0, [1, 2, 3, 7]), ga.shortest_path(1, 7))
        self.assertEqual((float("inf"), []), ga.shortest_path(1, 88))
        self.assertEqual((9, [3, 7, 8, 9]), ga.shortest_path(3, 9))

    def test_tsp(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        self.assertEqual(([1, 2, 8], 1.5), ga.TSP([1, 8]))
        self.assertEqual(([7,8,9,1], 12), ga.TSP([7, 1]))
        self.assertEqual(([7,3,4,6,7,8,9,1], 22), ga.TSP([7, 1, 4, 9]))



    def test_center_point(self):
        # test center of A0.json:
        file = '../data/A0.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((7, 6.806805834715163), graphAlgo.centerPoint())

        # test center of A1.json:
        file = '../data/A1.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((8, 9.925289024973141), graphAlgo.centerPoint())

        # test center of A2.json:
        file = '../data/A2.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((0, 7.819910602212574), graphAlgo.centerPoint())

        # test center of A3.json:
        file = '../data/A3.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((2, 8.182236568942237), graphAlgo.centerPoint())

        # test center of A4.json:
        file = '../data/A4.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((6, 8.071366078651435), graphAlgo.centerPoint())

        # test center of A5.json:
        file = '../data/A5.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((40, 9.291743173960954), graphAlgo.centerPoint())

    # def test_1000json(self):
    #     # test save&load:
    #     file_path = '../data/1000Nodes.json'
    #     test_path = "../data/testSave.json"
    #     graphAlgo = GraphAlgo()
    #     self.assertTrue(graphAlgo.load_from_json(file_path))
    #     self.assertTrue(graphAlgo.save_to_json(test_path))

        # #test center:
        # self.assertEqual((362, 1185.9594924690523), graphAlgo.centerPoint())

        # #test tsp:
        # self.assertEqual(([7, 218, 407, 475, 990, 96, 844, 1, 720, 719, 44, 445, 9, 772, 976, 888, 374, 497, 861, 818, 337, 112, 4], 3215.874793828493), graphAlgo.TSP([7, 1, 4, 9]))

        # # #test shortest path:
        # self.assertEqual((374.84683509966385, [20, 80, 945, 128, 108, 556]), graphAlgo.shortest_path(20, 556))

    @staticmethod
    def simple_graph_generate():
        """
        DiGraph: |V| = 10	|E| = 16
        {0: (0), 1: (1), 2: (2), 3: (3), 4: (4), 5: (5), 6: (6), 7: (7), 8: (8), 9: (9)}
        Edge Data:
        (1) -> {9: 0.5, 2: 0.5}
        (2) -> {8: 1.0, 3: 1.0}
        (3) -> {7: 1.5, 4: 1.5}
        (4) -> {6: 2.0, 5: 2.0}
        (5) -> {6: 2.5}
        (6) -> {4: 3.0, 7: 3.0}
        (7) -> {3: 3.5, 8: 3.5}
        (8) -> {2: 4.0, 9: 4.0}
        (9) -> {1: 4.5}
        https://user-images.githubusercontent.com/73063199/103218639-3a423580-4924-11eb-8316-f438c2846570.png      """
        g = DiGraph()
        for i in range(10):
            g.add_node(i)

        for i in range(10):
            g.add_edge(i, 10 - i, i * 0.5)
            g.add_edge(i, i + 1, i * 0.5)
        return g


if __name__ == '__main__':
    unittest.main()
