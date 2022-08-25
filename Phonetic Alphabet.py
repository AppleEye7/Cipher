phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
             "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
             "Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]
check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie'......
newlist = []
i = 0
w = 0
# l == the leter
# i == index number of letter
#w == word in wordlist
inputword = input("Please enter your word:\n").lower()
wordlist = list(inputword.split(" "))

for alphabet, phonetics in check_value.items():
    word = wordlist[w]
    if i == len(word):
        w += 1
        i = 0
    if w == len(wordlist):
        break
    for l in alphabet:
        if l == word[i]:
            newlist.append(check_value[word[i]])
        else:
            newlist.append(check_value[word[i]])
        i += 1
    # for second word it repeats second letter twice

print(" ".join(newlist))

