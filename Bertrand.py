import util
import Wilson


def find_primes(n):
    """Find and return a list of all primes between n and 2n-2"""

    primes = []  # List of prime numbers

    for i in range(n + 1, 2 * n - 2):
        if Wilson.is_prime(i):
            primes.append(i)

    return primes


if __name__ == '__main__':
    num = util.get_num(lim=3)
    print("Primes between {0} and {1}:".format(num, 2 * num - 2))
    util.display_list(find_primes(num))
