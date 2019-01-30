import sys
import unittest
from Multiplo3_5 import Multiplo3_5

class TestMethod(unittest.TestCase):

    def test_Multiplo(self):
        self.assertEqual(Multiplo3_5(10),23)
        self.assertEqual(Multiplo3_5(15),45)
        self.assertEqual(Multiplo3_5(3),0)
        self.assertEqual(Multiplo3_5(5),3)
        self.assertEqual(Multiplo3_5(22),119)
        self.assertEqual(Multiplo3_5(35),258)
        self.assertEqual(Multiplo3_5('abc'),None)
        self.assertEqual(Multiplo3_5(-1),None)
        self.assertEqual(Multiplo3_5('-1'),None)
        self.assertEqual(Multiplo3_5('10'),23)
        self.assertEqual(Multiplo3_5('abc-1'),None)
        self.assertEqual(Multiplo3_5(0),0)

if __name__ == '__main__':
    unittest.main()