import math
import unittest
from LibCom import *


class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        u = (3, 5)
        v = (5, 6)
        self.assertEqual(suma(u, v), (8, 11))

    def test_producto(self):
        u = (3, 5)
        v = (5, 6)
        self.assertEqual(producto(u, v), (-15, 43))

    def test_resta(self):
        u = (3, 5)
        v = (5, 6)
        self.assertEqual(resta(u, v), (-2, -1))

    def test_division(self):
        u = (3, 5)
        v = (5, 6)
        self.assertEqual(division(u, v), (45 / 61, 7 / 61))

    def test_modulo(self):
        u = (3, 5)
        self.assertEqual(modulo(u), (34 ** 0.5))

    def test_modulob(self):
        v = (5, 6)
        self.assertEqual(modulob(v), (61 ** 0.5))

    def test_conjugado(self):
        u = (3, 5)
        self.assertEqual(conjugado(u), (3, -5))

    def test_conjugadob(self):
        v = (5, 6)
        self.assertEqual(conjugadob(v), (5, -6))

    def test_cartesiano(self):
        u = (3, 5)
        self.assertEqual(cartesiano(u), (0.2614672282, 2.988584094))

    def test_cartesianob(self):
        v = (5, 6)
        self.assertEqual(cartesianob(v), (0.5226423163, 4.972609477))

    def test_polar(self):
        u = (3, 5)
        self.assertEqual(polar(u), (math.sqrt(34), 1.030376827))

    def test_polarb(self):
        v = (5, 6)
        self.assertEqual(polarb(v), (math.sqrt(61), 0.8760580506))

    def test_SumaVec(self):
        v = [(3, 4), (1, 1), (2, 1)]
        u = [(3, 4), (1, 1), (2, 1)]
        self.assertEqual(SumaVec(u, v), ([(6, 8), (2, 2), (4, 2)]))

    def test_InverNCom(self):
        v = [(3,4),(1,1),(2,1)]
        self.assertEqual(InverNCom(v), ([(-3,-4),(-1,-1),(-2,-1)]))

    def test_MultCom(self):
        v = [(3, 4), (1, 1), (2, 1)]
        u = (1, 1)
        self.assertEqual(MultCom(u, v), ([(-1, 7), (0, 2), (1, 3)]))

    def test_SumMat(self):
        v = [[(3, 4), (1, 1), (2, 1)],[(3, 4), (1, 1), (2, 1)],[(3,4),(1,1),(2,1)]]
        u = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(SumMat(u, v), ([[(6, 8), (2, 2), (4, 2)],[(6, 8), (2, 2), (4, 2)], [(6, 8), (2, 2), (4, 2)]]))

    def test_MultEscalar(self):
        u = (5, 6)
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(MultEscalar(u, v), ([[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]))

    def test_conjugadaM(self):
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(conjugadaM(v), ([[(3, -4), (1, -1), (2, -1)], [(3, -4), (1, -1), (2, -1)], [(3, -4), (1, -1), (2, -1)]]))

    def test_TransMat(self):
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(TransMat(v), ([[(3, 4), (3, 4), (3, 4)], [(1, 1), (1, 1), (1, 1)], [(2, 1), (2, 1), (2, 1)]])

    def test_inversamatriz(self):
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(inversamatriz(v), ([[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]))

    def test_AdjuntaMat(self):
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(AdjuntaMat(v), ([[(3, -4), (3, -4), (3, -4)], [(1, -1), (1, -1), (1, -1)], [(2, -1), (2, -1), (2, -1)]]))

    def test_ProdMat(self):
        u = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(ProdMat(u, v), ([[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]))

    def test_accion(self):
        u = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        v = [[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]
        self.assertEqual(accion(u,v), ([[(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)], [(3, 4), (1, 1), (2, 1)]]))

    def test_ProdInterno(self):
        v = [(3, 4), (1, 1), (2, 1)]
        u = [(3, 4), (1, 1), (2, 1)]
        self.assertEqual(ProdInterno(u, v), ([(3, 4), (1, 1), (2, 1)]))

    def test_Norma(self):
        v = [(3, 0), (1, 0), (2, 0)]
        self.assertEqual(Norma(v), (math.sqrt(14)))

    def test_DistanciaVec(self):
        v = [(3, 4), (1, 1), (2, 1)]
        u = [(1, 2), (4, 5), (2, 2)]
        self.assertEqual(DistanciaVec(u, v), (math.sqrt(-7,32)))




if __name__ == '__main__':
    unittest.main()
