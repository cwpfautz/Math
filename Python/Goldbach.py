import util
import Wilson


def find_sums(n):
    """Find and return a list of sets of primes that sum to n"""

    sums = []  # Sets of primes that sum to n

    for i in range(1, n):
        if Wilson.is_prime(i) and Wilson.is_prime(n - i):
            if [n - i, i] not in sums:
                sums.append([i, n - i])

    return sums


if __name__ == '__main__':
    num = util.get_num(lim=2)
    print("{0} can be expressed as:".format(num))
    for sum_ in find_sums(num):
        print("{0} + {1}".format(sum_[0], sum_[1]))
