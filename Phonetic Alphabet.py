def Phonetic_Alp_de(message):
    phonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india",
                 "juliet","kilo","lima","mike","november","oscar", "papa","quebec", "qbec", "romeo",
                 "sierra","tango","uniform","victor","whiskey","x-ray","xray","yankee","zulu"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "q", "r", "s", "t", "u", "v", "w", "x", "x", "y", "z"]
    check_value = dict(zip(phonetics, alphabet)) # {'Alpha': 'a', 'Bravo': 'b'... joins both lists into dictionary
    decoded_message = []
    # /----------------------Creates a list containing each word when decoded as a separate object
    word_list = list(message.split(". "))
    print(word_list)
    number_of_words = len(word_list)
    # /----------------------w = 0 each loop w + 1 until it is the amount of objects in wordlist
    for w in range(0,number_of_words):
        word = word_list[w]
        letters_in_word = word.split(" ")
        amount_letters_in_word = len(letters_in_word)
    for l in range(0, amount_letters_in_word):
        letter = letters_in_word[l]
    # /----------------------For each word alphabet = the corresponding letter in alphabet
        alphabet = check_value[letter]
    # /-----------------------Adds the letter to a list
        decoded_message.append(alphabet)
    # /-----------------------Return each letter with a space in between
    return("".join(decoded_message))

def Phonetic_Alp_en(message):
    phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
                 "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
                 "Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'b'... joins both lists into dictionary
    encoded_message = []
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    # /----------------------w = 0 each loop w + 1 until it is the amount of words in wordlist
    for w in range(0,number_of_words):
        word = word_list[w]
        number_of_letters = len(word)
    # /----------------------i = 0 each loop i + 1 until it is the amount of letters in each word
        for i in range(0,number_of_letters):
            letter = word[i]
    # /----------------------For each letter phonetic = the corresponding word in phonetics
            phonetic = check_value[letter]
    # /-----------------------Return each phonetic word with a space in between
            encoded_message.append(phonetic)
    return(" ".join(encoded_message))
