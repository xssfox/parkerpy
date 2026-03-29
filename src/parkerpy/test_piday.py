import unittest
import math


class PiDayTestCase(unittest.TestCase):

    def test_2026(self):
        from . import piday_2026
        self.assertEqual(math.pi, 3.2265927137573907)
    
    def test_2025(self):
        from . import piday_2025
        self.assertEqual(math.pi, 3.125)

    def test_2024(self):
        from . import piday_2024
        self.assertEqual(math.pi, 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223176)

    def test_2023(self):
        from . import piday_2023
        self.assertEqual(math.pi, 3.117)

    def test_2022(self):
        from . import piday_2022
        self.assertEqual(math.pi, 3.14159265358979523)

    def test_2021(self):
        from . import piday_2021
        self.assertEqual(math.pi, 3.875)

    def test_2020(self):
        from . import piday_2020
        self.assertEqual(math.pi, 3.141592653589793238462)

    def test_2019(self):
        from . import piday_2019
        self.assertEqual(math.pi, 3.11791)

    def test_2018(self):
        from . import piday_2018
        self.assertEqual(math.pi, 3.141592)

    def test_2018_first_term(self):
        from . import piday_2018_first_term
        self.assertEqual(math.pi, 3.1415927)

    def test_2017(self):
        from . import piday_2017
        self.assertEqual(math.pi, 3.052338478336799 )

    def test_2016(self):
        from . import piday_2016
        self.assertEqual(math.pi, 3.04)

    def test_2015(self):
        from . import piday_2015
        self.assertEqual(math.pi, 3.128)

    def test_2015_pre(self):
        from . import pre_piday_2015
        self.assertEqual(math.pi, 3.1512)

    def test_2013(self):
        from . import piday_2013
        self.assertEqual(math.pi, 3.13834)


if __name__ == '__main__':
    unittest.main()