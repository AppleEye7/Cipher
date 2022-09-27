# The phonetic alphabet is 26 words that correspond with the 26 letters of the alphabet.
# This means that each letter can be substituted for a phonetic word and vise versa.
# For the purpose of error prevention and since each letter in a word is a phonetic word itself

# the format of converting phonetic words to normal text (DECODING) is as follows: 'Tango Echo Sierra Tango. Oscar November Echo'
# -----------------------------------Output---------------------------------------:        test.                     one
# the program recognises that everything before the ". " is part of one word, so it prints the decoded message accurately.

# the format of converting normal text to phonetic words(ENCODING) is as follows: 'test one'
# ------------------------------------Output--------------------------------------:Tango Echo Sierra Tango. Oscar November Echo
# the program recognises that " " separates words so that it can access each word individually and print the encoded message accurately.

# The phonetic words are capitalised because that is the way they are written in the real word, so it makes it consistent for users.


# takes phonetic words from user and converts them to normal text: 'Tango Echo Sierra Tango. Oscar November Echo' ---> test one
def Phonetic_Alp_de(message):
    # global alphabet_letter
    # list of all 26 words in the phonetic alphabet words with some typos to account for user error 
    phonetics = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                 "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                 "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Xray", "Yankee", "Zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "q", "r",
                "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(phonetics, alphabet))  # {'Alpha': 'a', 'Bravo': 'b'... joins both lists into dictionary
    decoded_word = []
    # /----------------------splits message into separate words
    alphabet_word_list = list(message.split(". "))
    number_of_alphabet_words = len(alphabet_word_list)
    # /----------------------for each word from user input
    for w in range(0, number_of_alphabet_words):
        # /----------------------for each word in the user input list of words
        alphabet_word = alphabet_word_list[w]
        # /----------------------splits each word into the letters(phonetic words) ie  "Tango Hotel Echo" ---> "Tango","Hotel","Echo"
        phonetic_word_list = alphabet_word.split(" ")
        number_of_phonetic_words = len(phonetic_word_list)
        # /----------------------for each letter in the word
        for l in range(0, number_of_phonetic_words):
            # /------------------for each letter in the letter list
            phonetic_word = phonetic_word_list[l]
            # /-----------------------if it is the last letter
            if l == number_of_phonetic_words - 1:
                # /-----------------------for the phonetic word find the corresponding letter in alphabet list
                alphabet_letter = check_value[phonetic_word]
                # /-----------------------adds " " at the end of decoded letter
                last_alphabet_letter = alphabet_letter.ljust(2)
                # /------------------------add decoded letter to list
                decoded_word.append(last_alphabet_letter)
            else:
                # /----------------------for each phonetic word  find the corresponding letter in alphabet list
                alphabet = check_value[phonetic_word]
                # /-----------------------adds the decoded letter to list
                decoded_word.append(alphabet)
    # /-----------------------Return each letter with no space in between so that the letters become words and the first letter has " " in front
    # /--------input---------'Tango Echo Sierra Tango. Oscar November Echo'
    # /--------Output--------'test one '
    return "".join(decoded_word)


# takes one or more words from user and converts them to phonetic: test one --->Tango Echo Sierra Tango. Oscar November Echo
def Phonetic_Alp_en(message):
    phonetic_words_in_each_word_list = []
    phonetic_word_for_each_letter_in_word = []
    # list of all 26 words in the phonetic alphabet with some typos to account for user error 
    phonetics = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India",
                 "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Qbec", "Romeo",
                 "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Xray", "Yankee", "Zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "q", "r", "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(alphabet, phonetics))  # {'a': 'Alpha', 'b': 'Bravo', 'b'... joins both lists into dictionary
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(". "))
    number_of_words = len(word_list)
    # /----------------------for each word 
    for w in range(0, number_of_words):
        # /------------------for each word in the word list 
        word = word_list[w]
        number_of_letters = len(word)
        # /----------------------for every letter in each word
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
    # /------------joins each encoded word with ". " so the output is: Tango Echo Sierra Tango. Oscar November Echo. Tango Whiskey Oscar
    # /------------------------------------------------------------------first word-----------second word----------last word------
    return ". ".join(phonetic_words_in_each_word_list)
