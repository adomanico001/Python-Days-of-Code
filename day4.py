# Write a program to find the sum of all elements in a list

# @author - Addie Domanico
# @version - 01/13/2024

sum = 0
user_input = input("Please enter five integers, separated by spaces: ")

user_list = [int(num) for num in user_input.split(' ')]
# Calculate the sum of the elements
for num in user_list:
    sum += num

print("The sum of the elements in the list is:", sum)
