def runNum(num):
    n = num % 2
    if n==0:
        return num / 2
    else:
        return num * 3 + 1

if __name__=="__main__":
    number = int(input("Enter a number: "))
    while(number!=1):
        number = runNum(number)
        print(number)