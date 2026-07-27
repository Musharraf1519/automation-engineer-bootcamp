"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q20
========================================================

Question:

Input:

- Age
- Has Driving License (yes/no)

Display whether the person is eligible to drive.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below



age = int(input("Enter Your age : "))
license_status = input("Has Driving License (Yes/No)")

if age>18 and license_status == 'Yes':
    print("Eligible for Driving")
else:
    print("Not Eligible")
