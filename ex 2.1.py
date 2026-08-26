# Student Scorecard Program

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n" + "=" * 35)
print("         STUDENT SCORECARD")
print("=" * 35)
print(f"Student Name : {name}")
print(f"Subject 1    : {marks1}")
print(f"Subject 2    : {marks2}")
print(f"Subject 3    : {marks3}")
print(f"Total Marks  : {total}")
print(f"Average      : {average:.2f}")
print("=" * 35)