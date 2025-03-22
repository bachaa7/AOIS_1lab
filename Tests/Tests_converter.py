import unittest
from B_converter import BinaryConverter

class TestBinaryConverter(unittest.TestCase):

    def test_dec_to_bin(self):
        # Тест перевода числа в двоичный формат (прямой, обратный, дополнительный коды)
        direct, inverse, complement = BinaryConverter.dec_to_bin(5, 8)
        self.assertEqual(direct, '00000101')  # Ожидаемый прямой код для 5
        self.assertEqual(inverse, '00000101')  # Ожидаемый обратный код для 5
        self.assertEqual(complement, '00000101')  # Ожидаемый дополнительный код для 5

        # Тест для отрицательного числа
        direct, inverse, complement = BinaryConverter.dec_to_bin(-5, 8)
        self.assertEqual(direct, '10000101')  # Ожидаемый прямой код для -5
        self.assertEqual(inverse, '11111010')  # Ожидаемый обратный код для -5
        self.assertEqual(complement, '11111011')  # Ожидаемый дополнительный код для -5

    def test_bin_to_dec(self):
        # Тест перевода двоичного числа в десятичное (с дробной частью)
        result = BinaryConverter.bin_to_dec('101.101')
        self.assertEqual(result, 5.625)  # Ожидаемый десятичный результат
