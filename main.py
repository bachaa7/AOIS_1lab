from B_converter import BinaryConverter
from B_operation import BinaryOperations
from IEEE754_converter import IEEE754Converter

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Перевести число в двоичный формат")
        print("2. Арифметические операции")
        print("3. Операции IEEE-754 (32 бита)")
        print("4. Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            number = int(input("Введите число для перевода: "))
            bits = int(input("Выберите разрядность (8 или 32): "))

            if bits not in [8, 32]:
                print("Неверная разрядность! Выберите 8 или 32.")
                continue

            direct, inverse, complement = BinaryConverter.dec_to_bin(number, bits)
            print(f"Прямой код: {direct}")
            print(f"Обратный код: {inverse}")
            print(f"Дополнительный код: {complement}")

        elif choice == "2":
            print("\nВыберите арифметическую операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")

            operation = input("Введите номер операции: ")
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите второе число: "))
            bits = 8

            if operation == "1":
                result_bin, result_dec = BinaryOperations.add_complement(n1, n2, bits)
                print(f"Результат (двоичный): {result_bin}")
                print(f"Результат (десятичный): {result_dec}")

            elif operation == "2":
                result_bin, result_dec = BinaryOperations.subtract_complement(n1, n2, bits)
                print(f"Результат (двоичный): {result_bin}")
                print(f"Результат (десятичный): {result_dec}")

            elif operation == "3":
                result_bin, result_dec = BinaryOperations.multiply_direct(n1, n2, bits)
                print(f"Результат (двоичный): {result_bin}")
                print(f"Результат (десятичный): {result_dec}")

            elif operation == "4":
                result_bin, result_dec = BinaryOperations.divide_direct(n1, n2, bits)
                print(f"Результат (двоичный): {result_bin}")
                print(f"Результат (десятичный): {result_dec}")

            else:
                print("Неверный выбор операции!")

        elif choice == "3":
            print("\nОперации с числами в формате IEEE-754 (32 бита):")
            print("1. Перевести число в IEEE-754")
            print("2. Перевести IEEE-754 в число")
            print("3. Сложить два числа IEEE-754")

            ieee_choice = input("Введите номер операции: ")

            if ieee_choice == "1":
                num = float(input("Введите число с плавающей точкой: "))
                ieee_binary = IEEE754Converter.float_to_ieee754(num)
                print(f"IEEE-754 (32 бита): {ieee_binary}")

            elif ieee_choice == "2":
                ieee_binary = input("Введите 32-битное двоичное число IEEE-754: ")
                num = IEEE754Converter.ieee754_to_float(ieee_binary)
                print(f"Десятичное число: {num}")

            elif ieee_choice == "3":
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result, binary_result = IEEE754Converter.sum_floats_ieee754(num1, num2)
                print(f"Результат (десятичный): {result}")
                print(f"Результат (IEEE-754): {binary_result}")

            else:
                print("Неверный выбор!")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
