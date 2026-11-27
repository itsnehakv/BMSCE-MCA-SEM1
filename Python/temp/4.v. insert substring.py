try:
    string = input("Enter a string: ")
    sub = input("Enter the substring to insert: ")
    pos = int(input("Enter the position: "))

    if pos < 0 or pos > len(string):
        raise IndexError("Invalid position")

    result = string[:pos] + sub + string[pos:]

    print("String after insertion:", result)

except ValueError:
    print("Enter an integer for position")

except IndexError as e:
    print("Error:", e)