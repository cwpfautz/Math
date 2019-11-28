import math as m
import util


def is_prime(n):
    """Determine whether n is prime using Wilson's Theorem"""

    return m.factorial(n - 1) % n == (-1) % n


def display_primality(n):
    """Display the primality of n"""

    if is_prime(n):
        print("{0} is a prime number".format(n))
    else:
        print("{0} is a composite number".format(n))


if __name__ == '__main__':
    num = util.get_num(lim=1)
    display_primality(num)
