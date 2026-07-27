"""
=========================================================
Chapter 6 : Conditional Statements
File      : 06_conditional_statements.py
=========================================================

This file demonstrates the concepts covered in
Chapter 6.

Topics Covered

1. if Statement
2. if...else Statement
3. if...elif...else Statement
4. Nested if
5. Logical Operators
6. Multiple Conditions
7. Real-World Examples
"""

print("=" * 60)
print("1. IF STATEMENT")
print("=" * 60)

age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote.")

print()

print("=" * 60)
print("2. IF...ELSE STATEMENT")
print("=" * 60)

age = int(input("Enter your age : "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

print()

print("=" * 60)
print("3. IF...ELIF...ELSE")
print("=" * 60)

marks = float(input("Enter your marks : "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")

print()

print("=" * 60)
print("4. NESTED IF")
print("=" * 60)

age = int(input("Enter your age : "))
has_license = input("Do you have a driving license (yes/no) : ")

if age >= 18:

    if has_license.lower() == "yes":
        print("You are allowed to drive.")

    else:
        print("You need a driving license.")

else:
    print("You are underage.")

print()

print("=" * 60)
print("5. LOGICAL OPERATORS")
print("=" * 60)

age = int(input("Enter your age : "))
citizen = input("Are you an Indian citizen? (yes/no) : ")

if age >= 18 and citizen.lower() == "yes":
    print("Eligible to Vote")

else:
    print("Not Eligible")

print()

print("=" * 60)
print("6. MULTIPLE CONDITIONS")
print("=" * 60)

username = input("Username : ")
password = input("Password : ")

if username == "admin" and password == "admin123":
    print("Login Successful")

else:
    print("Invalid Credentials")

print()

print("=" * 60)
print("7. REAL-WORLD EXAMPLE")
print("=" * 60)

salary = float(input("Enter Monthly Salary : "))
experience = int(input("Years of Experience : "))

if salary >= 50000 and experience >= 5:
    print("Eligible for Senior Position")

elif salary >= 30000:
    print("Eligible for Mid-Level Position")

else:
    print("Eligible for Entry-Level Position")

print()

print("=" * 60)
print("8. SUMMARY")
print("=" * 60)

print("✔ if Statement")
print("✔ if...else Statement")
print("✔ if...elif...else Statement")
print("✔ Nested if")
print("✔ Logical Operators")
print("✔ Multiple Conditions")