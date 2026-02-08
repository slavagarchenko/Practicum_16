def num_in_set(set_numbers: set, number: int) -> bool:
    """
    Check if the given number exists in the set of numbers.

    Args:
        set_numbers (set): A set of integers to search in.
        number (int): The number to check for existence in the set.

    Returns:
        bool: True if the number is in the set, False otherwise.
    """
    return number in set_numbers


try:
    numbers_str = input("Введите числа через пробел: ")
    set_numbers = set(map(int, numbers_str.split()))
    number = int(input("Введите число для проверки: "))

    print(num_in_set(set_numbers, number))


except ValueError:
    print("Ошибка ввода! Убедитесь, что введены корректные данные")
