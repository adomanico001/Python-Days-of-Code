# Write a program to shuffle the elements of a list randomly

# @author - Addie Domanico
# @version - 01/22/2024

import random

print("Get ready to be shuffled!")

user_input = input("Enter a list of elements separated by spaces: ")
input_list = user_input.split()

print("Original list:", input_list)
random.shuffle(input_list)

print("Shuffled list:", input_list)

