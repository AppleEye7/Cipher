def Morse_Code_en(message):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(alphabet, morse)) # {'a': '.-', 'b': '-...'... joins both lists into dictionary
    encoded_message = []
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    # /----------------------w = 0 each loop w + 1 until it is the amount of words in wordlist
    for w in range(0,number_of_words):
        word = word_list[w]
        number_of_letters = len(word)
    # /----------------------l = 0 each loop l + 1 until it is the amount of letters in each word
        for l in range(0,number_of_letters):
            letter = word[l]
    # /----------------------For each letter in each word Morse = the corresponding letter in morse list
            Morse = check_value[letter]
            encoded_message.append(Morse)
    # /----------------------Returns each letter in each word with a space between
    return(" ".join(encoded_message))

def Morse_Code_de(message):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(morse, alphabet)) # {'.-': 'a', '-...': 'b'... joins both lists into dictionary
    decoded_message = []
    # /----------------------Creates a list containing each letter as a separate object
    letter_list = list(message.split(" "))
    number_of_letters = len(letter_list)
    # /----------------------l = 0 each loop l + 1 until it is the amount of letters in letter_list
    for l in range(0,number_of_letters):
    # /----------------------For each letter in list Morse = the corresponding letter in morse list
        Morse = check_value[letter_list[l]]
        decoded_message.append(Morse)
    # /----------------------Returns each letter in each word with a space between
    return(" ".join(decoded_message))

