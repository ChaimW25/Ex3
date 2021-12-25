import unittest
from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        file_path = '../data/A1.json'
        test_path = "../data/testSave.json"
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))
        g = ga.get_graph()
        ga.save_to_json(test_path)
        ga1 = GraphAlgo()
        self.assertTrue(ga1.load_from_json(test_path))
        g1 = ga1.get_graph()
        self.assertEqual(g.__str__(), g1.__str__())

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
