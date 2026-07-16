"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q22
========================================================

Question:
Create an Employee Information program.

Input:

- Employee ID
- Name
- Department
- Salary

Display all details.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below
emp_id = input("Enter your Employee ID: ")
name = input("Enter your Name: ")
department = input("Enter your Deparment: ")
salary = float(input("Enter your Salary: "))

print("Employee Information")
print("-"*60)
print(f"Employee ID  : {emp_id}.")
print(f"Name         : {name}.")
print(f"Department   : {department}.")
print(f"Salary       : ₹ {salary}.")
print("-"*60)




