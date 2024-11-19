# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: James Van
# created: 11/18/24
# last update: 11/19/24
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message(plain_text):
    plain_text = str(input("Enter a message to encode"))
    ciphertext = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]




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
    running = True
    while running:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")


        if selection == "1":
            encode_message()
            # in_string = input("Please Enter a String!")
            # print(f"String is: {in_string}")
            # out_string = ""
            # for char in in_string:
            #     if 65 <= ord(char) <= 90:
            #         # uppercase to lower case
            #         out_string += chr(ord(char) + 32)
            #         # lowercase to uppercase
            #     elif 97 <= ord(char) <= 122:
            #         out_string += chr(ord(char) - 32)
            #     else:
            #         out_string += char

            print(f"Final String is {out_string}")
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        # else:
        #     print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()