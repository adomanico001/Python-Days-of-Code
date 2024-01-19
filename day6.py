# Write a program to count the occurrences of a specific character in a string.

# @author - Addie Domanico
# @version - 01/15/2024

def countChar(input_str, char_to_count):
    count = 0
    for char in input_str:
        if char == char_to_count:
                count += 1
    return count

user_input = input("Enter a short sentence: ")
char_to_count = input("Enter a specific character to count: ")

result = countChar(user_input, char_to_count)
print(f"The character '{char_to_count}' appears {result} times in the sentence.")
