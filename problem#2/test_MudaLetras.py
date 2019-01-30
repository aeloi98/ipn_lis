import sys
import unittest
from MudaLetras import MudaLetras

class TestMethod(unittest.TestCase):

    def test_Multiplo(self):
        self.assertEqual(MudaLetras('hello*3'),'Ifmmp*3')
        self.assertEqual(MudaLetras('fun times!'),'gvO Ujnft!')
        self.assertEqual(MudaLetras('a'),'b')
        self.assertEqual(MudaLetras('d'),'E')
        self.assertEqual(MudaLetras('z'),'A')
        self.assertEqual(MudaLetras('Z'),'A')
        self.assertEqual(MudaLetras('!&/=(a'),'!&/=(b')
        self.assertEqual(MudaLetras('-1'),-1)
        self.assertEqual(MudaLetras(-1),-1)
        self.assertEqual(MudaLetras(10),10)
        
        
       

if __name__ == '__main__':
    unittest.main()