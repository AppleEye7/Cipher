def Phonetic_Alp_de(message):
    global alphabet_letter
    phonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india",
                 "juliet","kilo","lima","mike","november","oscar","papa","quebec", "qbec", "romeo",
                 "sierra","tango","uniform","victor","whiskey","x-ray", "xray", "yankee","zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "q", "r",
                "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(phonetics, alphabet)) # {'Alpha': 'a', 'Bravo': 'b'... joins both lists into dictionary
    decoded_word = []
    # /----------------------Creates a list containing each word when decoded as a separate object
    alphabet_word_list = list(message.split(". "))
    number_of_alphabet_words = len(alphabet_word_list)
    # /----------------------w = 0 each loop w + 1 until it is the amount of objects in wordlist
    for w in range(0,number_of_alphabet_words):
        alphabet_word = alphabet_word_list[w]
    # /----------------------splits each word into the letters ie  "Tango Hotel Echo" ---> "Tango","Hotel","Echo"
        phonetic_word_list = alphabet_word.split(" ")
        number_of_phonetic_words = len(phonetic_word_list)
    # /----------------------l = 0 each loop l + 1 until it is the amount of objects in letters_list
        for l in range(0, number_of_phonetic_words):
            phonetic_word = phonetic_word_list[l]
    # /-----------------------if there is more than one word when decoded
            if w > 0:
    # /-----------------------for each phonetic word find the corresponding letter in alphabet list
                alphabet_letter = check_value[phonetic_word]
                #print(alphabet_letter)
    # /-----------------------adds a " " to the front of decoded letter
                first_alphabet_letter = alphabet_letter.rjust(2)
    # /------------------------add decoded letter to list
                decoded_word.append(first_alphabet_letter)
            else:
    # /----------------------For each word to become letter.  alphabet = the corresponding letter in alphabet
                alphabet = check_value[phonetic_word]
    # /-----------------------Adds the letter to a list
                decoded_word.append(alphabet)
    # /-----------------------Return each letter with no space in between
    return"".join((decoded_word))

def Phonetic_Alp_en(message):
    phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
                 "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
                 "Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'b'... joins both lists into dictionary
    phonetic_word_in_each_words_list = []
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    # /----------------------w = 0 each loop w + 1 until it is the amount of words in wordlist
    for w in range(0,number_of_words):
        word = word_list[w]
        number_of_letters = len(word)
    # /----------------------i = 0 each loop i + 1 until it is the amount of letters in each word
        for l in range(0,number_of_letters):
            letter = word[l]
    # /----------------------For each letter phonetic = the corresponding word in phonetics
            phonetic = check_value[letter]
            phonetic_word_in_each_words_list.append(phonetic)
        phonetic_word_in_each_words = (" ".join(phonetic_word_in_each_words_list))
        phonetic_word_in_each_words.insert(number_of_letters +1,". ")
        # /-----------------------Return each phonetic word with a space in between
    return("".join(phonetic_word_in_each_words))

#hello there person
