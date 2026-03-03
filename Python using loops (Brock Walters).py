# Module 7 Assignment - Python Using Loops
# Brock Walters
# Purpose: Iterate through a list of numbers and print whether each number is odd or even

# List of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
