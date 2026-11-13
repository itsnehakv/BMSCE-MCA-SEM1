while True:

    try:

        amount=int(input("Enter amount to be withdrawn:"))

        if (amount>=0):

            hun_notes=(amount//100)

            amount-=(hun_notes\*100)



            fif_notes=(amount//50)

            amount-=(fif_notes\*50)



            ten_notes=(amount//10)

            amount-=(ten_notes\*10)





            print("Notes of 100:",hun_notes,"Notes of 50:",fif_notes, "Notes of 10:",ten_notes,"Remaining amount:",amount)





    except ValueError:

        print("The number entered is invalid")
