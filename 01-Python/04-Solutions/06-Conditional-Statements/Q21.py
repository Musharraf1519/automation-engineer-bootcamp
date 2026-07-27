"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q21
========================================================

Question:

Create a Salary Bonus Calculator.

Input:

- Salary
- Years of Experience

Rules:

- Experience ≥10 years → 20% Bonus
- Experience ≥5 years → 10% Bonus
- Otherwise → No Bonus

Display:

- Bonus
- Final Salary



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

salary = int(input("Enter your Salary: "))
year_of_exp = int(input("Enter Your years of Experience: "))
bonus = 0

if year_of_exp >= 10:
    bonus = 20
elif year_of_exp>= 5:
    bonus = 10

print(f"Your bonus is : {bonus}%")
print(f"Your final salary is : ₹{salary - salary*bonus/100}")