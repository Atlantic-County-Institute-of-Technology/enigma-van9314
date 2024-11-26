# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: James Van
# created: 11/18/24
# last update: 11/25/24
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    print("Welcome to Project Enigma! This is a program that can encode and decode files/messages as you wish!")
    # use string translation to manipulate ciphertext
    message = str(input("Enter a message to encode:"))
    key = random.randint(1, 25)
    ciphertext = ""
    message = message.lower()
    for char in message:
        if char in alphabet:
            index = alphabet.find(char)
            index = (index + key) % len(alphabet)
            ciphertext += alphabet[index]
    else:
        alphabet += char
    print(f"Encoded message is: {ciphertext}")
    print("Key for encode: {key}")


def decrypt_message():
    pass



# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"What would you like to do?\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Decode a custom message.\n"
              f"[3]: Encode a file.\n"
              f"[4]: Decode a file.\n"
              f"[5]: Exit")

        selection = input("Choose an option:")


        if selection == "1":
            encode_message()
        elif selection == "2":
            decrypt_message()
        elif selection == "3":
            encode_file()
        elif selection == "4":
            decode_file()
        elif selection == "5":
            exit("EXITING THE PROGRAM")

# runs on program start
if __name__ == "__main__":
    main()