# morse code is a cipher where each letter is a series of dots and/or dashes.
# Words are separated by slashes (|) and letters in each word separated by (/)
def morse_code_en(message):
    last_letter = []
    morse_letter = []
    encoded_message = []
    """takes user input of letters and turns it into morse code"""
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
             ".----", "..---", "...-- ", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check_value = dict(zip(alphabet, morse))  # {'a': '.-', 'b': '-...'... joins both lists into dictionary
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    # /----------------------for every word
    for w in range(0, number_of_words):
        # /------------------for each word from the user input
        word = word_list[w]
        number_of_letters = len(word)
        # /----------------------for every letter
        for l in range(0, number_of_letters):
            # /--------------for each letter in the word
            letter = word[l]

            # /---------making the display of the morse code with \ separating letters and | separating words--------- \

            # /--------------if it is the last letter------------------------------------------------------------------\
            if l == number_of_letters - 1:
                # /----------------------finds the corresponding morse translation for the letter
                last_letter_morse = check_value[letter]
                # /----------------------adds the morse letter to an array
                last_letter.append(last_letter_morse)
                # /-----------------------adds '|' to the array with the morse letter
                last_letter.append('|')
                # /-----------------------adds '|' to the end of the morse letter

                # /-----------------------adds the morse letter to the array
                encoded_message.append("".join(last_letter))
            else:
                # /----------------------finds the corresponding morse translation for the letter
                morse = check_value[letter]
                morse_letter.append(morse)
                # /-----------------------adds '/' to the array with the morse letter
                morse_letter.append('/')
                # /-----------------------adds '/' to the end of the morse letter
                morse_letter_joined = ''.join(morse_letter)
                # /-----------------------adds the morse letter to the array
                encoded_message.append(morse_letter_joined)
    # /----------------Returns each letter in each word (now translated into morse code) with a space between
    return "".join(encoded_message)


def morse_code_de(message):
    decoded_message = []
    global number_of_letters
    global letters_in_word
    """takes user input of dots and dashes and turns it into normal text"""
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    check_value = dict(zip(morse, alphabet))  # {'.-': 'a', '-...': 'b'... joins both lists into dictionary
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split("|"))
    number_of_words = len(word_list)
    # /----------------------for each word
    for w in range(0, number_of_words):
        # /------------------for every word
        word = word_list[w]
        # /------------------find each letter
        letters_in_word = word.split("/")
        number_of_letters = len(letters_in_word)
    # /----------------------for every morse letter
    for l in range(0, number_of_letters):
        # /-------------------if it is the last letter
        if l == number_of_letters:
            # /----------------------For each morse letter find the corresponding letter in the alphabet
            morse = check_value[letters_in_word[l]]
            # /----------------------adds " " at the end of the letter
            last_letter = morse.ljust(2)
            decoded_message.append(last_letter)
            # /----------------------For each morse letter find the corresponding letter in the alphabet
        else:
            morse = check_value[letters_in_word[l]]
            decoded_message.append(morse)
    # /----------------------Returns each letter in each word with a space between
    return " ".join(decoded_message)
