def fib(n):
    if (n==0 or n==1):
        return 1

    x=fib(n-1)
    y=fib(n-2)

    return (x+y)


num=int(input("Enter number to find it's fibonacci sequence:"))
for i in range(num+1):
    print(f"{fib(i)}",end="\t")
