def number_in_two(first_set: set, second_set: set, number: int) -> bool:
    """
    Check if a number belongs to both sets (intersection).

    Args:
        first_set (set): First set of integers.
        second_set (set): Second set of integers.
        number (int): Number to check.

    Returns:
        bool: True if number is in both sets, False otherwise.
    """
    intersection_set = first_set.intersection(second_set)

    return number in intersection_set


try:
    numbers_str = input("Введите числа для первого множества через пробел: ")
    first_set = set(map(int, numbers_str.split()))

    numbers_str = input("Введите числа для второго множества через пробел: ")
    second_set = set(map(int, numbers_str.split()))

    number = int(input("Введите число для проверки: "))

    print(number_in_two(first_set, second_set, number))

except ValueError:
    print("Ошибка ввода! Убедитесь, что введены корректные данные")
