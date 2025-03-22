import struct
from constans import IEEE754_TOTAL_BITS, IEEE754_EXPONENT_BITS, IEEE754_MANTISSA_BITS

class IEEE754Converter:
    @staticmethod
    def float_to_ieee754(num):
        return format(struct.unpack('!I', struct.pack('!f', num))[0], f'0{IEEE754_TOTAL_BITS}b')

    @staticmethod
    def ieee754_to_float(ieee_binary):
        return struct.unpack('!f', struct.pack('!I', int(ieee_binary, 2)))[0]

    @staticmethod
    def sum_floats_ieee754(first_float, second_float):
        first_binary = IEEE754Converter.float_to_ieee754(first_float)
        second_binary = IEEE754Converter.float_to_ieee754(second_float)

        first_exponent = int(first_binary[1:1 + IEEE754_EXPONENT_BITS], 2)
        first_mantissa = int(first_binary[1 + IEEE754_EXPONENT_BITS:], 2) | (1 << IEEE754_MANTISSA_BITS)

        second_exponent = int(second_binary[1:1 + IEEE754_EXPONENT_BITS], 2)
        second_mantissa = int(second_binary[1 + IEEE754_EXPONENT_BITS:], 2) | (1 << IEEE754_MANTISSA_BITS)

        if first_exponent > second_exponent:
            second_mantissa >>= (first_exponent - second_exponent)
            exponent = first_exponent
        else:
            first_mantissa >>= (second_exponent - first_exponent)
            exponent = second_exponent

        result_mantissa = first_mantissa + second_mantissa

        if result_mantissa & (1 << (IEEE754_MANTISSA_BITS + 1)):
            result_mantissa >>= 1
            exponent += 1

        result_mantissa &= ~(1 << IEEE754_MANTISSA_BITS)

        if exponent >= 255:
            raise OverflowError("Exponent Overflow.")

        result_binary = f"{0:01b}{format(exponent, f'0{IEEE754_EXPONENT_BITS}b')}{format(result_mantissa, f'0{IEEE754_MANTISSA_BITS}b')}"
        result_float = IEEE754Converter.ieee754_to_float(result_binary)

        return result_float, result_binary
