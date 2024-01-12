# Create a program that swaps the values of two variables
# @author - Addie Domanico
# @version - 01/10/2024

# Receive user input for two variables
value1 = input("Enter the first value (number or letter): ")
value2 = input("Enter the second value (number or letter): ")

print("The inital values include: " + value1 + " and " + value2)

# New variable
new = value1
value1 = value2
value2 = new

print("The values swapped are: " + value1 + " and " + value2)

