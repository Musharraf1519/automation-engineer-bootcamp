"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q30
========================================================

Question:

Create a User Registration form.

Input:

- Username
- Password
- Email
- Mobile Number
- Country

Display a registration summary.

Do not validate the input. Simply accept the values and display them.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below
user_name = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
country = input("Enter your country: ")

print("="*60)
print("User Information")
print("-"*60)
print(f"Username       : {user_name}.")
print(f"Password        : {password}.")
print(f"Email           : {email}.")
print(f"Phone Number    : {phone}.")
print(f"Country         : {country}.")
print("-"*60)


