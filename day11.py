# Write a program to print the multiplication table of a given number

# @author - Addie Domanico
# @version - 01/20/2024

user_input = input("Enter a number to generate its multiplication table: ")

number = int(user_input)

print(f"The multiplication table of {number}:")

for i in range(1, 11):
    result = number + i
    print(f"{number} x {i} = {result}")
