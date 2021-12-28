import unittest
from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        file_path = '../data/1000Nodes.json'
        test_path = "../data/testSave.json"
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))
        g = ga.get_graph()
        ga.save_to_json(test_path)
        # ga1 = GraphAlgo()
        # self.assertTrue(ga1.load_from_json(test_path))
        # g1 = ga1.get_graph()
        # self.assertEqual(g.__str__(), g1.__str__())

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        expected_lst = [1, 2, 3, 7]
        self.assertEqual((3.0, expected_lst), ga.shortest_path(1, 7))
        self.assertEqual((float("inf"), []), ga.shortest_path(1, 88))
        expected_lst = [3, 7, 8, 9]
        self.assertEqual((9, expected_lst), ga.shortest_path(3, 9))

    def test_tsp(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        self.assertEqual(([1, 2, 8], 1.5), ga.TSP([1, 8]))
        self.assertEqual(([7,8,9,1], 12), ga.TSP([7, 1]))
        self.assertEqual(([7,3,4,6,7,8,9,1], 22), ga.TSP([7, 1, 4, 9]))



    def test_center_point(self):
        # # test center of A0.json:
        # file = '../data/A0.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((7, 6.806805834715163), graphAlgo.centerPoint())
        #
        # # test center of A1.json:
        # file = '../data/A1.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((8, 9.925289024973141), graphAlgo.centerPoint())
        #
        # # test center of A2.json:
        # file = '../data/A2.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((0, 7.819910602212574), graphAlgo.centerPoint())
        #
        # # test center of A3.json:
        # file = '../data/A3.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((2, 8.182236568942237), graphAlgo.centerPoint())
        #
        # # test center of A4.json:
        # file = '../data/A4.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((6, 8.071366078651435), graphAlgo.centerPoint())
        #
        # # test center of A5.json:
        # file = '../data/A5.json'
        # graphAlgo = GraphAlgo()
        # self.assertTrue(graphAlgo.load_from_json(file))
        # self.assertEqual((40, 9.291743173960954), graphAlgo.centerPoint())
        # test center of A0.json:
        file = '../data/1000Nodes.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((7, 6.806805834715163), graphAlgo.centerPoint())

    def test_plot_graph(self):
        self.fail()

    def test_tsp1000(self):
        file = '../data/1000Nodes.json'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual(([1, 720, 719, 954, 172, 105, 179, 787, 56, 616, 12, 265, 8], 1250.8403048176592), graphAlgo.TSP([1, 8]))

    def test_shortest(self):
        g_algo = GraphAlgo()
        file1 = '../data/1000Nodes.json'
        g_algo.load_from_json(file1)
        self.assertEqual(g_algo.shortest_path(0, 8), (22.59506068993273, [0, 1, 2, 6, 7, 8]))
        self.assertEqual(g_algo.shortest_path(0, 16), (1.3118716362419698, [0, 16]))
        self.assertEqual(g_algo.shortest_path(16, 3), (14.129670896183516, [16, 0, 1, 2, 3]))

    def test_shortest1000(self):
        file = '../data/1000Nodes.json'
        graphAlgo = GraphAlgo()
        expected_lst = [1, 2, 3, 7]
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((1357.3070765153861, [1, 720, 234, 538, 433, 7] ), graphAlgo.shortest_path(1, 7))
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
