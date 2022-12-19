import unittest
from numeros_romanos import NumerosRomanos


class NumerosRomanosTest(unittest.TestCase):

    def test_0(self):
        result = NumerosRomanos.run(0)
        self.assertEqual(result, '')

    def test_0_minuscula(self):
        result = NumerosRomanos.run(0, minuscula=True)
        self.assertEqual(result, '')

    def test_3(self):
        result = NumerosRomanos.run(3)
        self.assertEqual(result, 'III')

    def test_3_minuscula(self):
        result = NumerosRomanos.run(3, minuscula=True)
        self.assertEqual(result, 'iii')

    def test_9(self):
        result = NumerosRomanos.run(9)
        self.assertEqual(result, 'IX')

    def test_9_minuscula(self):
        result = NumerosRomanos.run(9, minuscula=True)
        self.assertEqual(result, 'ix')

    def test_10(self):
        result = NumerosRomanos.run(10)
        self.assertEqual(result, 'X')

    def test_10_minuscula(self):
        result = NumerosRomanos.run(10, minuscula=True)
        self.assertEqual(result, 'x')

    def test_68(self):
        result = NumerosRomanos.run(68)
        self.assertEqual(result, 'LXVIII')

    def test_68_minuscula(self):
        result = NumerosRomanos.run(68, minuscula=True)
        self.assertEqual(result, 'lxviii')

    def test_134(self):
        result = NumerosRomanos.run(134)
        self.assertEqual(result, 'CXXXIV')

    def test_666(self):
        result = NumerosRomanos.run(666)
        self.assertEqual(result, 'DCLXVI')

    def test_999(self):
        result = NumerosRomanos.run(666)
        self.assertEqual(result, 'CMXCIX')

