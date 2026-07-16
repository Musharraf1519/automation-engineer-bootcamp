"""
=========================================================
Chapter 5 : Input & Output
File      : 05_input_output.py
=========================================================

This file demonstrates the concepts covered in
Chapter 5.

Topics Covered

1. print()
2. input()
3. Reading Strings
4. Reading Integers
5. Reading Floats
6. Type Conversion
7. Formatted Output (f-Strings)
8. Multiple Inputs
9. Real-World Example
"""

print("=" * 60)
print("1. PRINT FUNCTION")
print("=" * 60)

print("Hello World")

print("Welcome to Python")

print(100)

print(10 + 20)

print()

print("=" * 60)
print("2. READING STRING INPUT")
print("=" * 60)

name = input("Enter your name : ")

print(f"Hello {name}")

print(type(name))

print()

print("=" * 60)
print("3. READING INTEGER INPUT")
print("=" * 60)

age = int(input("Enter your age : "))

print(f"Age : {age}")

print(type(age))

print()

print("=" * 60)
print("4. READING FLOAT INPUT")
print("=" * 60)

salary = float(input("Enter your salary : "))

print(f"Salary : {salary}")

print(type(salary))

print()

print("=" * 60)
print("5. TYPE CONVERSION")
print("=" * 60)

number = input("Enter a number : ")

print("Before Conversion")

print(number)

print(type(number))

number = int(number)

print()

print("After Conversion")

print(number)

print(type(number))

print()

print("=" * 60)
print("6. FORMATTED OUTPUT")
print("=" * 60)

city = input("Enter your city : ")

country = input("Enter your country : ")

print()

print(f"City     : {city}")
print(f"Country  : {country}")

print()

print("=" * 60)
print("7. MULTIPLE INPUTS")
print("=" * 60)

first_name = input("First Name : ")

last_name = input("Last Name : ")

email = input("Email : ")

print()

print(f"First Name : {first_name}")
print(f"Last Name  : {last_name}")
print(f"Email      : {email}")

print()

print("=" * 60)
print("8. REAL-WORLD EXAMPLE")
print("=" * 60)

student_name = input("Student Name : ")

student_age = int(input("Student Age : "))

student_course = input("Course : ")

student_marks = float(input("Marks : "))

print()

print("=" * 60)
print("STUDENT INFORMATION")
print("=" * 60)

print(f"Name       : {student_name}")
print(f"Age        : {student_age}")
print(f"Course     : {student_course}")
print(f"Marks      : {student_marks}")

print()

print("Datatypes")

print(f"Name       : {type(student_name)}")
print(f"Age        : {type(student_age)}")
print(f"Course     : {type(student_course)}")
print(f"Marks      : {type(student_marks)}")

print()

print("=" * 60)
print("9. SUMMARY")
print("=" * 60)

print("✔ print()")
print("✔ input()")
print("✔ String Input")
print("✔ Integer Input")
print("✔ Float Input")
print("✔ Type Conversion")
print("✔ Formatted Output")
print("✔ Multiple Inputs")