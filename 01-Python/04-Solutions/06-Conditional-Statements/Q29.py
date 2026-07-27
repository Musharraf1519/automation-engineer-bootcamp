"""
========================================================
Module   : 01-Python
Chapter  : 06-Conditional-Statements
Question : Q29
========================================================

Question:

Create a Loan Eligibility Checker.

Input:

- Monthly Salary
- Years of Experience
- Credit Score

Eligible only if:

- Salary ≥ ₹40000
- Experience ≥2 years
- Credit Score ≥700

Display the result.

--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below


monthly_salary = int(input("Enter your monthly salary: "))
years_of_experience = int(input("Enter your years of experience: "))
credit_score = int(input("Enter your credit score: "))

if monthly_salary>=40000 and years_of_experience >=2 and credit_score>=700:
    print("Eligible for loan. ")
else:
    print("Not Eligible for loan.")