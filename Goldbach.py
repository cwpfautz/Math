import math as m

def isPrime(num): 
    return m.factorial(num-1)%num == (-1)%num

def rightNum(num):
    if num%2 != 0 or num <=2:
        return False
    else:
        return True

def runNum(num): 
    primes = []
    i = 1
    while i < num:
        if isPrime(i) and isPrime(num - i):
            if primes.__contains__([num - i, i]):
                i += 1
            else:
                primes.append([i, num - i])
            i += 1
        else:
            i += 1
    return primes

if __name__=="__main__":
    num = int(input("Enter an even integer greater than two: "))
    if rightNum(num):
        print("{0} can be expressed as the sum of these {1} pairs of prime numbers:\n{2}".format(num,len(runNum(num)),runNum(num)))
    else:
        print("Is {0} an even integer greater than two? No. No it isn't.".format(num))
