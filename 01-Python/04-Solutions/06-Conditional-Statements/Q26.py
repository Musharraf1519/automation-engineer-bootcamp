"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q26
========================================================

Question:

Input:

- Username
- Password
- OTP

Login is successful only if all three are correct.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

username = input("Enter your username: ")
password = input("Enter your password: ")
otp = int(input("OTP "))

if username == 'admin' and password == 'python123' and otp == 123789:
    print("Login Successfull.")
else: 
    print("Wrong Credentials")


