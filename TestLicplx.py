import Libcplx as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_sumacplx1(self):
        self.assertEqual(lc.sumacplx((3.5, 6),(-6.7, 2)), (-3.2,8))

    def test_sumacplx2(self):
        self.assertEqual(lc.sumacplx((8, 6),(7, -2)), (15,4))

    def test_multcplx1(self):
        self.assertEqual(lc.multcplx((3.5, 6),(-6.7, 2)), (-35.45,-33.2))

    def test_multcplx2(self):
        self.assertEqual(lc.multcplx((8, 6),(7, -2)), (68,26))

    def test_restacplx1(self):
        self.assertEqual(lc.restacplx((3.5, 6),(-6.7, 2)), (10.2,4))

    def test_restacplx2(self):
        self.assertEqual(lc.restacplx((8, 6),(7, -2)), (1,8))

    def test_divcplx1(self):
        self.assertEqual(lc.divcplx((3.5, 6),(-6.7, 2)), (-0.2341992227449376,-0.965432603804459))

    def test_divcplx2(self):
        self.assertEqual(lc.divcplx((8, 6),(7, -2)), (0.8301886792452831,1.0943396226415094))

    def test_modulocplx1(self):
        self.assertEqual(lc.modulocplx((3.5, 6)),4.358898943540674)

    def test_modulocplx2(self):
        self.assertEqual(lc.modulocplx((8, 4)),4.898979485566356)

    def test_conjugadocplx1(self):
        self.assertEqual(lc.conjugadocplx((3.5, 6)),(3.5, -6))

    def test_conjugadocplx2(self):
        self.assertEqual(lc.conjugadocplx((8, 4)),(8, -4))

    def test_carte_a_polar1(self):
        self.assertEqual(lc.carte_a_polar((3.5, 6)),(4.358898943540674, 1.042721878368537))

    def test_carte_a_polar2(self):
        self.assertEqual(lc.carte_a_polar((8, 4)),(4.898979485566356, 0.4636476090008061))

    def test_polar_a_carte1(self):
        self.assertEqual(lc.polar_a_carte((3.5, 6)),(3.3605960032762807, -0.9779542436962405))

    def test_polar_a_carte2(self):
        self.assertEqual(lc.polar_a_carte((8, 4)),(-5.2291489669088955, -6.054419962463426))

    def test_retornar_fase1(self):
        self.assertEqual(lc.retornar_fasecplx((3.5, 6)), 1.042721878368537)

    def test_retornar_fase2(self):
        self.assertEqual(lc.retornar_fasecplx((8, 4)), 0.4636476090008061)

if __name__ == '__main__':
    unittest.main()