"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q24
========================================================

Question:

Input three side lengths.

Determine whether they can form a valid triangle.


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


side_1 = int(input("Enter length of side 1: "))
side_2 = int(input("Enter length of side 2: "))
side_3 = int(input("Enter length of side 3: "))

if side_1 >0 and side_2 >0  and side_3 > 0:
    if side_1+side_2 > side_3:
        print("Triangle is possible. ")
    elif side_3+side_2 > side_1:
        print("Triangle is possible. ")
    elif side_1+side_3 > side_2:
        print("Triangle is possible. ")
else:
    print("Triangle not possible.")
    