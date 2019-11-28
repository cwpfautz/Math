import util


def run_collatz(n):
    """Run the Collatz Conjecture for n"""

    while n != 1:
        if util.is_even(n):
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
        print(n)


if __name__ == '__main__':
    num = util.get_num(lim=0)
    run_collatz(num)
