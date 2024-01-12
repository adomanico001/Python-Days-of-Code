# @author - Addie Domanico
# @version - 01/11/2024

# Create a program to calculate the area of a circle given its radius.

# Import pi constant
from math import pi


while True:
    # Prompt the user to input the radius of the circle
    radius = input("Enter the radius of the circle: ")
    
    try:
        radius = int(radius)
        break
    # Checks if input is a valid number
    except ValueError:
        print("This is not a number. Please enter a valid number.")

# Calculate the area of the circle
area = pi * radius ** 2

# Calculated result
print("The area of the circle with radius", radius, "is:", area)
