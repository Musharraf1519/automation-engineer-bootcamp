"""
========================================================
Module   : 01-Python
Chapter  : 05-Input-and-Output
Question : Q28
========================================================

Question:
Input five subject marks.

Calculate:

- Total
- Average

Display both values.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

marks_1 = int(input("Enter Subject 1 Marks   : "))
marks_2 = int(input("Enter Subject 2 Marks   : "))
marks_3 = int(input("Enter Subject 3 Marks   : "))
marks_4 = int(input("Enter Subject 4 Marks   : "))
marks_5 = int(input("Enter Subject 5 Marks   : "))

total = marks_1+marks_2+marks_3+marks_4+marks_5

print(f"Total Marks       : {total}")
print(f"Average Marks     : {total/5}")



