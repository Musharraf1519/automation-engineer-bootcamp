"""
========================================================
Module   : 01-Python
Chapter  : 03-Data-Types
Question : Q24
========================================================

Question:
Write a program that converts:

- int → float
- float → str
- str → int
- int → bool

Display the datatype after every conversion.

--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below
# int → float
num = 25
float_num = float(num)
print("int → float:", float_num)
print("Datatype:", type(float_num))

# float → str
decimal = 45.75
str_decimal = str(decimal)
print("\nfloat → str:", str_decimal)
print("Datatype:", type(str_decimal))

# str → int
text = "100"
int_text = int(text)
print("\nstr → int:", int_text)
print("Datatype:", type(int_text))

# int → bool
number = 1
bool_number = bool(number)
print("\nint → bool:", bool_number)
print("Datatype:", type(bool_number))

