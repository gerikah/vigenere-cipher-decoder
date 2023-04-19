# Object Oriented Programming CMPE-103 LAB EXERCISE No. 1 : Problem 3

import pyfiglet
border = "-" * 180
title = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Vigenere\nCipher\n", justify = "center", font = "isometric1", width = 175) + "\n")
print(title)

def vigenere_cipher(message, keyword):
# Convert message and keyword to uppercase
    message = message.upper()
    keyword = keyword.upper()

# Convert the keyword to a numeric key of values 0 - 25
    key_values = [ord(character) - 65 for character in keyword]

# Empty ciphertext string
    ciphertext = []
    
    # Loop through message characters
    for i in range(len(message)):

        # Get letter value of current message character
        letter_value = ord(message[i]) - 65

        # Get corresponding letter value of current keyword character
        key_value = key_values[i % len(keyword)]

        # Calculate sum and take mod 26
        sum_value = (letter_value + key_value) % 26

        # Convert sum_val to corresponding letter and add to ciphertext list
        ciphertext.append(chr(sum_value + 65))

    # Join ciphertext list into a string and return
    return "".join(ciphertext)
    
# Input message
print(border + "\033[95m" + pyfiglet.figlet_format("\nInput Message", justify = "center", font = "cybermedium", width = 175))
message = input(" ".center(80))

message_without_spaces = message.replace(" ", "") #If user input a message with spaces

# Input keyword
# Print the ciphertext