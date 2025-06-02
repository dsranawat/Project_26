print(" Even or Odd Checker")

while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Exiting .... Goodbye!")
        break

    if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
        print("Invalid input! Please enter a valid number.")
        continue
    
    number = int(user_input)
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")