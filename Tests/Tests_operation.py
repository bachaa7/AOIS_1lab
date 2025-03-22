import unittest
from B_operation import BinaryOperations


class TestBinaryOperations(unittest.TestCase):

    def test_add_complement(self):
        result_bin, result_dec = BinaryOperations.add_complement(5, 3)
        self.assertEqual(result_bin, '00001000')
        self.assertEqual(result_dec, 8)

        result_bin, result_dec = BinaryOperations.add_complement(-5, 3)
        self.assertEqual(result_bin, '11111110')
        self.assertEqual(result_dec, -2)

    def test_subtract_complement(self):
        result_bin, result_dec = BinaryOperations.subtract_complement(5, 3)
        self.assertEqual(result_bin, '00000010')
        self.assertEqual(result_dec, 2)

        result_bin, result_dec = BinaryOperations.subtract_complement(5, -3)
        self.assertEqual(result_bin, '00001000')
        self.assertEqual(result_dec, 8)

    def test_multiply_direct(self):
        result_bin, result_dec = BinaryOperations.multiply_direct(3, 4)
        self.assertEqual(result_bin, '0000000000001100')
        self.assertEqual(result_dec, 12)

    def test_divide_direct(self):
        result_bin, result_dec = BinaryOperations.divide_direct(7, 3)
        self.assertEqual(result_bin, '00000010.01010')
        self.assertAlmostEqual(result_dec, 2.3125, places=5)

        result_bin, result_dec = BinaryOperations.divide_direct(7, 0)
        self.assertEqual(result_bin, "Ошибка: деление на ноль")
        self.assertIsNone(result_dec)
