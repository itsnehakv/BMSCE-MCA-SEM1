'''string=input("Enter a sentence:")
count=1

string=string.strip()

for i in string:
    if i == " ":
        count+=1

print(f"No. of words in string: {count}")
'''

string = input("Enter a sentence: ")

print(string.split())
count = len(string.split())


print(f"No. of words in string: {count}")




