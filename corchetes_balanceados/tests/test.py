import unittest
from corchetes_balanceados import CorchetesBalanceados


class TestCorchetesBalanceados(unittest.TestCase):

    def test_simple(self):
        result = CorchetesBalanceados.run('[]')
        self.assertTrue(result)

    def test_simple_doble(self):
        result = CorchetesBalanceados.run('[[]]')
        self.assertTrue(result)

    def test_impar(self):
        result = CorchetesBalanceados.run('[[-]]')
        self.assertTrue(result)

    def test_par(self):
        result = CorchetesBalanceados.run('[-[]-]')
        self.assertTrue(result)


class TestCorchetesNoBalanceados(unittest.TestCase):

    def test_simple_abierto(self):
        result = CorchetesBalanceados.run('[')
        self.assertFalse(result)

    def test_simple_cerrado(self):
        result = CorchetesBalanceados.run('[')
        self.assertFalse(result)

    def test_impar_cerrado(self):
        result = CorchetesBalanceados.run('[]]')
        self.assertFalse(result)

    def test_par_abierto(self):
        result = CorchetesBalanceados.run('[[]')
        self.assertFalse(result)

    def test_simple_desordenados(self):
        result = CorchetesBalanceados.run('][')
        self.assertFalse(result)

    def test_simple_desordenados_dobles(self):
        result = CorchetesBalanceados.run('][][')
        self.assertFalse(result)


class TestEjemplosBrindados(unittest.TestCase):

    def test_1(self):
        result = CorchetesBalanceados.run('')
        self.assertTrue(result)

    def test_2(self):
        result = CorchetesBalanceados.run('[]')
        self.assertTrue(result)

    def test_3(self):
        result = CorchetesBalanceados.run('[][]')
        self.assertTrue(result)

    def test_4(self):
        result = CorchetesBalanceados.run('[[]]')
        self.assertTrue(result)

    def test_5(self):
        result = CorchetesBalanceados.run('][')
        self.assertFalse(result)

    def test_6(self):
        result = CorchetesBalanceados.run('[[[][]]]')
        self.assertTrue(result)

    def test_7(self):
        result = CorchetesBalanceados.run('][][')
        self.assertFalse(result)

    def test_8(self):
        result = CorchetesBalanceados.run('[][]][')
        self.assertFalse(result)
