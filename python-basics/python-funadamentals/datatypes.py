"""
Data Types

"""


"""
What is a Data Type?

ans: A Data Type tells Python what kind of value a variable stores.

Example

age = 25

Python knows 25 is an integer.

name = "Manas"

Python knows this is a string.

Every object in Python has a data type.

"""


"""

Why Data Types are Important

Python needs to know

How much memory to allocate
Which operations are allowed
How to store the value
How to compare values

Example

10 + 20

Works.

But

10 + "20"

Produces

TypeError

because Integer and String are different data types.

"""

"""
Python Built-in Data Types
Category	   Data Types
Numeric	       int, float, complex
Boolean	       bool
Text	       str
Sequence	   list, tuple, range
Set	           set, frozenset
Mapping	       dict
Binary	       bytes, bytearray, memoryview
None	       NoneType

There are 15+ built-in types.

"""

"""
1. Integer (int)

Stores whole numbers.

example:
"""
x = 10

y = -100

z = 999999999999999999999999

print(type(x))  # Output: <class 'int'>


a = 10000000000000000000000000000000000

print(a)

"Python integers have arbitrary precision."

"Integer Operations"

a = 10
b = 3

print(a+b)

print(a-b)

print(a*b)

print(a/b)

print(a//b)

print(a%b)

print(a**b)


"""
2. Float

Represents decimal numbers.
"""