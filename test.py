def is_valid_input(input_str):
    try:
        input_num = int(input_str)
        if input_num <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


while True:
    user_input = input("Please enter a positive integer: ")
    if is_valid_input(user_input):
        print("thank you")
        break
    else:
        print("Invalid input. Please try again.")
