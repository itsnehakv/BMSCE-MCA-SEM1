#3.i. Check whether the given number is even or odd

try:
    num=int(input("Enter a number:"))

    if num & 1:
        print("Odd")
    else:
        print("Even")

except ValueError:
    print("Please enter an integer value")
