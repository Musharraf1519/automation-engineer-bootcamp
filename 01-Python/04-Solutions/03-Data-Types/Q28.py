"""
========================================================
Module   : 01-Python
Chapter  : 03-Data-Types
Question : Q28
========================================================

Question:
Explain the difference between:

- None
- Empty String


--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below

# **Difference between `None` and Empty String (`""`)**

# | **None**                                        | **Empty String (`""`)**                                    |
# | ----------------------------------------------- | ---------------------------------------------------------- |
# | Represents the **absence of a value**.          | Represents a **string with zero characters**.              |
# | It is of type `NoneType`.                       | It is of type `str`.                                       |
# | Used when a variable has **no value assigned**. | Used when a variable contains text, but the text is empty. |
# | Written as `None`.                              | Written as `""` or `''`.                                   |

### Example (Python)


name = None
print(name)          # Output: None
print(type(name))    # Output: <class 'NoneType'>


name = ""
print(name)          # Output: (blank line)
print(type(name))    # Output: <class 'str'>


### Key Difference

# * **`None`** means **no value exists**.
# * **`""` (empty string)** means **a value exists, but it contains no characters**.

# **Example:**

# * `middle_name = None` → The middle name is not provided.
# * `middle_name = ""` → The middle name field exists but is intentionally left blank.
