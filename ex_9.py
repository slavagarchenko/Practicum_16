from itertools import combinations


def get_k_subsets(input_str: str, k: int) -> list:
    """
    Generate all K-element subsets of a set of natural numbers.

    Args:
        input_str (str): String containing natural numbers separated by spaces.
        k (int): Size of subsets to generate.

    Returns:
        list: List of tuples, where each tuple represents a K-element subset.
    """
    numbers = list(map(int, input_str.split()))
    unique_numbers = sorted(set(numbers))

    return list(combinations(unique_numbers, k))


def main():
    """
    Main function.
    """
    try:
        input_str = input("Введите натуральные числа через пробел: ").strip()

        if not input_str:
            print("Ошибка: ввод не может быть пустым!")
        else:
            k = int(input("Введите K (размер подмножеств): ").strip())

            print("=" * 50)
            print(get_k_subsets(input_str, k))

    except ValueError:
        print("Ошибка: все элементы должны быть натуральными числами!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
