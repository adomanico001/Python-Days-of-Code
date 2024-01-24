# Write a program to check if a number is even or odd

# @author - Addie Domanico
# @version - 01/18/2024

while True:
    user_input = input("Enter a whole number: ")

    number = int(user_input)
    
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

    try_again = input("Do you want to try another number? (Y/N): ").upper()

    if try_again != 'Y':
        break
