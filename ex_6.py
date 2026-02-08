def find_solutions() -> None:
    """
    Find all solutions for ХОД + ХОД + ХОД = МАТ
    where different letters represent different digits.
    """
    solutions = []

    for xod in range(100, 1000):
        mat = xod * 3

        if mat < 100 or mat > 999:
            continue

        xod_str = str(xod)
        mat_str = str(mat)

        if len(set(xod_str)) != 3:
            continue

        all_digits = xod_str + mat_str

        if len(set(all_digits)) != 6:
            continue

        solutions.append((xod, mat))

    solutions.sort(key=lambda s: s[0])

    print("Все решения:")
    print("=" * 30)

    for xod, mat in solutions:
        print(f"{xod}+{xod}+{xod}={mat}")
