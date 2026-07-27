"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q23
========================================================

Question:

Create a Student Grade System.

Input marks of five subjects.

Calculate percentage.

Display Grade:

- A
- B
- C
- D
- Fail



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

marks_1 = int(input("Enter Marks 1: "))
marks_2 = int(input("Enter Marks 2: "))
marks_3 = int(input("Enter Marks 3: "))
marks_4 = int(input("Enter Marks 4: "))
marks_5 = int(input("Enter Marks 5: "))

percentage = (marks_1+marks_2+marks_3+marks_4+marks_5)/5


if percentage > 90:
    print("A")
elif percentage <= 90 and percentage > 74:
    print("B")
elif percentage >=75 and percentage > 60:
    print("C")
elif percentage >=60 and percentage > 40:
    print("D")
else:
    print("Fail")