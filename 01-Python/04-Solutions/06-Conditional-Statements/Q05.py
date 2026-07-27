"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q05
========================================================

Question:

Input two numbers.

Display the greater number.




--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

if num1>num2:
    print(f"Greater of {num1} and {num2} is: {num1}")
else:
    print(f"Greater of {num1} and {num2} is: {num2}")


