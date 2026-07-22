"""
=========================================================
                PYTHON FUNDAMENTALS - VARIABLES
=========================================================

Topics
------
1. What is a Variable?
2. Variable Assignment
3. Multiple Assignment
4. Dynamic Typing
5. Strong Typing
6. Variable Naming Rules
7. Reserved Keywords
8. Naming Conventions (PEP 8)
9. Variables are References
10. Memory References (id)
11. type()
12. Mutable vs Immutable
13. PEP 8 Summary

Author: Manas
=========================================================
"""

# =========================================================
# 1. What is a Variable?
# =========================================================
"""
Definition
----------
A variable is a name that refers to an object stored in memory.
"""

name = "Manas"
print(name)

# =========================================================
# 2. Variable Assignment
# =========================================================
"""
Assignment means storing a value inside a variable.

Syntax:
variable_name = value
"""
age = 22
price = 99.5
name = "John"
is_active = True

print(age)
print(price)
print(name)
print(is_active)

# =========================================================
# 3. Multiple Assignment
# =========================================================
a, b, c = 10, 20, 30
print(a, b, c)

x, y, z = 1, 2, 3
print(x, y, z)

p = q = r = 100
print(p, q, r)

a = 5
b = 10
a, b = b, a
print(a, b)

# =========================================================
# 4. Dynamic Typing
# =========================================================
"""
Python is dynamically typed.
A variable can reference objects of different types.
"""
x = 10
print(type(x))

x = "Python"
print(type(x))

# =========================================================
# 5. Strong Typing
# =========================================================
"""
Python does not automatically mix incompatible types.
"""
result = int("5") + 5
print(result)

# =========================================================
# 6. Variable Naming Rules
# =========================================================
"""
Rules
-----
* Letters, digits and underscore allowed.
* Cannot start with a digit.
* Cannot contain spaces.
* Cannot use Python keywords.
"""
student_name = "John"
_price = 500
salary2025 = 1000

# =========================================================
# 7. Reserved Keywords
# =========================================================
import keyword
print(keyword.kwlist)

# =========================================================
# 8. Naming Conventions (PEP 8)
# =========================================================
"""
    Variables / Functions : snake_case
    Classes              : PascalCase
    Constants            : UPPER_CASE
"""

MAX_SIZE = 100

class StudentRecord:
    pass

def calculate_total():
    return 100

# =========================================================
# 9. Variables are References
# =========================================================
a = 100
b = a
print(a, b)

# =========================================================
# 10. Memory References
# =========================================================
"""
id() returns the identity of an object.
"""
name = "Python"
print(id(name))

a = 10
b = 10
print(id(a))
print(id(b))

list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))

# =========================================================
# 11. type()
# =========================================================
print(type(10))
print(type(3.14))
print(type(True))
print(type("Python"))
print(type([1,2]))
print(type((1,2)))
print(type({1,2}))
print(type({"a":1}))

# =========================================================
# 12. Mutable vs Immutable
# =========================================================
"""
Immutable:
int, float, bool, str, tuple, frozenset

Mutable:
list, dict, set
"""

text = "Python"
print(id(text))
text += "3"
print(text)
print(id(text))

numbers = [1,2]
print(id(numbers))
numbers.append(3)
print(numbers)
print(id(numbers))

# =========================================================
# 13. PEP 8 Summary
# =========================================================
"""
✔ 4-space indentation
✔ snake_case for variables/functions
✔ PascalCase for classes
✔ UPPER_CASE for constants
✔ Imports at top
✔ Group imports
✔ Maximum line length ~79 chars
✔ Meaningful names
✔ Spaces around operators
"""

# =========================================================
# Interview Questions
# =========================================================
"""
1. What is a variable?
2. What is variable assignment?
3. What is dynamic typing?
4. What is strong typing?
5. What does id() return?
6. What does type() return?
7. Difference between mutable and immutable objects?
8. Why are variables references?
9. What is PEP 8?
10. Why should we follow PEP 8?
"""