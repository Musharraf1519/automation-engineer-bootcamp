"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q18
========================================================

Question:

Input:

- Product Name
- Product Price

Display the product details.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

product_name = input("Enter your product name: ")
price = int(input("Enter your price for the product: "))


print("Product Details")
print("-"*60)
print(f"Product Name: {product_name}.")
print(f"Price: {price}.")
print("-"*60)


