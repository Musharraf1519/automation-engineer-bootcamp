"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q27
========================================================

Question:

Input:

- Name
- Email
- Phone Number
- City

Display the information inside a well-formatted report.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
city = input("Enter your city: ")

print("="*60)
print("Personal Information")
print("-"*60)
print(f"Name         : {name}.")
print(f"Email        : {email}.")
print(f"Phone Number : {phone}.")
print(f"City         : {city}.")
print("-"*60)




