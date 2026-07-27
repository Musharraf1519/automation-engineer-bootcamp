"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q30
========================================================

Question:

Create an ATM Withdrawal Validation program.

Input:

- Account Balance
- Withdrawal Amount

Rules:

- Withdrawal amount must be greater than zero.
- Withdrawal amount must not exceed the account balance.
- Minimum account balance after withdrawal must be ₹1000.

Display an appropriate message.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below
account_balance = int(input("Enter your Account Balance: "))
withdrawal_amount = int(input("Amount to be withdrawn: "))


if withdrawal_amount > 0:
    if withdrawal_amount > account_balance:
        print("Insufficient Balance.")
    elif account_balance - withdrawal_amount <=1000:
        print("Minimum balance should be less than 1000")
    else:
        print("Withdrawal is successful.")


