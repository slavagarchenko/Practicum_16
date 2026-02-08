from itertools import permutations


def get_all_permutations(input_str: str) -> list:
    """
    Get all permutations of a set of natural numbers in lexicographic order.

    Returns:
        list: List of tuples representing all permutations.
    """
    numbers = list(map(int, input_str.split()))

    unique_numbers = sorted(set(numbers))

    return list(permutations(unique_numbers))


try:
    input_str = input("Введите натуральные числа через пробел: ").strip()
    if not input_str:
        print("Ошибка: ввод не может быть пустым!")

    print("=" * 50)
    print(get_all_permutations(input_str))

except ValueError:
    print("Ошибка: все элементы должны быть натуральными числами!")

except Exception as e:
    print(f"Произошла ошибка: {e}")
