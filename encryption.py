from string import printable,\
                   ascii_letters,\
                   ascii_lowercase,\
                   ascii_uppercase
import random
import pickle

# Generates a random number for each printable ASCII character,
# Each character/number pair is stored as a tuple in a list named "code"
characters = printable
numbers = random.sample(range(len(characters) + 1000), len(characters))
code = list(zip(characters, numbers))

def encode(string):
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

def decode(string):

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

def save_code():
    global code
    with open("code.p", "wb") as f:
        pickle.dump(code, f)

def retrieve_code():
    global code
    with open("code.p", "rb") as f:
        code = pickle.load(f)

def main():

    import time

    print("Welcome to my encryption program!")

    while True:

        print("Please select an option:")
        print("1: Use saved code")
        print("2: Use new code and overwrite saved code")
        print("3: Use new code and keep saved code")
        prompt = input(">")
        if prompt == "1":
            try:
                retrieve_code()
            except:
                print("No code found, we'll use a new one")
        elif prompt == "2":
            save_code()

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
                continue

        phrase = input("Enter your text here :\n>")
        print (f"\nHere is your code : {encode(phrase)}\n")
        print("Would you like to decrypt a phrase?(Y/N)")
        prompt = input(">")
        if prompt in ("N", "no", "No", "n"):
            continue
        code = input("Enter your code here :\n>")
        print(f"\nHere is your original text : {decode(code)}\n")
        time.sleep(1)
        input("Press Enter to continue")
        print("\n")

if __name__ == '__main__':
    main()
