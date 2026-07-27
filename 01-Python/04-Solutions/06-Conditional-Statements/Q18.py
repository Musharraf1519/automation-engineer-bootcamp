"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q18
========================================================

Question:

Input:

- Username
- Password

Display whether login is successful.

Use:

Username: `admin`

Password: `python123`



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below
username = input("Enter Your Username ")
password = input("Enter Your Password ")

if username == 'admin' and password == 'python123':
    print("Login Successfull")
else:
    print("Incorrect username or password")




