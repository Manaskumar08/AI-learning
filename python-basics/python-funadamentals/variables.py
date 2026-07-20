definitions = [
    "A variable is a name that refers to an object stored in memory.",
]

# name is the variable.
# "Manas" is the object.
# = assigns the object to the variable.

name = "Manas"
print(name)  # Output: Manas

# 2. Variable Assignment

   # .Assignment means storing a value inside a variable.

age = 22

price = 99.5

name = "John"

is_active = True

print(age)        # Output: 22
print(price)      # Output: 99.5
print(name)       # Output: John
print(is_active)  # Output: True


#3. Multiple Assignments

#Assign multiple variables
a = 10
b = 20
c = 30

print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

#Multiple assignment in one line

x, y, z = 1, 2, 3

print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

#Same value to multiple variables

a = b = c = 100

print(a)  # Output: 100
print(b)  # Output: 100
print(c)  # Output: 100

#Swap variables

a = 5
b = 10

a, b = b, a

print(a)
print(b)


#4. Dynamic Typing

x = 10

print(type(x))  # Output: <class 'int'>

x = "Python"

print(type(x))  # Output: <class 'str'>

#5. Strong Typing

# Python is dynamically typed but strongly typed.

result = "5" + 5
print(result)  # This will raise a TypeError because you cannot concatenate a string and an integer.

#Traceback (most recent call last):
#   File "/home/nav187/Learning/ai_learning/python-basics/python-funadamentals/variables.py", line 82, in <module>
#     result = "5" + 5
# TypeError: can only concatenate str (not "int") to str

result = int("5") + 5
print(result)  # Output: 10