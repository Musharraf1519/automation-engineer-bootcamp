"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q27
========================================================

Question:

Create a Movie Ticket Eligibility program.

Input:

- Age

Display ticket type:

- Kids
- Adult
- Senior Citizen

Also display ticket price:

- Kids → ₹100
- Adult → ₹200
- Senior Citizen → ₹120





--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

age = int(input("Enter your age: "))
if age<= 12:
    print("You are in Kids category. And your ticket price is : ₹100")
if age>12  and age<60:
    print("You are in Adult category. And your ticket price is : ₹200")
else: 
    print("You are in Adult category. And your ticket price is : ₹120")