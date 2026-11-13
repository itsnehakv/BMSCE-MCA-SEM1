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
