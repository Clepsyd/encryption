from string import printable,\
                   ascii_letters,\
                   ascii_lowercase,\
                   ascii_uppercase
import random
import pickle

def generate_code():
    # Generates a random number for each printable ASCII character,
    # Returns a list of tuples containing each character/number pair.
    characters = printable
    numbers = random.sample(range(len(characters) + 1000), len(characters))
    code = list(zip(characters, numbers))
    return code

def encode(string, code):
    # Replaces each character of string with its code-number
    # and adds a random number of random letters

    coded_string = []
    # find matching number for each character
    for character in string:
        for letter, number in code:
            if character == letter:
                # add the matching number
                coded_string.append(str(number))
                coded_string.append(''.join(
                                        random.sample(
                                            ascii_lowercase,
                                            random.randint(2,6)
                                            )
                                        )
                                   )# random letters used to separate numbers
    for _ in range(random.randrange(len(string))):
        coded_string.insert(
                            random.randrange(len(coded_string)),
                            ''.join(random.sample(
                                          ascii_uppercase, random.randint(1, 3)
                                          ))
                            ) # random uppercase letters randomly inserted
    return ''.join(coded_string)

def decode(string, code):

    def retrieve_letter(n):
        for letter, number in code:
            if int(n) == number:
                return letter
            else:
                continue
        return "No Match found"


    decoded_list = []
    decoded_string = ''
    character = ''
    for item in string:
        if item.isdigit():
            character += item
        else:
            if character != '':
                decoded_list.append(character)
                character = ''
    for n in decoded_list:
        decoded_string += retrieve_letter(n)
    return decoded_string

def save_code(object):
    with open("code.p", "wb") as f:
        pickle.dump(object, f)

def load_code():
    try:
        with open("code.p", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No saved code found.")
        return None


def main():

    import time

    code = generate_code()

    print("Welcome to my encryption program!")

    while True: #Code selection menu

        print("Please select an option:")
        print("1: Use saved code")
        print("2: Use new code and overwrite saved code")
        print("3: Use new code and keep saved code")
        prompt = input(">")
        if prompt == "1":
            if load_code() == None:
                code = generate_code()
            else:
                code = load_code()
            break
        elif prompt == "2":
            save_code(code)
            break
        elif prompt == "3":
            break
        else:
            "This option is not available"
            continue

    while True: #Main Loop, asks user if he wants to encode/decode

        print("Would you like to encrypt a phrase?(Y/N)")

        prompt = input(">")
        if prompt in ("N", "no", "No", "n"):
            print("Press Enter to exit or type in anything to continue:")
            prompt = input(">")
            if prompt == '':
                print ("Thank you for using the program, good bye!")
                time.sleep(2)
                break
        else:
            phrase = input("Enter your text here :\n>")
            print (f"\nHere is your code : {encode(phrase, code)}\n")

        print("Would you like to decrypt a phrase?(Y/N)")

        prompt = input(">")
        if prompt in ("N", "no", "No", "n"):
            print("Press Enter to exit or type in anything to continue:")
            prompt = input(">")
            if prompt == '':
                print ("Thank you for using the program, good bye!")
                time.sleep(2)
                break
        else:
            coded_phrase = input("Enter your code here :\n>")
            print(f"\nHere is your original text: {decode(coded_phrase, code)}\n")
            time.sleep(1)
            input("Press Enter to continue")
            print("\n")

if __name__ == '__main__':
    main()
