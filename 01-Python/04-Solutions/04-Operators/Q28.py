"""
========================================================
Module   : 01-Python
Chapter  : 04-Operators
Question : Q28
========================================================

Question:

Write a program that calculates the total bill.

Store:

- Product Price
- GST
- Discount

Calculate the final payable amount.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

price = 1000
gst = price*18/100
discount = price*10/100


print(f"Total price = {price+gst-discount}")
