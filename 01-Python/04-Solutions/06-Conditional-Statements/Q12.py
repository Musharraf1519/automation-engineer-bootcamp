"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q12
========================================================

Question:

Input three numbers.

Display the largest number.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))
num3 = int(input("Enter Third number : "))

if num1>num2 and num1>num3:
    print(f"Greatest of {num1} , {num2} and {num3} is: {num1}")
elif num2>num3:
    print(f"Greatest of {num1} , {num2} and {num3} is: {num2}")
else:
    print(f"Greatest of {num1} , {num2} and {num3} is: {num3}")

