"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q29
========================================================

Question:
Create a Personal Profile program.

Input:

- Name
- Age
- Occupation
- Country
- Monthly Income

Display all details in a professional format.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


name = input("Enter your name: ")
age = int(input("Enter your age: "))
occupation = input("Enter your occupation: ")
country = input("Enter your country: ")
monthly_income = int(input("Enter Your Monthly Salary: "))

print("="*60)
print("Personal Information")
print("-"*60)
print(f"Name           : {name}.")
print(f"Age            : {age}.")
print(f"Occupation     : {occupation}.")
print(f"Country        : {country}.")
print(f"Monthly Income : {monthly_income}.")
print("-"*60)

