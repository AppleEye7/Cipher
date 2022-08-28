import string
from PhoneticAlphabet import *                      # imports the Phonetic Alphabet cipher functions

def Caear_Shift_de(shift,message):
    alphabet = string.ascii_lowercase               # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[:shift]   # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(alphabet,shifted)         # create dict for alphabet to shifted
    decoded = message.translate(table)              # message letters translated into the letters from table
    return (decoded)

def Caear_Shift_en(shift,message):
    alphabet = string.ascii_lowercase               # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[:shift]   # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(shifted,alphabet)         # create dict for shifted to alphabet
    encoded = message.translate(table)              # message letters translated into the letters from table
    return (encoded)

#-------------------------------------------------------------------------------------
while True:
    # /----------------------Asks user to decode or encode the message
    choicenum = int(input("Welcome to cipher\nWhat do you want to do?\n"                
                          "(please type corresponding number ie. 1)\n1.Encode Message\n2.Decode Message\n3.Quit\n"))
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
    ciphernum = int(input("Chose the cipher you would like to use to {} your message\n" 
                          "(please type corresponding number ie. 1)\n1.Caesar Shift\n2.Morse Code\n3.Phonetic Alphabet\n4.Quit\n5.Home\n".format(choice)))
    # /----------------------Sets cipher depending on user input
    if ciphernum == 1:
        cipher = "CAESAR SHIFT"
        shift = int(input("How many shifts would you like?\n"))
    elif ciphernum == 2:
        cipher = "MORSE CODE"
    elif ciphernum == 3:
        cipher = "PHONETIC ALPHABET"
    #/----------------------Ends program
    elif ciphernum == 4:
        break
    # /----------------------Sends user back to first GUI
    elif ciphernum == 5:
        continue
    # /---------------------if invalid input repeat until valid
    else:
        print("INVALID ENTRY Please type one of: 1 2 3 4 5\n")
        continue
    # /----------------------Asks user for message
    input_message = input("You chose {} to {} your message\nENTER MESSAGE without using numbers (ei one,three)\n"   
                        "(Chose corresponding number if needed ie. 1)\n1.Quit \n2.Home\n".format(cipher,choice))
    # /----------------------Creates a new variable for the message in lowercase so the users input can be recorded precisely
    message = input_message.lower()
    # /----------------------Ends program
    if message == "1":
        break
    # /----------------------Sends user back to first GUI
    elif message == "2":
        continue
    # /---------------------if invalid number input repeat until valid

    # /------------------------Ciphers----------------------------\ #
    # /----encode-------------------------------------------------
    if choicenum == 1:
        if ciphernum == 1:
            new_message = Caear_Shift_en(shift,message)
        elif ciphernum == 2:
            new_message = Morse_Code_en(message)
        elif ciphernum == 3:
            new_message = Phonetic_Alp_en(message)
    # /----decode-------------------------------------------------
    elif choicenum == 2:
        if ciphernum == 1:
            new_message = Caear_Shift_de(shift,message)
        elif ciphernum == 2:
            new_message = Morse_Code_de(message)
        elif ciphernum == 3:
            new_message = Phonetic_Alp_de(message)
    # /---------------------if invalid input repeat until valid
    else:
        print("INVALID ENTRY Please try again\n")
        continue

    # /----------------------Displys: original message, new message, cipher, choice
    choice2 = int(input("Your message '{}'\nwas {}D using '{}'\nNew message:\n\n{}\n\n"
                        "(please type corresponding number ie. 1)\n1.Quit\n2.Home\n".format(input_message,choice,cipher,new_message)))
    # /----------------------Ends program
    if choice2 == 1:
        break
    # /----------------------Sends user to first GUI
    elif choice2 == 2:
        continue
