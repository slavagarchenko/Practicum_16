def different_favourites(set_favourites: set, friend_favourite: set) -> set:
    """
    Return products that are liked only by Sladkoejkin.

    Args:
        set_favourites (set): Set of products liked by Sladkoejkin.
        friend_favourite (set): Set of products liked by a friend.

    Returns:
        set: Set of products liked only by Sladkoejkin after 
             comparing with friend.
    """
    return set_favourites.difference(friend_favourite)


def main():
    """
    Main function.
    """
    try:
        str_favourites = input(
            "Введите то, что нравится Сладкоежкину: ").strip()
        set_favourites = set(str_favourites.split())
        number_friends = int(input("Введите число друзей: "))

        while number_friends < 0:
            print("Введите корректное число друзей")
            number_friends = int(input("Введите число друзей: "))

        for i in range(number_friends):
            friend_favourite = input("Введите предпочтение для "
                                     f"{i+1}-ого друга: ").strip()
            friend_favourite = set(friend_favourite.split())

            set_favourites = different_favourites(
                set_favourites, friend_favourite)

            if not set_favourites:
                break

        print(f"Количество различных препочтений: {len(set_favourites)}")

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")


if __name__ == "__main__":
    main()
