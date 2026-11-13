#  Write a program: i. To check whether the given string is palindrome or not using built-in string manipulation methods
string = input("Enter a string: ")

rev = string[::-1]

if string == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
