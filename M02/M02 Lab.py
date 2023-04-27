"""
Programmer: Noah Ruckman
Title: M02 Lab.py
Summary: Allows the user to enter student names and GPAs. Then checks to see if they made the Honor Roll or Deans List and prints both lists.
Version: 1.0
Last Revision: 3/26/2023
"""
grade_Book = []
deans_List = []
honor_Roll = []

while True:
    last_name = input("Enter a student's last name or ZZZ to quit: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter that student's first name: ")
    GPA = float(input("Enter that student's GPA: "))
    grade_Book.append({"first_name": first_name, "last_name": last_name, "GPA": GPA})

for student in grade_Book:
    if student['GPA'] >= 3.5:
        deans_List.append(f"{student['first_name']} {student['last_name']}")
for student in grade_Book:
    if student['GPA'] >= 3.25 and student['GPA'] < 3.5:
        honor_Roll.append(f"{student['first_name']} {student['last_name']}")
           
print("The following students made the Deans List and Honor Roll: " + ", ".join(deans_List))
print("The following students made the Honor Roll: " + ", ".join(honor_Roll))
