"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q28
========================================================

Question:

Input:

- Product Price
- Membership Status (yes/no)

Rules:

- Members receive 15% discount.
- Non-members receive no discount.

Display the final bill.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

price = int(input("Enter price of your product: "))
membership_status = input("Enter your membership status : (Yes/No) ")


if membership_status == 'Yes':
    print(f"Your final Price is: {price*0.85}")
else: 
    print(f"Your final Price is: {price}")

