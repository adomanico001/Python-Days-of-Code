# Write a program to check if a number is positive, negative, or zero.

# @author - Addie Domanico
# @version - 01/16/2024

def get_integer():
    while True:
        user_input = input("Enter a number: ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input - not a number. Please enter a number.")

def check_number(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"

number = get_integer()
result = check_number(number)
print(f"This number is {result}.")
