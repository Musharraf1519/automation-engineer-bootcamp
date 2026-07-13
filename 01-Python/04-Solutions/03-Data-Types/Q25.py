"""
========================================================
Module   : 01-Python
Chapter  : 03-Data-Types
Question : Q25
========================================================

Question:
Which datatype would you choose for storing the following?

- Aadhaar Number
- PAN Number
- Mobile Number
- Salary
- Percentage
- Is Married

Explain your choices.

--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

# The choice of data type depends on the **kind of data**, not just whether it contains digits. Here's the most appropriate choice for each field:

# | Data               | Recommended Data Type         | Reason                                                                                                                                                             |
# | ------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
# | **Aadhaar Number** | **String (VARCHAR/CHAR)**     | Although it contains 12 digits, it is an identifier, not used for calculations. Storing it as a string preserves leading zeros and prevents arithmetic operations. |
# | **PAN Number**     | **String (VARCHAR/CHAR)**     | A PAN (e.g., `ABCDE1234F`) contains both letters and numbers, so it must be stored as a string.                                                                    |
# | **Mobile Number**  | **String (VARCHAR/CHAR)**     | Mobile numbers are identifiers, not numeric values for calculation. A string also supports country codes (e.g., `+91`) and leading zeros if needed.                |
# | **Salary**         | **Decimal (DECIMAL/NUMERIC)** | Salary may include paise (decimal values), so a fixed-point decimal type ensures accurate financial calculations.                                                  |
# | **Percentage**     | **Float/Double or DECIMAL**   | Percentages can have fractional values (e.g., 87.5%). `DECIMAL` is preferred when precision is important, while `FLOAT` is acceptable for general use.             |
# | **Is Married**     | **Boolean (BOOL/BOOLEAN)**    | This field has only two possible values: `True/False` or `Yes/No`, making a Boolean type ideal.                                                                    |

# ### Summary

# * **Aadhaar Number:** String
# * **PAN Number:** String
# * **Mobile Number:** String
# * **Salary:** Decimal
# * **Percentage:** Float/Decimal
# * **Is Married:** Boolean

# **Key principle:** If a value is an **identifier** (like Aadhaar, PAN, or Mobile Number), store it as a **string**, even if it consists only of digits. If it represents a **quantity** on which calculations are performed (like Salary or Percentage), use an appropriate **numeric** data type. Boolean values are best stored using the **Boolean** data type.
