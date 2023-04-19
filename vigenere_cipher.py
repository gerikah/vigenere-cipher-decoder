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
        # Get corresponding letter value of current keyword character
        # Calculate sum and take mod 26
        # Convert sum_val to corresponding letter and add to ciphertext list
    # Join ciphertext list into a string and return
# Input message
# Input keyword
# Print the ciphertext