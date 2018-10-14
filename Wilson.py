def factorial(num):
    fact = 1
    for i in range(num):
        fact = fact*(i+1)
    return fact

def isPrime(num): 
    if num<1:
        return "is not an integer greater than zero."
    elif factorial(num-1)%num == (-1)%num:
        return "is prime"
    else:
        return "is not prime"

if __name__=="__main__":
    num = int(input("Enter an integer greater than zero: "))
    print(num, isPrime(num))
