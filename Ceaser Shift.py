"""Caear Shift is a cipher which moves the letters position in the message to the right a certain number to encode the
    message and moves the position to the left a certain number to decode the message"""

import string


def ceaser_shift_en(shift, message):
    """Moves each letter in message to the right of their position a certain number which is determined by the value of
       shift"""
    # /----------------generates the alphabet in lowercase
    alphabet = string.ascii_lowercase
    # /----------------moves each letter before the index of shift value(not inclusive) to the end of string
    shifted = alphabet[shift:] + alphabet[:shift]
    # /----------------creates a dictionary for the shifted alphabet to the real alphabet
    table = str.maketrans(shifted, alphabet)
    # /-----------------letters from the message changed into the letters from table
    encoded = message.translate(table)
    # /-----------------returns the changed message
    return encoded


def ceaser_shift_de(shift, message):
    """Moves each letter in message to the left of their position a certain number which is determined by the value of
       shift"""
    # /----------------generates the alphabet in lowercase
    alphabet = string.ascii_lowercase
    # /----------------moves each letter before the index of shift value(not inclusive) to the end of string
    shifted = alphabet[shift:] + alphabet[:shift]
    # /----------------create dictionary for the real alphabet to the shifted alphabet
    table = str.maketrans(alphabet, shifted)
    # /-----------------letters from the message changed into the letters from table
    decoded = message.translate(table)
    # /-----------------returns the changed message
    return decoded
