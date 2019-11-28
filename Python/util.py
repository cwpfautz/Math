def get_num(lim):
    """Get an integer from the user and verify that it is greater than lim"""

    number = int(input("Please enter an integer greater than {0}: ".format(lim)))

    while number <= lim:
        number = int(input("Please enter an integer greater than {0}: ".format(lim)))

    return number


def display_list(list_):
    """Print each element in a given list on a new line"""

    for l in list_:
        print(l)


def is_even(num):
    """Determine whether num is even"""

    return num % 2 == 0
