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

# Standard operators
result = 5 + 5
print(result)

result = 5 - 5
print(result)

result = 5 * 5
print(result)

result = 5 / 5
print(result)

result = 42 // 4
print(result)

result = 100 % 55 # modulus = remainder
print(result)

result = 2 ** 4
print(result)

age = 25
age = age + 1
age += 1
print(age)

result = ((10 + 5) *2) / 3 - 1
print(result)

# Collect Types
# A list of integers. 
daily_step_count = [10343, 9385, 7029, 10931, 5921]
print(daily_step_count)

# A list of mixed data values. 
employee_data = ["A123", 55024.23, 595, True] 
print(employee_data)

# A list of lists. 
list_of_lists = [["A", "B", "C"], [1, "X", True], [False, 12, 5.5]]
print(list_of_lists)

print(daily_step_count[2])

daily_step_count[4] = 100 
print(daily_step_count) 

# Appends the value 8694 to the end of the list. 
daily_step_count.append(8694) 
print(daily_step_count) 

# Inserts the value 4473 before the current element 3.  
daily_step_count.insert(3, 4473) 
print(daily_step_count) 

# Removes the first occurrence of 7029 from the list. 
daily_step_count.remove(7029) 
print(daily_step_count) 

# Removes the last item from the list.
# captures it into the popped variable. 
popped = daily_step_count.pop() 
print(daily_step_count) 
print(popped)
# output: [10343, 9385, 10931, 5921]

# Sets index_value to the index of the first 4473. 
index_value = daily_step_count.index(4473) 
print(daily_step_count)
print(index_value) 

#index_value = daily_step_count.index(9999) 
#output: an exception occurs because the value 9999 does not exist in the list.


daily_step_count = [10343, 9385, 7029, 10931, 5921, 5921] 

# Sets count to the number of occurrences of 5921. 
count = daily_step_count.count(5921) 
print(count)

daily_step_count = [10343, 9385, 7029, 10931, 5921] 

# Sorts in ascending order.
daily_step_count.sort() 
print(daily_step_count) 

daily_step_count.sort(reverse=True)
print(daily_step_count)

# Reverses the order of the items in the list.
daily_step_count.reverse() 
print(daily_step_count) 

# Slicing
red_river = ['R', 'R', 'C', ' ', 'P', 'o', 'l', 'y', 't', 'e', 'c', 'h', 'n', 'i', 'c'] 

print(red_river[2: 12: 2])

print(red_river[: 10: 1]) 

print(red_river[5: : 3]) 

print(red_river[::5]) 

print(red_river[-1: -5: -1]) 

# Tuples