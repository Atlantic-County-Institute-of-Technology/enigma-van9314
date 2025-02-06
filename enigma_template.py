# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: James Van
# created: 11/18/24
# last update: 2/5/25
import random
import sys
# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    # use string translation to manipulate ciphertext
    message = input("Enter a message to encode:").lower()
    key_input = input("Please input a key")
    if key_input.strip() == "":
        key = random.randint(0, 25)
        print(f"Random Key generated {key}")
    else:
        key = int(key_input)
    encoded_message = ""
    for char in message:
        if char in alphabet:
            index = (alphabet.index(char) + key) % len(alphabet)
            encoded_message += alphabet[index]
        else:
            encoded_message += char  # other characters remain unchanged

    print(f"Encoded message: {encoded_message}")

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    input_file = input("Enter the file name to encode: ")
    output_file = input("Enter the output file name: ")
    key_input = input("Please input the key (leave blank for random): ")

    if key_input.strip() == "":
        key = random.randint(0, 25)
        print(f"Random key generated: {key}")
    else:
        key = int(key_input)

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                encoded_line = ""
                for char in line.lower():
                    if char in alphabet:
                        index = (alphabet.index(char) + key) % len(alphabet)
                        encoded_line += alphabet[index]
                    else:
                        encoded_line += char
                outfile.write(encoded_line)
        print(f"File encoded successfully with key {key}. Output written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    input_file = input("Enter the file name to decode")
    output_file = input("Enter the output file name")
    key = int(input("Enter the key to decode:"))
    try:
        with open(input_file,"r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                decoded_line = ""
                for char in line.lower():
                    if char in alphabet:
                        index = (alphabet.index(char) - key) % len(alphabet)
                        decoded_line += alphabet[index]
                    else:
                        decoded_line += char
                        outfile.write(decoded_line)
                print(f"File decoded successfully. Output written to {output_file}.")
    except FileNotFoundError:
                print(f"Error: The file '{input_file}' was not found.")


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    try:
        with open(filename,"r") as infile:
            content = infile.read()
            for key in range(len(alphabet)):
                decoded_message = ""
                for char in content.lower():
                    if char in alphabet:
                        index = (alphabet.index(char) - key) % len(alphabet)
                        decoded_message += alphabet[index]
                    else: 
                        decoded_message += char
                print(f"Key is {key}: {decoded_message}")
    except FileNotFoundError:
        print(f"Error: File {filename} was not found")




# main method declaration
def main():
    while True:
        print(f"What would you like to do?\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode File.\n"
              f"[3]: Decode File.\n"
              f"[4]: Exit.\n")

        selection = input("Choose an option:")


        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("invalid choice. Please try again")

# runs on program start
if __name__ == "__main__":
    main()