""" The phonetic alphabet is 26 words that correspond with the 26 letters of the alphabet.
This means that each letter can be substituted for a phonetic word and vise versa.
In the phonetic alphabet the format is: words are separated by ". " and letters are separated by " "
"""
# /-------------------this is outside the function so the program can check if the input message contains phonetic words
phonetic_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                     "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                     "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Xray", "Yankee", "Zulu"]


def phonetic_alp_en(message):
    """takes word/s from user and converts them to phonetic words in the correct format"""
    phonetic_words_in_each_word_list = []
    phonetic_word_for_each_letter_in_word = []
    # /----------------------list of all 26 letters and the phonetic alphabet with some typos to account for user error
    phonetics = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                 "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                 "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Xray", "Yankee", "Zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "q", "r", "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(alphabet, phonetics))  # {'a': 'alpha', 'b': 'Bravo', 'b'... joins both lists into dictionary
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    # /----------------------counts how many words there are
    number_of_words = len(word_list)
    # /----------------------runs the loop one more time than there is words
    for w in range(0, number_of_words):
        # /------------------for each word
        word = word_list[w]
        # /------------------counts how many letters in the word
        number_of_letters = len(word)
        # /----------------------runs the loop one more time than there are letters
        for l in range(0, number_of_letters):
            # /------------------for each letter in the word
            letter = word[l]
            # /----------------------For each letter in the user input word: find the corresponding phonetic word
            phonetic = check_value[letter]
            # /----------------------add that phonetic word to list
            phonetic_word_for_each_letter_in_word.append(phonetic)
            # /----------------------if the letter is the last in the word
            if l == number_of_letters - 1:
                # /----------------------join the encoded letters together so there is " " between them
                encoded_word = (" ".join(phonetic_word_for_each_letter_in_word))
                # /----------------------adds the encoded word to list
                phonetic_words_in_each_word_list.append(encoded_word)
                # /----------------------makes the list empty for the next user input word
                phonetic_word_for_each_letter_in_word = []
            else:
                continue
    # /------------joins each encoded word with ". " and returns as one string
    return ". ".join(phonetic_words_in_each_word_list)


def phonetic_alp_de(message):
    """takes phonetic words from user and converts them to normal text"""
    shift_num = 2
    # /----------------------list of all 26 letters and the phonetic alphabet with some typos to account for user error
    phonetics = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                 "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                 "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-Ray", "Xray", "Yankee", "Zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "q", "r",
                "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(phonetics, alphabet))  # {'alpha': 'a', 'Bravo': 'b'... joins both lists into dictionary
    decoded_word = []
    # /----------------------splits message into separate words
    alphabet_word_list = list(message.split(". "))
    # /----------------------counts how many words there are
    number_of_alphabet_words = len(alphabet_word_list)
    # /----------------------runs the loop one more time than there are words
    for w in range(0, number_of_alphabet_words):
        # /----------------------for each word
        alphabet_word = alphabet_word_list[w]
        # /----------------------splits each word into the letters(phonetic words) ie  "Tango Hotel Echo" ---> "Tango","Hotel","Echo"
        phonetic_word_list = alphabet_word.split(" ")
        # /------------------counts how many letters in the word
        number_of_phonetic_words = len(phonetic_word_list)
        # /----------------------runs the loop one more time than there are letters
        for l in range(0, number_of_phonetic_words):
            # /------------------for each letter in the letter list
            phonetic_word = phonetic_word_list[l]
            # /-----------------------if it is the last letter
            if l == number_of_phonetic_words - 1:
                # /-----------------------for the phonetic word find the corresponding letter in alphabet list
                alphabet_letter = check_value[phonetic_word]
                # /-----------------------length of the letter + 1
                # /-----------------------adds " " at the end of the decoded letter
                last_alphabet_letter = alphabet_letter.ljust(shift_num)
                # /------------------------add decoded letter to list
                decoded_word.append(last_alphabet_letter)
            else:
                # /----------------------for each phonetic word find the corresponding letter in the alphabet
                alphabet = check_value[phonetic_word]
                # /-----------------------adds the decoded letter to list
                decoded_word.append(alphabet)
    # /-----------------------Returns the original message in normal text format
    return "".join(decoded_word)
