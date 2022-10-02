"""morse code is a cipher where each letter in the alphabet is a specific series of dots and/or dashes.
Words are separated by '|' and letters in each word are separated by '/'
"""


def morse_code_en(message):
    """takes the user input of message and changes the word/s into morse code and returns the encoded message in
        morse code format"""
    last_letter = []
    morse_character = []
    encoded_message = []

    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
             ".----", "..---", "...-- ", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    check_value = dict(zip(alphabet, morse))  # {'a': '.-', 'b': '-...'... joins both lists into a dictionary
    # /----------------------creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    # /----------------------counts the number of words
    number_of_words = len(word_list)
    # /----------------------runs the loop one more time than there are words
    for w in range(0, number_of_words):
        # /------------------for each word
        word = word_list[w]
        # /------------------counts the number of letters in the word
        number_of_letters = len(word)
        # /----------------------runs the loop one more time than there are letters
        for l in range(0, number_of_letters):
            # /--------------finds each letter in the word
            letter = word[l]
            # /-------making the output in morse code format with '|' separating words and '\' separating letters------\

            # /--------------if it is the last letter in the word------------------------------------------------------\
            if l == number_of_letters - 1:
                # /----------------------finds the corresponding morse character for the letter
                last_letter_morse = check_value[letter]
                # /----------------------adds the morse character to an array
                last_letter.append(last_letter_morse)
                # /-----------------------adds '|' to the array with the morse character
                last_letter.append('|')
                # /---------------joins the morse character with '|' so it is for example: '.-|' and adds it to an array
                encoded_message.append("".join(last_letter))
                # /-----------------------empties the array so the next morse character can be added with '/'
                last_letter = []
            # /--------------if the letter is not the last in the word
            else:
                # /----------------------finds the corresponding morse character for the letter
                morse = check_value[letter]
                # /----------------------adds the morse character to an array
                morse_character.append(morse)
                # /-----------------------adds '/' to the array with the morse character
                morse_character.append('/')
                # /-----------------------joins the morse character with '/' and adds it to an array for example: ['.-/']
                encoded_message.append("".join(morse_character))
                # /-----------------------empties the array so the next morse character can be added with '/'
                morse_character = []
    # /----------------joins each letter (in morse code format) to get one string and returns it
    return "".join(encoded_message)


# ..../...././...././.--/---|...././.--/-/---|....|

def morse_code_de(message):
    """takes the user input of message and changes the word/s (in morse code format) to normal text"""
    decoded_message = []
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    check_value = dict(zip(morse, alphabet))  # {'.-': 'a', '-...': 'b'... joins both lists into dictionary
    # /----------------------creates a list containing each word as a separate object
    word_list = list(message.split("|"))
    # /-----------------------removes the empty object that is after '|' which is created when the array is split
    word_list.remove('')
    # /----------------------counts how many words there are
    number_of_words = len(word_list)
    # /----------------------runs the loop one more time than there is words
    for w in range(0, number_of_words):
        # /------------------for every word
        word = word_list[w]
        # /------------------creates a list containing each letter as a separate object
        letters_in_word = word.split("/")
        # /------------------counts how many letters in the word
        number_of_letters = len(letters_in_word)
        # /----------------------runs the loop one more time than there is letters
        for l in range(0, number_of_letters):
            # /-------------------if the letter is the last letter in the word
            if l == number_of_letters - 1:
                # /----------------------find the corresponding letter in the alphabet
                morse = check_value[letters_in_word[l]]
                # /----------------------adds " " at the end of the letter
                last_letter = morse.ljust(2)
                # /----------------------adds the letter with the " " to an array for example ['a ']
                decoded_message.append(last_letter)
            # /--------------------if the letter is not the last letter in the word
            else:
                # /----------------------find the corresponding letter in the alphabet
                morse = check_value[letters_in_word[l]]
                # /-----------------------adds the letter (in the alphabet) to the array
                decoded_message.append(morse)
    # /----------------------joins each letter (in the alphabet) to get one string and returns it
    return "".join(decoded_message)
