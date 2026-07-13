"""
=========================================================
Chapter 3 : Data Types
File      : 03_data_types.py
=========================================================

This file demonstrates all major built-in data types
covered in Chapter 3.

Topics Covered

1. Integer
2. Float
3. String
4. Boolean
5. Complex
6. NoneType
7. type()
8. Type Conversion
9. Real World Examples
"""

print("=" * 60)
print("1. INTEGER (int)")
print("=" * 60)

age = 25
marks = 98
temperature = -5

print(age)
print(type(age))

print(marks)
print(type(marks))

print(temperature)
print(type(temperature))

print()


print("=" * 60)
print("2. FLOAT (float)")
print("=" * 60)

salary = 65000.75
pi = 3.14159

print(salary)
print(type(salary))

print(pi)
print(type(pi))

print()


print("=" * 60)
print("3. STRING (str)")
print("=" * 60)

name = "Musharraf Khan"
city = "Bangalore"
phone = "9876543210"

print(name)
print(type(name))

print(city)
print(type(city))

print(phone)
print(type(phone))

print()


print("=" * 60)
print("4. BOOLEAN (bool)")
print("=" * 60)

is_student = True
is_employee = False

print(is_student)
print(type(is_student))

print(is_employee)
print(type(is_employee))

print()


print("=" * 60)
print("5. COMPLEX (complex)")
print("=" * 60)

complex_number = 5 + 3j

print(complex_number)
print(type(complex_number))

print()


print("=" * 60)
print("6. NONE (NoneType)")
print("=" * 60)

manager = None

print(manager)
print(type(manager))

print()


print("=" * 60)
print("7. type() FUNCTION")
print("=" * 60)

print(type(10))
print(type(15.8))
print(type("Automation"))
print(type(True))
print(type(5 + 2j))
print(type(None))

print()


print("=" * 60)
print("8. TYPE CONVERSION")
print("=" * 60)

number = "100"

print(number)
print(type(number))

number = int(number)

print(number)
print(type(number))

print()

salary = 45000

print(type(salary))

salary = float(salary)

print(type(salary))

print()

cgpa = 8.75

print(type(cgpa))

cgpa = str(cgpa)

print(type(cgpa))

print()

status = 1

print(type(status))

status = bool(status)

print(status)
print(type(status))

print()


print("=" * 60)
print("9. REAL WORLD EXAMPLES")
print("=" * 60)

employee_name = "John"

employee_age = 28

employee_salary = 75000.50

is_permanent = True

employee_email = "john@email.com"

manager = None

print(f"Name       : {employee_name}")
print(f"Age        : {employee_age}")
print(f"Salary     : {employee_salary}")
print(f"Permanent  : {is_permanent}")
print(f"Email      : {employee_email}")
print(f"Manager    : {manager}")

print()

print("=" * 60)
print("10. SUMMARY")
print("=" * 60)

print("✔ int       -> Whole Numbers")
print("✔ float     -> Decimal Numbers")
print("✔ str       -> Text")
print("✔ bool      -> True / False")
print("✔ complex   -> Complex Numbers")
print("✔ NoneType  -> No Value")
print("✔ type()    -> Checks Datatype")
print("✔ int(), float(), str(), bool() -> Type Conversion")