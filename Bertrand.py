import math as m

def isPrime(num): 
    return m.factorial(num-1)%num == (-1)%num

def runNum(num): 
    if num<=3:
        return "None because this theorem only works for integers greater than three"
    else:
        primes = []
        i = num+1
        while i < 2*num-2:
            if isPrime(i):
                primes.append(i)
                i+=1
            else:
                i+=1
        return primes

if __name__=="__main__":
    num = int(input("Enter an integer greater than three: "))
    print("Primes that satisfy Bertrand's Postulate for {0}:\n".format(num), runNum(num))
