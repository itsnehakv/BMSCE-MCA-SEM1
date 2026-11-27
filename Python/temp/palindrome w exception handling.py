try:
    string = input("Enter a string: ")

    if string.strip() == "":
        raise ValueError("String cannot be empty or contain only spaces")

    rev = string[::-1]

    if string == rev:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

except ValueError as e:
    print(e)