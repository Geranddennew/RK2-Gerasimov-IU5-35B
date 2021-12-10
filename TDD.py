import unittest
from main import taskD1, taskD2, taskD3, ClassDeps


class TestD(unittest.TestCase):

    def test_d1(self):
        self.assertEqual(taskD1(), {'7А': ['Герасимов', 'Макаров'], '8Б': ['Сидоров'], '10А': ['Морозов'], '11Б': ['Иванов']})

    def test_d2(self):
        self.assertEqual(taskD2(), [('8Б', 81.0), ('7А', 80.5), ('9В', 55.5), ('11Б', 53.0), ('10А', 24.0)])

    def test_d3(self):
        self.assertEqual(taskD3(ClassDeps), {'7А': ['Герасимов', 'Макаров'], '10А': ['Троцук', 'Морозов']})


suite = unittest.TestLoader().loadTestsFromTestCase(TestD)
unittest.TextTestRunner(verbosity=2).run(suite)
