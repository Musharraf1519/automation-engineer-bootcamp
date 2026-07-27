"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q22
========================================================

Question:

Create a BMI Classification program.

Input:

- Height (meters)
- Weight (kg)

Calculate BMI.

Display:

- Underweight
- Normal
- Overweight
- Obese



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


height =  float(input("Enter your Height in cm: "))
weight = float(input("Enter your Weight in kg: "))

bmi = (weight/ (height**2))*10000

print(bmi)
if bmi > 35 : 
    print("Obese")
elif bmi>25 and bmi <=35:
    print("Overweight")
elif bmi>18.5 and bmi <=25:
    print("Normal")
else: 
    print("Underweight")