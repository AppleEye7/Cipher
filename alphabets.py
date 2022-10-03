"""These functions are to make the program easily modifiable and so flexible. If the user wants to run the program with
different values than the English, Morse, or Phonetic alphabet than they can change it here, and it will make all the
relevant ciphers use the changed alphabet."""


# /----------------------------Phonetic Alphabet cipher alphabets-------------------------------------------------------
def phonetic_alphabet():
    phonetic_alphabet_list = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                              "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                              "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Xray", "Yankee", "Zulu"]
    return phonetic_alphabet_list


def alphabet_with_typos():
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "q", "r", "s", "t", "u", "v", "w", "x", "x" "y", "z"]
    return alphabet_list


# /-----------------------------Morse Code and Ceaser Shift cipher alphabets--------------------------------------------

def morse_alphabet():
    morse_alphabet_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                           "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
                           ".----", "..---", "...-- ", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
    return morse_alphabet_list


def alphabet():
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return alphabet_list


def alphabet_with_numbers():
    alphabet_with_numbers_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                                  "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return alphabet_with_numbers_list
