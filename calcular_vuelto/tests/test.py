import unittest
from calcular_vuelto import CalcularVuelto


class TestParams(unittest.TestCase):

    def test_y_bigger_than_x(self):
        try:
            CalcularVuelto.run(100, 101)
        except Exception as e:
            self.assertEqual(e.__str__(), 'El dinero no alcanza')

    def test_x_str(self):
        try:
            CalcularVuelto.run('10', 1)
        except Exception as e:
            self.assertEqual(e.__str__(), 'x debe ser entero')

    def test_y_str(self):
        try:
            CalcularVuelto.run(10, '1')
        except Exception as e:
            self.assertEqual(e.__str__(), 'y debe ser entero')


class TestEjemplosBrindados(unittest.TestCase):

    def test_1(self):
        result = CalcularVuelto.run(100, 100)
        self.assertEqual(result, [0])

    def test_2(self):
        result = CalcularVuelto.run(100, 75)
        self.assertEqual(result, [20, 5])

    def test_3(self):
        result = CalcularVuelto.run(200, 75)
        self.assertEqual(result, [100, 20, 5])

    def test_4(self):
        result = CalcularVuelto.run(1000, 442)
        self.assertEqual(result, [500, 50, 5, 2, 1])

    def test_5(self):
        result = CalcularVuelto.run(500, 50)
        self.assertEqual(result, [200, 200, 50])

    def test_6(self):
        result = CalcularVuelto.run(1889, 1)
        self.assertEqual(result, [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1])
