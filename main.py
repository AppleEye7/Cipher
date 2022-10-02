"""
Cipher is a program which takes the users input of a message and either decodes or encodes the message using the users 
choice of method (cipher).
"""

from phonetic_alphabet import *  # imports the Phonetic Alphabet cipher functions
from morse_code import *  # imports the Morse Code cipher functions
from ceaser_shift import *  # imports the Ceaser Shift cipher functions

input_message = ""
message = ""
shift = 0

while True:
    # /----------------------Asks user to decode or encode the message-------------------------------------------------\
    try:
        choice_num = int(input("WELCOME TO CIPHER!\nWhat do you want to do?\n"
                               "(please type corresponding number e.g. 1)\n1.Encode Message\n2.Decode Message\n3.Quit\n"))
        # /----------------------Sets choice depending on users input
        if choice_num == 1:
            choice = "ENCODE"
        elif choice_num == 2:
            choice = "DECODE"
        elif choice_num == 3:
            print("<program terminated>")
            break
        # /---------------------if invalid number input repeat until valid
        else:
            print("INVALID ENTRY Please type one of: 1 2 3\n")
            continue
    # /-------------------------if invalid character repeat until valid
    except ValueError:
        print("INVALID ENTRY Please type one of: 1 2 3\n")
        continue
    # /----------------------Asks user what cipher to use--------------------------------------------------------------\
    try:
        cipher_num = int(input("Chose the cipher you would like to use to {} your message\n"
                               "(please type corresponding number e.g. 1)\n1.Caesar Shift\n2.Morse Code\n"
                               "3.Phonetic Alphabet\n4.Home\n5.Quit\n".format(choice)))
    # /-----------------------if user input is not a number then ends program
    except ValueError:
        print("INVALID ENTRY Please enter a value from 1 to 5 (inclusive)\n<Reload program>")
        break
    # /----------------------Sets cipher depending on user input
    try:
        if cipher_num == 1:
            cipher = "CAESAR SHIFT"
            try:
                shift = int(
                    input("How many shifts would you like?\n(please type a number between (1 - 26) inclusive\n"))
            except ValueError:
                print("INVALID ENTRY Please enter a value from 1 to 26 (inclusive)\n<Reload program>")
                break
            if shift < 0 or shift > 26:
                print("INVALID ENTRY Please enter a value from 1 to 26 (inclusive)\n<Reload program>")
                break
        elif cipher_num == 2:
            cipher = "MORSE CODE"
        elif cipher_num == 3:
            cipher = "PHONETIC ALPHABET"
        # /----------------------Sends user back to first GUI
        elif cipher_num == 4:
            continue
        # /----------------------ends program
        elif cipher_num == 5:
            print("<program terminated>")
            break
        else:
            print("INVALID ENTRY Please type one of: 1 2 3 4 5\n<Reload program>")
            break
    # /---------------------if invalid input repeat until valid
    except ValueError:
        print("INVALID ENTRY Please type one of: 1 2 3 4 5\n<Reload program>")
        continue
    # /----------------------Asks user for message---------------------------------------------------------------------\
    # /----------------------------------------------------CAESAR SHIFT------------------------------------------------\
    # /-------------------------lets user know that there is escape options
    print("Type '<home>' to go to home and '<quit>' to end program\n")
    if cipher == "CAESAR SHIFT":
        input_message = input("You chose {} to {} your message\nENTER MESSAGE without special characters e.g.'(,@/\n"
                              .format(cipher, choice))
        # /----------------------if the message contains special characters
        if any(char in set(string.punctuation) for char in input_message):
            print("INVALID ENTRY Please enter message without special characters\n<Reload program>")
            break
            # /------------------------if message does not meet the above criteria then it is in the correct format
        else:
            # /------message is created to be able to use input_message to display the exact message that the user typed
            message = input_message.strip()
    # /--------------------------------------------------MORSE CODE----------------------------------------------------\
    elif cipher == "MORSE CODE":
        if choice == "ENCODE":  # test ----> - . ... -
            input_message = input("You chose {} to {} your message\nENTER MESSAGE\n".format(cipher, choice))
            # /----------------------if the user entered nothing or a space
            if input_message == "" or " ":
                print("please enter a valid value\n<program terminated>")
                break
            # /----------------------if the message contains characters break loop otherwise continue
            if any(char in set(string.punctuation) for char in input_message):
                print("INVALID ENTRY Please enter message without special characters\n<Reload program>")
                break
            else:
                pass
        # /------------------------------------------------------------if the user choose to decode a message
        elif choice == "DECODE":  # - . ... - ----> test
            input_message = input("You chose {} to {} your message\nENTER MESSAGE with '/' separating letters "
                                  "and '|' ending every word e.g. ../-/-..-|-.|\n".format(cipher, choice))
            # /----------------------if the user entered nothing or a space
            if input_message == "" or " ":
                print("Please enter a valid value\n<program terminated>")
                break
            # /----------------------if message contains letter
            if input_message.isalpha():
                print("INVALID ENTRY Please enter message in morse code\n<Reload program>")
                break
            # /-----------------------if message contains numbers
            elif input_message.isnumeric():
                print("INVALID ENTRY Please enter message in morse code\n<Reload program>")
                break
            # /-----------------------if message does not have '/' or '|' then incorrect format
            elif not '/' and '|' in input_message:
                print("INVALID ENTRY Please enter message with'/' separating letters and '|' ending words "
                      "\n<Reload program>")
                break
            # /------------------------if message does not meet the above criteria then it is in the correct format
            else:
                # /--message is created to be able to use input_message to display the exact message that the user typed
                message = input_message.strip()
    # /----------------------------------------------------Phonetic Alphabet---------------------------------------------\
    elif cipher == "PHONETIC ALPHABET":
        if choice == "ENCODE":  # test ----> Tango Echo Sierra Tango
            input_message = input("You chose {} to {} your message\nENTER MESSAGE without numbers e.g.2 4 10 or special"
                                  " characters e.g.'(,@/'\n".format(cipher, choice))
            # /-----------------------if message contains special characters
            if any(char in set(string.punctuation) for char in input_message):
                print("INVALID ENTRY Please enter message without special characters\n<Reload program>")
                break
            # /-----------------------if message contains numbers
            if input_message.isnumeric():
                print("INVALID ENTRY Please enter message without numbers \n<Reload program>")
                break
            # /-----------------------if message contains nothing or a space
            if input_message == "" or " ":
                print("Please enter a valid value\n<program terminated>")
                break
            # /-----------------------if message does not meet the above criteria then it is in the correct format
            else:
                # /--message is created to be able to use input_message to display the exact message that the user typed
                message = input_message.title().strip()
        # /------------------------------------------------------------if the user choose to decode a message
        elif choice == "DECODE":  # Tango Echo Sierra Tango ----> test
            input_message = input("You chose {} to {} your message\nENTER MESSAGE with spaces between letters and a "
                                  "full stop for a word e.g. Tango Hotel Echo. X-ray\n".format(cipher, choice))

            # /------------------------if message contains numbers end program
            if input_message.isnumeric():
                print("INVALID ENTRY Please enter message without numbers \n<Reload program>")
                break
            # /------------------------if message contains nothing or a space end program
            if input_message == "" or " ":
                print("Please enter a valid value\n<program terminated>")
                break
            # /------------------------if message does not meet the above criteria then it is in the correct format
            else:
                # /--message is created to be able to use input_message to display the exact message that the user typed
                message = input_message.title().strip()
    # /--------------------------------if cipher is not one of the above than user did not enter a value for cipher
    else:
        print("Please chose a cipher to encode or decode your message\n<program terminated>")
        break
    # /----------------------if user typed these in then program does the following
    # /----------------------Sends user back to first GUI
    if input_message == "<home>":
        continue
    # /----------------------Ends program
    elif input_message == "<quit>":
        print("<program terminated>")
        break
    # /----------------------if user did not type the above then they entered a message so continue program
    else:
        pass
    # /----------------calls the function to decode/encode message depending on the cipher the user chose--------------\
    # /----------------if choice_num == 1 then user chose encode-------------------------------------------------------\
    if choice_num == 1:
        # /-----------------Ceaser Shift
        if cipher_num == 1:
            new_message = ceaser_shift_en(shift, message)
        # /------------------Morse code
        elif cipher_num == 2:
            new_message = morse_code_en(message)
        # /------------------Phonetic Alphabet
        elif cipher_num == 3:
            new_message = phonetic_alp_en(message)
        # /------------------if cipher_num is not equal to any of the above values then the user did not enter a cipher
        else:
            print("Please chose a cipher\n<program terminated>")
            break
    # /------------------if choice_num == 2 then user chose decode-----------------------------------------------------\
    elif choice_num == 2:
        # /------------------Ceaser Shift
        if cipher_num == 1:
            new_message = ceaser_shift_de(shift, message)
        # /------------------Morse code
        elif cipher_num == 2:
            new_message = morse_code_de(message)
        # /-------------------Phonetic Alphabet
        elif cipher_num == 3:
            new_message = phonetic_alp_de(message)
        # /------------------if cipher_num is not equal to any of the above values then the user did not enter a cipher
        else:
            print("Please chose a cipher\n<program terminated>")
            break
    # /-------------------if choice_num is not equal to any of the above values then the user did not enter their choice
    else:
        print("INVALID ENTRY Please chose to encode or decode\n<program terminated>")
        break
    # /----------------------Displays the original message, new message, cipher, choice--------------------------------\
    try:
        choice2 = int(input("Your message '{}'\nwas {}D using {}\nNew message:\n\n{}\n\n(please type corresponding"
                            " number e.g. 1)\n1.Home\n2.Quit\n".format(input_message, choice,cipher, new_message)))
        # /----------------------Sends user to first GUI
        if choice2 == 1:
            continue
        # /----------------------Ends program
        elif choice2 == 2:
            print("<program terminated>")
            break
        # /----------------------if the user did not enter 1 or 2 end program
        else:
            print("Please enter one of the values: 1 2\n<program terminated>")
            break
        # /---------------------if the user did not enter a number end program
    except ValueError:
        print("Please enter one of the values: 1 2\n<program terminated>")
        break
