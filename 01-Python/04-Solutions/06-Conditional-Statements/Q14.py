"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q14
========================================================

Question:

Input a person's age.

Display the ticket category:

- Child (<12)
- Adult (12–59)
- Senior Citizen (60+)


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


age = int(input("Enter Your age : "))

if age<12:
    print("Child")
elif age>=12 and age<60:
    print("Adult")
else:
    print("Senior Citizen")