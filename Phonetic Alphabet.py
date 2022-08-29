
def Phonetic_Alp_de(message):
    phonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india",
                 "juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo",
                 "sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(phonetics,alphabet )) # {'Alpha': 'a', 'Bravo': 'b'... joins both lists into dictionary
    decoded_message = []
    # /----------------------Creates a list containing each word as a separate object
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    for w in range(0,number_of_words):
        word = word_list[w]
        alphabet = check_value[word]
        decoded_message.append(alphabet)
    return("".join(decoded_message))

def Phonetic_Alp_en(message):
    phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
                 "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
                 "Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'b'...
    encoded_message = []
    word_list = list(message.split(" "))
    number_of_words = len(word_list)
    for w in range(0,number_of_words):
        word = word_list[w]
        number_of_letters = len(word)
        for i in range(0,number_of_letters):
            letter = word[i]
            phonetic = check_value[letter]
            encoded_message.append(phonetic)
    return(" ".join(encoded_message))
