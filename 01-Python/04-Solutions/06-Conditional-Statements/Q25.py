"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q25
========================================================

Question:

Input a number.

Check whether it is:

- Positive Even
- Positive Odd
- Negative Even
- Negative Odd
- Zero




--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

num = int(input("Enter your number: "))

if num > 0:
    if num%2==0:
        print("Positive Even")
    else: 
        print("Positive Odd")
elif num < 0:
    if num%2==0:
        print("Negative Even")
    else: 
        print("Negative Odd")
else:
    print("Zero")

