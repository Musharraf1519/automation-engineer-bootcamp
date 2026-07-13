"""
========================================================
Module   : 01-Python
Chapter  : 03-Data-Types
Question : Q30
========================================================

Question:
Suppose you are designing an Employee Management System.

Choose an appropriate datatype for each field and justify your choice.

- Employee ID
- Name
- Email
- Phone Number
- Salary
- Date of Joining
- Is Active
- Manager

--------------------------------------------------------
Solution
--------------------------------------------------------
"""


# Write your solution below

# Here is an appropriate choice of data types for an **Employee Management System**:

# | **Field**           | **Recommended Data Type**       | **Justification**                                                                                                                                                                                                                |
# | ------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **Employee ID**     | **Integer (INT)**               | Each employee has a unique numeric ID used for identification and searching. Arithmetic is usually not performed on it, but integers are efficient for indexing. *(If IDs include letters like `EMP101`, use a String instead.)* |
# | **Name**            | **String (VARCHAR/CHAR)**       | Names consist of letters, spaces, and sometimes special characters, so they should be stored as text.                                                                                                                            |
# | **Email**           | **String (VARCHAR)**            | Email addresses contain letters, numbers, and special characters such as `@` and `.`, making a string the appropriate type.                                                                                                      |
# | **Phone Number**    | **String (VARCHAR)**            | Phone numbers are identifiers, not values for calculation. A string also supports country codes (e.g., `+91`) and leading zeros.                                                                                                 |
# | **Salary**          | **Decimal (DECIMAL/NUMERIC)**   | Salary may include decimal values (e.g., `50000.75`), and `DECIMAL` provides accurate financial calculations.                                                                                                                    |
# | **Date of Joining** | **Date (DATE)**                 | Stores calendar dates and allows date-based operations such as calculating years of service.                                                                                                                                     |
# | **Is Active**       | **Boolean (BOOL/BOOLEAN)**      | This field has only two possible values: `True` (active) or `False` (inactive).                                                                                                                                                  |
# | **Manager**         | **Integer (INT) / Foreign Key** | Stores the Employee ID of the employee's manager. This creates a relationship between employees in the database.                                                                                                                 |
