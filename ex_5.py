def prime_less_number(number: int) -> bool:
    """
    Simple implementation of Sieve of Eratosthenes using sets.

    Args:
        number (int): Upper bound 

    Returns:
        set: Set of prime numbers less than upper bound
    """
    if number <= 2:
        return set()

    primes_set = set(range(2, number))

    current = 2
    while current * current < number:
        if current in primes_set:
            multiple = current * current

            while multiple < number:
                primes_set.discard(multiple)
                multiple += current

        current += 1

    return primes_set


def main():
    """
    Main function.
    """
    try:
        number = int(input("Введите натуральное число n: "))

        if number <= 0:
            print("Число должно быть натуральным (n > 0)!")
        elif number <= 2:
            print(f"Простых чисел меньше {number} не существует.")
        else:
            primes = prime_less_number(number)

            if primes:
                sorted_primes = sorted(primes)
                print(f"Простые числа меньше {number}: {sorted_primes}")

            else:
                print("Простых чисел нет")

    except ValueError:
        print("Ошибка: введите целое натуральное число!")


if __name__ == "__main__":
    main()
