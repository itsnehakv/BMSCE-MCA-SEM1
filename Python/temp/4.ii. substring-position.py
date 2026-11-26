# 4. ii. Display all positions of a substring in a main string

word = input("Enter the main string: ")
sub = input("Enter the substring: ")

pos = 0

while True:
    pos = word.find(sub, pos)

    if pos == -1:
        break

    print("Substring found at position:", pos)
    pos += 1
    # moves the pos counter ahead to catch other occurances of substring in the word. EG. 'an' in 'banana'
