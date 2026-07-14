"""
=========================================================
Chapter 4 : Operators
File      : 04_operators.py
=========================================================

This file demonstrates all operators discussed
in Chapter 4.

Topics Covered

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Operator Precedence
"""

print("=" * 60)
print("1. ARITHMETIC OPERATORS")
print("=" * 60)

a = 20
b = 6

print(f"a = {a}")
print(f"b = {b}")

print()

print(f"Addition (+)             : {a + b}")
print(f"Subtraction (-)          : {a - b}")
print(f"Multiplication (*)       : {a * b}")
print(f"Division (/)             : {a / b}")
print(f"Floor Division (//)      : {a // b}")
print(f"Modulus (%)              : {a % b}")
print(f"Exponentiation (**)      : {a ** b}")

print()


print("=" * 60)
print("2. ASSIGNMENT OPERATORS")
print("=" * 60)

number = 10

print(f"Initial Value            : {number}")

number += 5
print(f"After += 5               : {number}")

number -= 3
print(f"After -= 3               : {number}")

number *= 2
print(f"After *= 2               : {number}")

number /= 4
print(f"After /= 4               : {number}")

number //= 2
print(f"After //= 2              : {number}")

number %= 3
print(f"After %= 3               : {number}")

number **= 2
print(f"After **= 2              : {number}")

print()


print("=" * 60)
print("3. COMPARISON OPERATORS")
print("=" * 60)

x = 15
y = 10

print(f"x = {x}")
print(f"y = {y}")

print()

print(f"x == y                   : {x == y}")
print(f"x != y                   : {x != y}")
print(f"x > y                    : {x > y}")
print(f"x < y                    : {x < y}")
print(f"x >= y                   : {x >= y}")
print(f"x <= y                   : {x <= y}")

print()


print("=" * 60)
print("4. LOGICAL OPERATORS")
print("=" * 60)

is_logged_in = True
is_admin = False

print(f"Logged In                : {is_logged_in}")
print(f"Admin                    : {is_admin}")

print()

print(f"AND                      : {is_logged_in and is_admin}")
print(f"OR                       : {is_logged_in or is_admin}")
print(f"NOT Logged In            : {not is_logged_in}")

print()


print("=" * 60)
print("5. IDENTITY OPERATORS")
print("=" * 60)

list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(f"list1 == list2           : {list1 == list2}")
print(f"list1 is list2           : {list1 is list2}")

print()

print(f"list1 == list3           : {list1 == list3}")
print(f"list1 is list3           : {list1 is list3}")

print()


print("=" * 60)
print("6. MEMBERSHIP OPERATORS")
print("=" * 60)

language = "Python"

numbers = [10, 20, 30, 40]

print(f"'P' in language          : {'P' in language}")
print(f"'Z' in language          : {'Z' in language}")

print()

print(f"20 in numbers            : {20 in numbers}")
print(f"50 in numbers            : {50 in numbers}")

print()

print(f"'Java' not in language   : {'Java' not in language}")

print()


print("=" * 60)
print("7. BITWISE OPERATORS")
print("=" * 60)

m = 5
n = 3

print(f"m = {m}")
print(f"n = {n}")

print()

print(f"m & n                    : {m & n}")
print(f"m | n                    : {m | n}")
print(f"m ^ n                    : {m ^ n}")
print(f"~m                       : {~m}")
print(f"m << 1                   : {m << 1}")
print(f"m >> 1                   : {m >> 1}")

print()


print("=" * 60)
print("8. OPERATOR PRECEDENCE")
print("=" * 60)

print(f"10 + 5 * 2               : {10 + 5 * 2}")

print(f"(10 + 5) * 2             : {(10 + 5) * 2}")

print(f"2 ** 3 + 5               : {2 ** 3 + 5}")

print(f"(2 + 3) * 4              : {(2 + 3) * 4}")

print()


print("=" * 60)
print("9. REAL-WORLD EXAMPLE")
print("=" * 60)

salary = 60000
bonus = 10000
tax = 5000

total_salary = salary + bonus - tax

is_eligible_for_loan = total_salary >= 50000

print(f"Salary                   : ₹{salary}")
print(f"Bonus                    : ₹{bonus}")
print(f"Tax                      : ₹{tax}")
print(f"Net Salary               : ₹{total_salary}")
print(f"Loan Eligible            : {is_eligible_for_loan}")

print()


print("=" * 60)
print("10. SUMMARY")
print("=" * 60)

print("✔ Arithmetic Operators")
print("✔ Assignment Operators")
print("✔ Comparison Operators")
print("✔ Logical Operators")
print("✔ Identity Operators")
print("✔ Membership Operators")
print("✔ Bitwise Operators")
print("✔ Operator Precedence")