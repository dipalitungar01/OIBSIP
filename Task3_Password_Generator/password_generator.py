import random 
import string

def generate_password():

    while True:
        try:
            length = int(input("Enter password length(minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")


    print("\nChoose character types:") 
    print("1. Uppercase letters")       
    print("2. Lowercase letters") 
    print("3. Numbers") 
    print("4. Symbols")

    choices = input("Enter your choice separated by space(example: 1 2 3 4): ").split()

    choices = set(choices)

    if len(choices) < 2:
        print("Please select at least 2 character types.")
        return

    character_sets = []

    if "1" in choices:
        character_sets.append(string.ascii_uppercase)

    if "2" in choices:
        character_sets.append(string.ascii_lowercase)

    if "3" in choices:
        character_sets.append(string.digits)

    if "4" in choices:
        character_sets.append(string.punctuation)

    if length < len(character_sets):
        print("Password length is too short.")
        return

    password_characters = [] 

    for character_set in character_sets:
        password_characters.append(random.choice(character_set))

    all_characters = "".join(character_sets)

    remaining_length = length - len(password_characters)

    for _ in range(remaining_length):
        password_characters.append(random.choice(all_characters))

    random.shuffle(password_characters)
    password = "".join(password_characters)

    print("\nGenerated password:", password)

while True:
    generate_password()

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the password generator.")
        break           