from constans import BITS_DEFAULT

class BinaryConverter:
    @staticmethod
    def dec_to_bin(n, bits=BITS_DEFAULT):
        min_val = -(2 ** (bits - 1))
        max_val = 2 ** (bits - 1) - 1

        if not (min_val <= n <= max_val):
            raise ValueError(f"Число {n} выходит за допустимый диапазон для {bits} битов!")

        # Прямой код
        if n >= 0:
            direct_code = BinaryConverter.int_to_binary(n, bits)
            inverse_code = direct_code
            complement_code = direct_code
        else:
            abs_n = abs(n)
            direct_code = '1' + BinaryConverter.int_to_binary(abs_n, bits - 1)
            inverse_code = '1' + ''.join('1' if b == '0' else '0' for b in direct_code[1:])
            complement_code = BinaryConverter.add_one(inverse_code)

        return direct_code, inverse_code, complement_code

    @staticmethod
    def int_to_binary(n, bits):
        binary_str = ''
        for _ in range(bits):
            binary_str = str(n % 2) + binary_str
            n //= 2

        return binary_str.zfill(bits)

    @staticmethod
    def add_one(binary_str):
        binary_list = list(binary_str)
        carry = 1

        for i in range(len(binary_list) - 1, -1, -1):
            if binary_list[i] == '0':
                binary_list[i] = '1'
                carry = 0
                break
            else:
                binary_list[i] = '0'

        return ''.join(binary_list)

    @staticmethod
    def bin_to_dec(binary_str):
        if '.' in binary_str:
            int_part, frac_part = binary_str.split('.')
        else:
            int_part, frac_part = binary_str, ''

        decimal_value = int(int_part, 2)
        frac_value = sum(int(bit) * (2 ** -i) for i, bit in enumerate(frac_part, start=1))

        return decimal_value + frac_value
