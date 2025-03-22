import unittest
from B_converter import BinaryConverter

class TestBinaryConverter(unittest.TestCase):

    def test_dec_to_bin(self):
        direct, inverse, complement = BinaryConverter.dec_to_bin(5, 8)
        self.assertEqual(direct, '00000101')
        self.assertEqual(inverse, '00000101')
        self.assertEqual(complement, '00000101')

        direct, inverse, complement = BinaryConverter.dec_to_bin(-5, 8)
        self.assertEqual(direct, '10000101')
        self.assertEqual(inverse, '11111010')
        self.assertEqual(complement, '11111011')

    def test_bin_to_dec(self):
        result = BinaryConverter.bin_to_dec('101.101')
        self.assertEqual(result, 5.625)
