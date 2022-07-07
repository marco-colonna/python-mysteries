# Define a function to shift the character by the specified amount
def lasso_character(character, shift_amount):
    # Lowercase character (default)
    # Invoke the ord function to translate the character to its ASCII code
    # Save the code to the character_code variable
    character_code = ord(character.lower())

    # Save the base ASCII code to the ascii_base variable
    # The ASCII number representation of lowercase letter 'a'
    ascii_base = ord('a')

    # Save the range of ASCII codes to the ascii_range variable
    # The number of letters in the alphabet
    ascii_range = 26

    # Uppercase character
    if character.isupper():
        # Save the code to the character_code variable
        character_code = ord(character)

        # The ASCII number representation of uppercase letter 'A'
        ascii_base = ord('A')

    # Numeric character
    if character.isnumeric():
        # Save the code to the character_code variable
        character_code = ord(character)

        # The ASCII number representation of digit '0'
        ascii_base = ord('0')

        # The number of digits in the decimal system
        ascii_range = 10

    # The formula to calculate the ASCII number for the decoded character
    # Take into account looping around the ascii_range
    true_character_code = ascii_base + (((character_code - ascii_base) + shift_amount) % ascii_range)

    # Convert the ASCII number to the character
    decoded_character = chr(true_character_code)

    # Send the decoded character back
    return decoded_character

# Define a function to shift the characters in a word by a specified amount
def lasso_word(word, shift_amount):
    # This variable is updated each time another character is decoded
    decoded_word = ""

    # This for loop iterates through each character in the word parameter
    for character in word:
        # The lasso_character() function is invoked with each character and the shift amount
        # The result (the decoded character) is stored in a variable called decoded_character
        decoded_character = lasso_character(character, shift_amount)

        # The decoded_character value is added to the end of the decoded_word value
        decoded_word = decoded_word + decoded_character

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word

# Define a function to find the truth in a secret message
def lasso_message(message, shift_amount):
    # This variable is updated each time another word is decoded
    decoded_message = []

    # This for loop iterates through each word in the message parameter
    for index, word in enumerate(message):
        # The lasso_word() function is invoked with each word and the shift amount
        # The result (the decoded word) is stored in a variable called decoded_word
        decoded_word = lasso_word(word, shift_amount[index])

        # The decoded_word value is added to the end of the decoded_message value
        decoded_message.append(decoded_word)

    # The decoded_message is sent back to the line of code that invoked this function
    return decoded_message

# Try to decode the secret, encoded message
words = ["Ncevy", "gpvsui", "ugflgkg", "wjmmf"]

shifts = [13, 25, -18, -1]

print("Shifting ", words, " by ", shifts, " gives: \n", lasso_message(words, shifts), sep = "")

# Additional challenges for your decrypt code
# As an added challenge, you can explore how to:
#   Maintain casing for each letter throughout the decoding process. -> DONE
#   Create a function to read in an entire message without having to print each word individually. -> DONE
#   Modify your decoder to include numbers. -> DONE
