from constans import BITS_DEFAULT
from B_converter import BinaryConverter

class BinaryOperations:
    @staticmethod
    def add_complement(n1, n2, bits=BITS_DEFAULT):
        _, _, comp1 = BinaryConverter.dec_to_bin(n1, bits)
        _, _, comp2 = BinaryConverter.dec_to_bin(n2, bits)
        result = int(comp1, 2) + int(comp2, 2)
        result = result & ((2 ** bits) - 1)
        result_bin = bin(result)[2:].zfill(bits)
        result_value = int(result_bin, 2) - (1 << bits) if result_bin[0] == '1' else int(result_bin, 2)
        return result_bin, result_value

    @staticmethod
    def subtract_complement(n1, n2, bits=BITS_DEFAULT):
        return BinaryOperations.add_complement(n1, -n2, bits)

    @staticmethod
    def multiply_direct(n1, n2, bits=BITS_DEFAULT):
        result = n1 * n2
        result_bin = bin(result & (2 ** (bits * 2) - 1))[2:].zfill(bits * 2)
        return result_bin, result

    @staticmethod
    def divide_direct(n1, n2, bits=BITS_DEFAULT, precision=5):
        if n2 == 0:
            return "Ошибка: деление на ноль", None

        quotient = n1 / n2
        quotient_bin = format(int(quotient), 'b').zfill(bits) + '.'
        frac_part = quotient - int(quotient)

        for _ in range(precision):
            frac_part *= 2
            quotient_bin += '1' if frac_part >= 1 else '0'
            frac_part -= int(frac_part)

        quotient_dec = BinaryConverter.bin_to_dec(quotient_bin)
        return quotient_bin, quotient_dec
