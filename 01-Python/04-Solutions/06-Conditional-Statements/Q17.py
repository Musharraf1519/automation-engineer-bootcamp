"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q17
========================================================

Question:
Input a student's percentage.

Display:

- Excellent (90+)
- Very Good (75–89)
- Good (60–74)
- Average (40–59)
- Fail (<40)



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

percent = int(input("Enter Your Percentage : "))

if percent>=90:
    print("Excellent")
elif percent>=75 and percent<90:
    print("Very Good")
elif percent>=60 and percent<=74:
    print("Good")
elif percent>=40 and percent<59:
    print("Average")
else:
    print("Fail")


