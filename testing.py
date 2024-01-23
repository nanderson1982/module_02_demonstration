# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating an empty list to store the squares
squares = []

# Looping through the numbers list
for number in numbers:
    square = number ** 2  # Calculating the square of the current number
    squares.append(square)  # Adding the square to the squares list

# Printing the original numbers and their squares
for i in range(len(numbers)):
    print(f"The square of {numbers[i]} is {squares[i]}")
