phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
             "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
             "Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]
check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie'......

word = input("Please enter your word:\n ")

for k, v in check_value.items():
    for letter in word:
        if letter == k:
            print(v)



