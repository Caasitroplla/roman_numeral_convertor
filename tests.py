import unittest
from convertor import convert_to_integer, convert_to_roman

class TestToInteger(unittest.TestCase):
    def test_I(self):
        self.assertEqual(convert_to_integer('I'), 1)

    def test_V(self):
        self.assertEqual(convert_to_integer('V'), 5)

    def test_X(self):
        self.assertEqual(convert_to_integer('X'), 10)

    def test_L(self):
        self.assertEqual(convert_to_integer('L'), 50)

    def test_C(self):
        self.assertEqual(convert_to_integer('C'), 100)

    def test_combinations(self):
        self.assertEqual(convert_to_integer('IV'), 4)

class TestToRoman(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert_to_roman(1), 'I')

    def test_10(self):
        self.assertEqual(convert_to_roman(10), 'X')

    def test_50(self):
        self.assertEqual(convert_to_roman(50), 'L')

    def test_2(self):
        self.assertEqual(convert_to_roman(2), 'II')
    
   