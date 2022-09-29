import string
from PhoneticAlphabet import *  # imports the Phonetic Alphabet cipher functions
from MorseCode import *  # imports the Morse Code cipher functions


def ceaser_shift_de(shift, message):
    """Ceaser Shift is a cipher which moves the letters in the message to the left a certain number which decodes the message"""
    alphabet = string.ascii_lowercase  # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[
                                 :shift]  # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(alphabet, shifted)  # create dict for alphabet to shifted
    decoded = message.translate(table)  # message letters translated into the letters from table
    return decoded


#
def ceaser_shift_en(shift, message):
    """Ceaser Shift is a cipher which moves the letters in the message to the right a certain number which encodes the message"""
    alphabet = string.ascii_lowercase  # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[
                                 :shift]  # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(shifted, alphabet)  # create dict for shifted to alphabet
    encoded = message.translate(table)  # message letters translated into the letters from table
    return encoded


# -------------------------------------------------------------------------------------
while True:
    # /----------------------Asks user to decode or encode the message
    choicenum = int(input("WELCOME TO CIPHER!\nWhat do you want to do?\n"
                          "(please type corresponding number e.g. 1)\n1.Encode Message\n2.Decode Message\n3.Quit\n"))
    # /----------------------Sets choice depending on users input
    if choicenum == 1:
        choice = "ENCODE"
    elif choicenum == 2:
        choice = "DECODE"
    elif choicenum == 3:
        break
    # /---------------------if invalid input repeat until valid
    else:
        print("INVALID ENTRY Please type one of: 1 2 3\n")
        continue
    # /----------------------Asks user what cipher to use
    cipher_num = int(input("Chose the cipher you would like to use to {} your message\n"
                           "(please type corresponding number e.g. 1)\n1.Caesar Shift\n2.Morse Code\n"
                           "3.Phonetic Alphabet\n4.Home\n5.Quit\n".format(choice)))
    # /----------------------Sets cipher depending on user input
    try:
        if cipher_num == 1:
            cipher = "CAESAR SHIFT"
            try:
                shift = int(input("How many shifts would you like?\n"))
            except:
                print("INVALID ENTRY Please enter a value from 1 to 26 (inclusive)\n<Reload program>")
                break
            if shift < 0 or shift > 26:
                print("INVALID ENTRY Please enter a value from 1 to 26 (inclusive)\n<Reload program>")
                break
            #else:
                #continue
        elif cipher_num == 2:
            cipher = "MORSE CODE"
        elif cipher_num == 3:
            cipher = "PHONETIC ALPHABET"
        # /----------------------Sends user back to first GUI
        elif cipher_num == 4:
            continue
        # /----------------------ends program
        elif cipher_num == 5:
            break
        else:
            print("INVALID ENTRY Please type one of: 1 2 3 4 5\n<Reload program>")
    # /---------------------if invalid input repeat until valid
    except ValueError:
        print("INVALID ENTRY Please type one of: 1 2 3 4 5\n<Reload program>")
        continue
    # /----------------------Asks user for message
    # /--------------------------------------------------MORSE CODE-----------------------------------------------\
    if cipher == "MORSE CODE":
        if choice == "ENCODE": # test ----> - . ... -
            input_message = input("You chose {} to {} your message\nENTER MESSAGE\n".format(cipher, choice))
        elif choice == "DECODE":  # - . ... - ----> test
            input_message = input(
                "You chose {} to {} your message\nENTER MESSAGE with '/' for letters and '|' for words"
                "e.g. ../-/-..-|-.|\n".format(cipher, choice))
        message = input_message.lower().strip()
# /----------------------if the message contains numbers  and/or letters continue otherwise break loop
        if any(char in set(string.punctuation) for char in input_message):
            print("INVALID ENTRY Please enter message without special characters\n<Reload program>")
            break
        else:
            message = input_message.lower().strip()

    # /----------------------------------------------------CAESAR SHIFT---------------------------------------------\
    elif cipher == "CAESAR SHIFT":
        input_message = input("You chose {} to {} your message\nENTER MESSAGE without special characters e.g.'(,@/'\n"
                              .format(cipher, choice))
        # /----------------------if the message contains numbers and/or letters continue otherwise break loop
        if any(char in set(string.punctuation) for char in input_message):
            print("INVALID ENTRY Please enter message without special characters\n<Reload program>")
            break
        else:
            message = input_message.lower().strip()

    # /----------------------------------------------------Phonetic Alphabet---------------------------------------------\
    elif cipher == "PHONETIC ALPHABET":
        if choice == "ENCODE":  # test ----> Tango Echo Sierra Tango
            input_message = input(
                "You chose {} to {} your message\nENTER MESSAGE without numbers e.g.2 4 10 or special "
                "characters e.g.'(,@/'\n".format(cipher, choice))
            message = input_message.lower().strip()

        elif choice == "DECODE":  # Tango Echo Sierra Tango ----> test
            input_message = input("You chose {} to {} your message\nENTER MESSAGE with spaces between letters and a "
                                  "full stop for a word e.g. Tango Hotel Echo. X-ray\n".format(cipher, choice))
            message = input_message.title().strip()
        print(message)
    # /----------------------message creates a new variable for the user input in case it is in incorrect format for
    #                        cipher so the users input can be recorded precisely
    # /----------------------Sends user back to first GUI
    if message == "1":
        continue
    # /----------------------Ends program
    elif message == "2":
        break

    # /------------------------Ciphers----------------------------\ #
    # /--if choicenum == 1 then user chose encode-----------------
    if choicenum == 1:
        if cipher_num == 1:  # cipher = Ceaser Shift
            new_message = ceaser_shift_en(shift, message)
        elif cipher_num == 2:  # cipher = Morse code
            new_message = morse_code_en(message)
        elif cipher_num == 3:  # cipher = Phonetic Alphabet
            new_message = phonetic_alp_en(message)

    # /--if choicenum == 2 then user chose decode-----------------
    elif choicenum == 2:
        if cipher_num == 1:  # cipher = Ceaser Shift
            new_message = ceaser_shift_de(shift, message)
        elif cipher_num == 2:  # cipher = Morse code
            new_message = morse_code_de(message)
        elif cipher_num == 3:  # cipher = Phonetic Alphabet
            new_message = phonetic_alp_de(message)
    # /---------------------if invalid input repeat whole program
    else:
        print("INVALID ENTRY Please try again\n")
        continue
    # /----------------------Displays: original message, new message, cipher, choice
    choice2 = int(input("Your message '{}'\nwas {}D using {}\nNew message:\n\n{}\n\n"
                        "(please type corresponding number e.g. 1)\n1.Home\n2.Quit\n".format(input_message, choice,
                                                                                             cipher, new_message)))
    # /----------------------Ends program
    if choice2 == 1:
        continue
    # /----------------------Sends user to first GUI
    elif choice2 == 2:
        break
