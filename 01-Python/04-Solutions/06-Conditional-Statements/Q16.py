"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q16
========================================================

Question:

Input a character.

Check whether it is a vowel or consonant.



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

input_char = input("Enter your character: ")

if input_char =='a' or input_char =='e' or input_char =='i' or input_char =='o' or input_char =='u':
    print(f"{input_char} is a vowel.")
elif input_char =='A' or input_char =='E' or input_char =='I' or input_char =='O' or input_char =='U':
    print(f"{input_char} is a vowel.")
else:
    print(f"{input_char} is not a vowel.")




