# 3.iii. Generate Fibonacci sequence with n elements

def fib(n):
    a,b=0,1
    for i in range(n):
        print(a, end="\t")

        a,b=b,a+b

try:
    num=int(input("Enter the number of terms: "))

    if num<=0:
        print("Enter a positive integer")
        print("Exiting Program...")
        exit(0)

    fib(num)

except ValueError:
    print("Please enter a postive integer.")


'''
OLD CODE

def fib(n):
    if (n==0 or n==1):
        return 1

    x=fib(n-1)
    y=fib(n-2)

    return (x+y)

try:
    num=int(input("Enter a number to find it's fibonacci sequence:"))
    for i in range(num+1):
        print(f"{fib(i)}",end="\t")

except ValueError:
    print("Please enter an integer value.")
    '''
