# Define a function to find the truth by shifting the character by the specified amount
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

# Define a function to find the truth in a secret message
# Shift the characters in a word by a specified amount to discover the hidden word
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

# Try to decode the secret, encoded message
print("Shifting Ncevy by 13 gives: \n" + lasso_word("Ncevy", 13))
print("Shifting gpvsui by 25 gives: \n" + lasso_word("gpvsui", 25))
print("Shifting ugflgkg by -18 gives: \n" + lasso_word("ugflgkg", -18))
print("Shifting wjmmf by -1 gives: \n" + lasso_word("wjmmf", -1))

# Additional challenges for your decrypt code
# As an added challenge, you can explore how to:
#   Maintain casing for each letter throughout the decoding process. -> DONE
#   Create a function to read in an entire message without having to print each word individually.
#   Modify your decoder to include numbers. -> DONE
