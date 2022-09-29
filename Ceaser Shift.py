#Caear Shift is a cipher which moves the letters in the message to the right a certain number to encode the message and
# moves the letter to the left to decode the message
import string

def Caear_shift_de(shift,message):
    alphabet = string.ascii_lowercase  # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[:shift]  # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(alphabet, shifted)  # create dict for alphabet to shifted
    decoded = message.translate(table)  # message letters translated into the letters from table
    return decoded


def Caear_shift_en(shift,message):
    alphabet = string.ascii_lowercase  # generates the ascii alphabet in lowercase
    shifted = alphabet[shift:] + alphabet[:shift]  # moves each letter before shift value(not inclusive) to the end of string
    table = str.maketrans(shifted, alphabet)  # create dict for shifted to alphabet
    encoded = message.translate(table)  # message letters translated into the letters from table
    return encoded



