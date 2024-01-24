# Write a program to remove duplicates from a list.

# @author - Addie Domanico
# @version - 01/19/2024

def remove_duplicates(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in user_input.split()]

result = remove_duplicates(input_list)

print("Original list:", input_list)
print("List with any duplicates removed:", result)


