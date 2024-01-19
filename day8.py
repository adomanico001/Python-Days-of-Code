# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# @author - Addie Domanico
# @version - 01/17/2024

def count_letters(input_str):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdeffghijklmnopqrstuvwxyz"
    
    uppercase_count = 0
    lowercase_count = 0
    
    for char in input_str:
        if char in uppercase_letters:
            uppercase_count += 1
        elif char in lowercase_letters:
            lowercase_count += 1

    return uppercase_count, lowercase_count

user_input = input("Enter 1-2 short sentences: ")
uppercase, lowercase = count_letters(user_input)

print(f"The number of uppercase letters in your sentence(s) is: {uppercase}")
print(f"The number of lowercase letters in your sentence(s) is: {lowercase}")
