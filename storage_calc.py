# Файл storage_calc.py
# Автор: Трусов Владимир
# Вариант: 22
# Практическое занятие №7

def run_storage_calculator():
    print("\n--- Калькулятор размеров данных ---")

    try:
        bytes_count = int(input("Введите количество байт: "))

        kb = bytes_count / 1024
        mb = bytes_count / (1024 ** 2)

        print("\nРезультаты:")
        print(f"Байты (DEC): {bytes_count}")
        print(f"Байты (BIN): {bin(bytes_count)}")
        print(f"Байты (HEX): {hex(bytes_count)}")
        print(f"Килобайты (KB): {kb}")
        print(f"Мегабайты (MB): {mb}")

    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    run_storage_calculator()