import math as m

def isSquare(num): 
    return m.sqrt(num) == int(m.sqrt(num))

def is1Mod4(num): 
    return num%4 == 1

def runNum(num): 
    i1 = 1
    while i1<num:
        if isSquare(i1) and isSquare(num-i1):
            return "is the sum of {0}^2 and {1}^2\n".format(int(m.sqrt(i1)), int(m.sqrt(num-i1)))
        else:
            i1+=1
    return "Either Fermat was wrong or this code is..."

def rightNum(num): 
    if num<1:
        return "is not an integer greater than zero."
    elif m.factorial(num-1)%num == (-1)%num:
        if is1Mod4(num):
            return runNum(num)
        else:
            return "is prime but is not 1 under mod 4"
    else:
        return "is not prime"

if __name__=="__main__":
    num = int(input("Enter a prime integer that is one under mod four and greater than zero: "))
    print(num, rightNum(num))