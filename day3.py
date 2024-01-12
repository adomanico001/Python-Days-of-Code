# Write a function to count the number of vowels in a given string.

# @author - Addie Domanico
# @version - 1/12/2024

def countVowels(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

# Receive user input
user_input = input("Enter a short sentence: ")

# Call function with user input
result = countVowels(user_input)

print(f"The number of vowels found in '{user_input}' is: {result}")

