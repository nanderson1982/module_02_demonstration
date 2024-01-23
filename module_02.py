"""
Description: Module 2 Demonstration
Author: Nathan Anderson
Date: 2024-01-23
Usage: To demonstrate content from module 2
"""

"""
This is a
mult-line comment.
"""

# This is a single comment

absolute_value = abs(-12)
print('absolute value:', absolute_value)

# embedded functions
print('absolute value:', abs(-12))

print("I am", 25, "years old")
print("I am 25 years old")

print("apples", "oranges", "bananas", sep= ", ")

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

value = 3.14159423423434654645
number = 123

print(f"The value is {value:.4f}.")
print(f"The number is {number:05}.")

print("Hello\nWorld.")

print(type(name))
print(type(value))
print(type(number))

print("Value as an int:", int(value))
print("Number as float:", float(number))

FEDERAL_TAX_RATE = 0.05

# Strings
original_string = "hello, world!"
original_string = original_string.capitalize()
print(original_string)

width = 20
char = '-'

centered_string = original_string.center(width, char)
print(centered_string)

uppercase = original_string.upper()
print(uppercase)

replaced_string = original_string.replace("Hello", "hi")
print(replaced_string)