i = 0

phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
             "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
             "Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]
check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie'......
newlist = []
# g == the leter
# i == index number of letter
word = input("Please enter your word:\n")
for alphabet, phonetics in check_value.items():
    if i == len(word):
        break
    for g in alphabet:
        if g == word[i]:
            print(g)
            print(i)
            new = check_value[g]
            newlist.append(new)
        print(g)
        i += 1
        g = alphabet[0]

print(newlist)
