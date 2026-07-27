"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q15
========================================================

Question:

Input a year.

Check whether it is a leap year.

*(Hint: A leap year is divisible by 4, except century years which must also be divisible by 400.)*



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

year = int(input("Enter Year to be checked : "))

if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap year")
else:
    print("Not a Leap Year")



