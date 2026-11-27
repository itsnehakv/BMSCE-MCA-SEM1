total_days=int(input("Enter no. of total working days so far:"))
no_students=int(input("Enter total no. of students:"))

students={}

for _ in range(no_students):
    roll_no=input(f"Enter roll no. of student {_+1}:")

    no_of_days_absent=int(input("Enter no. of days student was absent:"))

    students[roll_no]=no_of_days_absent

print("Students who are not eligible")

for roll_no,no_of_days_absent in students.items():
    stu_absent_perc=round((total_days-no_of_days_absent) / total_days *100)
    if ( stu_absent_perc < 85):
        print(f"Roll Number: {roll_no}")
        print(f"Attendance Percentage: {stu_absent_perc}")
        print("\n")


