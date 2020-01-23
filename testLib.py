import math
import unittest
from Lib import *

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        u=(3,5)
        v=(5,6)
        self.assertEqual(suma(u,v), (8,11))

    def test_producto(self):
        u=(3,5)
        v=(5,6)
        self.assertEqual(producto(u,v), (-15,43))

    def test_resta(self):
        u=(3,5)
        v=(5,6)
        self.assertEqual(resta(u,v), (-2,-1))

    def test_division(self):
        u=(3,5)
        v=(5,6)
        self.assertEqual(division(u,v), (45/61,7/61))

    def test_modulo(self):
        u=(3,5)
        self.assertEqual(modulo(u), (34**0.5))

    def test_modulob(self):
        v=(5,6)
        self.assertEqual(modulob(v), (61**0.5))

    def test_conjugado(self):
        u=(3,5)
        self.assertEqual(conjugado(u), (3,-5))

    def test_conjugadob(self):
        v=(5,6)
        self.assertEqual(conjugadob(v), (5,-6))

    def test_cartesiano(self):
        u=(3,5)
        self.assertEqual(cartesiano(u), (0.2614672282, 2.988584094))

    def test_cartesianob(self):
        v=(5,6)
        self.assertEqual(cartesianob(v), (0.5226423163, 4.972609477))

    def test_polar(self):
        u=(3,5)
        self.assertEqual(polar(u), (math.sqrt(34), 1.030376827))

    def test_polarb(self):
        v=(5,6)
        self.assertEqual(polarb(v), (math.sqrt(61), 0.8760580506))

    

    

if __name__ == '__main__':
    unittest.main()
