#!/usr/bin/python
# calculate the entropy of a password
# formula: log2(number of characters) * length of password (Entropy = log2(N^L)

# import modules
import math
import getpass  # for hiding the password input => need to run in cmd


def calculate_entropy(password):
    # Define the character sets
    lowercase_letters = 26
    uppercase_letters = 26
    digits = 10
    special_characters = 33  # Assuming a set of common special characters

    # Calculate the size of the character set
    character_set_size = lowercase_letters + uppercase_letters + digits + special_characters

    # Calculate entropy
    password_length = len(password)
    entropy = math.log2(math.pow(character_set_size, password_length))

    return entropy


# usage
password = getpass.getpass("Enter a password: ")
entropy = calculate_entropy(password)
print(f"Entropy: {entropy}")


def show_entropy_strength(entropy):
    if entropy < 50:
        print("Weak password")
    elif entropy < 85:
        print("Moderate password")
    elif entropy < 100:
        print("Strong password")
    else:
        print("Very strong password")


show_entropy_strength(entropy)
