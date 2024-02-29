import time as t
import pyfiglet as pyf

def underline_exceptions(number):
    number_str = str(number)
    result = ""

    for digit in number_str:
        if digit not in ['0', '1']:
            return "Error: Unexpected digit '{}' found.".format(digit)
        else:
            result += '\033[4m{}\033[0m'.format(digit)  # Using ANSI escape codes for underlining

    return result

def dec_to_bin(user_input):
    try:
        number = int(user_input)
        binary = bin(number)[2:]  # Convert to binary (remove '0b' prefix)
        return binary
    except ValueError:
        return "Error: Input is not a valid number."

def bin_to_dec(user_input):
    try:
        number = int(user_input, 2) # Convert binary to decimal
        return str(number)
    except ValueError:
        return "Error: Input is not a valid binary number."

print("=================================")
t.sleep(0.1)
print(pyf.figlet_format("CONVERTER", font="slant"))
t.sleep(0.1)
print("=================================")

run = True
while run:
    t.sleep(0.1)
    print("[1] Decimal to Binary")
    print("[2] Binary to Decimal")
    user_input = input(">> ")

    if user_input == '1':
        decimal_input = input("Enter a decimal number: ")
        result = dec_to_bin(decimal_input)
        print("Binary representation:", result)

    elif user_input == '2':
        binary_input = input("Enter a binary number: ")
        error_message = underline_exceptions(binary_input)

        if error_message.startswith("Error"):
            print(error_message)
        else:
            result = bin_to_dec(binary_input)
            print("Decimal representation:", result)

    else:
        print("Invalid Input")
