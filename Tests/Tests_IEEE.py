import unittest
from IEEE754_converter import IEEE754Converter

class TestIEEE754Converter(unittest.TestCase):

    def test_float_to_ieee754(self):
        ieee_binary = IEEE754Converter.float_to_ieee754(5.75)
        self.assertEqual(ieee_binary, '01000000101110000000000000000000')

    def test_ieee754_to_float(self):
        ieee_binary = '01000000101110000000000000000000'
        result = IEEE754Converter.ieee754_to_float(ieee_binary)
        self.assertEqual(result, 5.75)

    def test_sum_floats_ieee754(self):
        result_float, result_binary = IEEE754Converter.sum_floats_ieee754(5.75, 2.25)
        self.assertEqual(result_float, 8.0)
        self.assertEqual(result_binary, '01000001000000000000000000000000')
