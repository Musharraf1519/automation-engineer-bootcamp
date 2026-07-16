"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q25
========================================================

Question:
Input your height (in meters) and weight (in kilograms).

Calculate your BMI.

Formula:

```text
BMI = Weight / (Height × Height)


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

print(f"Your BMI is: ₹ {weight/(height **2)}.")


