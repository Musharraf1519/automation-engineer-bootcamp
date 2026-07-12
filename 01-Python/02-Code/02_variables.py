"""
=========================================================
Chapter 2 : Variables & Memory
File       : 02_variables.py
=========================================================

This file demonstrates all concepts discussed in
Chapter 2.

Topics Covered

1. Variable Creation
2. Object References
3. Multiple Assignment
4. Same Object Assignment
5. Variable Swapping
6. Dynamic Typing
7. type()
8. id()
9. Naming Conventions
10. Constants
"""

print("=" * 60)
print("1. Variable Creation")
print("=" * 60)

name = "Musharraf"
age = 25
salary = 65000.50
is_employee = True

print(name)
print(age)
print(salary)
print(is_employee)

print()


print("=" * 60)
print("2. Object References")
print("=" * 60)

x = 100
y = x

print(f"x = {x}")
print(f"y = {y}")

print()

print("Memory Address")

print(id(x))
print(id(y))

print()

print("Same Object ?")

print(x is y)

print()


print("=" * 60)
print("3. Multiple Assignment")
print("=" * 60)

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

print()


print("=" * 60)
print("4. Same Value Assignment")
print("=" * 60)

p = q = r = 500

print(p)
print(q)
print(r)

print()

print(id(p))
print(id(q))
print(id(r))

print()


print("=" * 60)
print("5. Variable Swapping")
print("=" * 60)

first = 10
second = 20

print("Before Swap")

print(first)
print(second)

first, second = second, first

print()

print("After Swap")

print(first)
print(second)

print()


print("=" * 60)
print("6. Dynamic Typing")
print("=" * 60)

value = 10

print(value)
print(type(value))

value = "Automation Engineer"

print()

print(value)
print(type(value))

print()


print("=" * 60)
print("7. type() Function")
print("=" * 60)

number = 50
decimal = 45.5
company = "OpenAI"
status = False

print(type(number))
print(type(decimal))
print(type(company))
print(type(status))

print()


print("=" * 60)
print("8. id() Function")
print("=" * 60)

student = "John"

print(student)

print(id(student))

print()


print("=" * 60)
print("9. Variable Naming")
print("=" * 60)

employee_name = "Alice"

employee_salary = 90000

department_name = "Engineering"

print(employee_name)
print(employee_salary)
print(department_name)

print()


print("=" * 60)
print("10. Constants (Convention)")
print("=" * 60)

PI = 3.14159
MAX_RETRY = 5

print(PI)
print(MAX_RETRY)

print()


print("=" * 60)
print("11. Summary")
print("=" * 60)

print("Variables are references.")
print("Everything in Python is an object.")
print("Variables point to objects in memory.")
print("Python is dynamically typed.")
print("Use meaningful variable names.")