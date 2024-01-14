# Write a program to find the maximum and minimum values in a list.

# @author - Addie Domanico
# @version - 01/14/2024

def min_max_list(my_list):
    min_value = max_value = my_list[0]

    for num in my_list:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value

user_input = input("Enter a list of numbers separated by spaces: ")
my_list = [int(num) for num in user_input.split()]

max_value, min_value = min_max_list(my_list)

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")
    
