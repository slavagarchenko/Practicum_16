from itertools import combinations


def get_all_subsets(input_str: str) -> list:
    """
    Generate all possible subsets of a set of natural numbers.

    Args:
        input_str (str): String containing natural numbers separated by spaces.

    Returns:
        list: List of tuples, where each tuple represents a subset.
    """
    numbers = list(map(int, input_str.split()))

    unique_numbers = sorted(set(numbers))

    subsets = []

    for r in range(len(unique_numbers) + 1):
        for combo in combinations(unique_numbers, r):
            subsets.append(combo)

    return subsets


try:
    input_str = input("Введите натуральные числа через пробел: ").strip()

    if not input_str:
        print("Ошибка: ввод не может быть пустым!")
    else:
        print("=" * 50)
        print(get_all_subsets(input_str))

except ValueError:
    print("Ошибка: все элементы должны быть натуральными числами!")

except Exception as e:
    print(f"Произошла ошибка: {e}")
