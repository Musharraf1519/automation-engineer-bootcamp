Perfect.

Current progress:

```text
Chapter 4

✅ Notes
✅ Reference Code
✅ Exercises
✅ Solution Templates

⬜ Mini Project
⬜ Documentation
⬜ Git Commit
```

Now let's build the project.

---

# Project 03 – Simple Calculator

---

## Folder Structure

```text
01-Python/
└── 05-Projects/
    └── 03-Simple-Calculator/
        ├── README.md
        ├── simple_calculator.py
        ├── sample_output.txt
        └── screenshots/
```

---

# README.md

````markdown
# Simple Calculator

## Objective

Build a command-line calculator that performs basic arithmetic operations using Python operators.

This project reinforces concepts learned in:

- Chapter 2 – Variables & Memory
- Chapter 3 – Data Types
- Chapter 4 – Operators

---

## Problem Statement

Create a command-line calculator that stores two numbers and performs various arithmetic operations on them.

The calculator should display the result of each operation in a well-formatted manner.

---

## Concepts Covered

- Variables
- Data Types
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Operator Precedence
- Formatted Output (f-Strings)

---

## Requirements

Store two numbers in variables.

Perform the following operations:

- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Modulus
- Exponentiation

Also demonstrate:

- +=
- -=
- *=
- /=
- //=
- %=
- **=

Display the result of every operation.

---

## Folder Structure

```text
03-Simple-Calculator/
│
├── README.md
├── simple_calculator.py
├── sample_output.txt
└── screenshots/
```

---

## Expected Output

Refer to `sample_output.txt`.

---

## Learning Outcomes

After completing this project you will understand:

- Arithmetic Operators
- Assignment Operators
- Mathematical Expressions
- Operator Precedence
- Formatted Console Output
````

---

# Project Requirements

Use two variables.

Example

```python
num1 = 25
num2 = 6
```

Perform and display:

```text
Addition

Subtraction

Multiplication

Division

Floor Division

Modulus

Exponentiation
```

---

## Assignment Operators

Demonstrate

```python
+=

-=

*=

/=

//=

%=

**=
```

using another variable.

---

## Comparison Operators

Display

```python
num1 == num2

num1 != num2

num1 > num2

num1 < num2

num1 >= num2

num1 <= num2
```

---

## Operator Precedence

Display the output of:

```python
10 + 5 * 2

(10 + 5) * 2

2 ** 3 + 4

(2 + 3) ** 2
```

---

## Expected Output

```text
============================================================
                 SIMPLE CALCULATOR
============================================================

First Number        : 25
Second Number       : 6

------------------------------------------------------------
Arithmetic Operations
------------------------------------------------------------

Addition            : 31
Subtraction         : 19
Multiplication      : 150
Division            : 4.1666666667
Floor Division      : 4
Modulus             : 1
Exponentiation      : 244140625

------------------------------------------------------------
Assignment Operators
------------------------------------------------------------

Initial Value       : 20

After += 5          : 25
After -= 2          : 23
After *= 2          : 46
After /= 2          : 23.0
After //= 3         : 7.0
After %= 2          : 1.0
After **= 3         : 1.0

------------------------------------------------------------
Comparison Operators
------------------------------------------------------------

25 == 6             : False
25 != 6             : True
25 > 6              : True
25 < 6              : False
25 >= 6             : True
25 <= 6             : False

------------------------------------------------------------
Operator Precedence
------------------------------------------------------------

10 + 5 * 2          : 20
(10 + 5) * 2        : 30
2 ** 3 + 4          : 12
(2 + 3) ** 2        : 25

============================================================
```

---

## Constraints

Do **not** use:

* `input()`
* `if`
* `match`
* Loops
* Functions
* Lists
* Dictionaries
* Classes

Those topics will be covered in later chapters.