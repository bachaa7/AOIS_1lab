import unittest
from B_operation import BinaryOperations


class TestBinaryOperations(unittest.TestCase):

    def test_add_complement(self):
        # Тест сложения в дополнительном коде
        result_bin, result_dec = BinaryOperations.add_complement(5, 3)
        self.assertEqual(result_bin, '00001000')  # Ожидаемый двоичный результат
        self.assertEqual(result_dec, 8)  # Ожидаемый десятичный результат

        result_bin, result_dec = BinaryOperations.add_complement(-5, 3)
        self.assertEqual(result_bin, '11111110')  # Ожидаемый двоичный результат
        self.assertEqual(result_dec, -2)  # Ожидаемый десятичный результат

    def test_subtract_complement(self):
        # Тест вычитания с использованием дополнительного кода
        result_bin, result_dec = BinaryOperations.subtract_complement(5, 3)
        self.assertEqual(result_bin, '00000010')  # Ожидаемый двоичный результат (для 2 в десятичной)
        self.assertEqual(result_dec, 2)  # Ожидаемый десятичный результат

        result_bin, result_dec = BinaryOperations.subtract_complement(5, -3)
        self.assertEqual(result_bin, '00001000')  # Ожидаемый двоичный результат (для 8 в десятичной)
        self.assertEqual(result_dec, 8)  # Ожидаемый десятичный результат

    def test_multiply_direct(self):
        # Тест умножения в прямом коде
        result_bin, result_dec = BinaryOperations.multiply_direct(3, 4)
        self.assertEqual(result_bin, '0000000000001100')  # Ожидаемый двоичный результат
        self.assertEqual(result_dec, 12)  # Ожидаемый десятичный результат

    def test_divide_direct(self):
        # Тест деления в прямом коде
        result_bin, result_dec = BinaryOperations.divide_direct(7, 3)
        self.assertEqual(result_bin, '00000010.01010')  # Ожидаемый двоичный результат
        self.assertAlmostEqual(result_dec, 2.3125, places=5)  # Ожидаемый десятичный результат

        result_bin, result_dec = BinaryOperations.divide_direct(7, 0)
        self.assertEqual(result_bin, "Ошибка: деление на ноль")
        self.assertIsNone(result_dec)
