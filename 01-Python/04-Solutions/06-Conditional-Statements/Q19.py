"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q19
========================================================

Question:
Input purchase amount.

If the amount is ₹5000 or more, give a 10% discount.

Otherwise, no discount.

Display the final amount.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


amount = int(input("Enter your Amount: "))

if amount >= 5000:
    print(f"Final Amount is {0.9*amount}")
else:
    print(f"No discount. You final bill is : {amount}.")
    

