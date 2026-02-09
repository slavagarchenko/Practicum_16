def faculties_number(set_faculties: set) -> int:
    """
    Calculate and return the number of unique faculties.

    Args:
        set_faculties (set): A set containing faculty names.

    Returns:
        int: The count of unique faculties in the set.
    """
    return (len(set_faculties))


def main():
    """
    Main function.
    """
    try:
        set_faculties = set()
        student_number = int(input("Введите число студентов: "))

        while student_number <= 0:
            print("Введите корректное число студентов")
            student_number = int(input("Введите число студентов: "))

        for i in range(student_number):
            faculty = input(f"Введите название факультатива для {i+1}-ого"
                            " студента: ").strip()

            while faculty == "":
                print("Введите корректное название курса")
                faculty = input(f"Введите название факультатива для {i+1}-ого"
                                " студента: ")

            set_faculties.add(faculty)

        print("Количество уникальных курсов: ",
              faculties_number(set_faculties))

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")


if __name__ == "__main__":
    main()
