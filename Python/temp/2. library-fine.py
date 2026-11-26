'''
2. A library charges a fine for every book returned late. For the first 5 days, the fine is 50 paisa, for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. 
If the book is returned after 30 days the membership will be cancelled. 
Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message
'''

while True:
    try: 
        no_days=int(input("Enter no. of days you were late by:"))

        if(no_days<=5):
            print("You fine to be paid is 0.50 rupee")

        elif(no_days>=6 and no_days<=10):
            print("You fine to be paid is 1 rupee")

        elif(no_days>10 and no_days<=30):
            print("You fine to be paid is 5 rupees")

        elif(no_days>30):
            print("Your membership is cancelled")

    except ValueError:
        print("Enter a number")
