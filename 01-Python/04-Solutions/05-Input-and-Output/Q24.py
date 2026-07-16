"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q24
========================================================

Question:

Input:

- Price
- GST Percentage

Calculate the final price.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

price = int(input("Enter your product price: "))
gst = int(input("Enter your GST percentage: "))

print(f"Final Price is: ₹ {price + price*gst/100}.")


