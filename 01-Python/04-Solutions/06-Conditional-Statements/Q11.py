"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q11
========================================================

Question:
Input marks.

Display:

- Distinction (≥75)
- Pass (40–74)
- Fail (<40)



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

marks = int(input("Enter Your marks: "))

if marks >= 75:
    print("Distinction")
elif marks <=74 and marks>=40:
    print("Pass")
else:
    print("Fail")



