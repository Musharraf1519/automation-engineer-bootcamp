"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q21
========================================================

Question:

Create a Student Information program.

Input:

- Name
- Age
- Course
- College
- Percentage

Display all details using formatted output.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
college = input("Enter your college: ")
percentage = float(input("Enter your percentage: "))

print("Student Information")
print("-"*60)
print(f"Name: {name}.")
print(f"Age: {age}.")
print(f"Course: {course}.")
print(f"College: {college}.")
print(f"Percentage: {percentage}%")
print("-"*60)




