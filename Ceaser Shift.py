#Caesar shift
import string
shift = 2
message = "jgnnq vjgtg rgtuqp"

def Caear_shift_de(shift,message):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet,shifted)
    decoded = message.translate(table)
    print(decoded)

def Caear_shift_en(shift,message):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(shifted,alphabet)
    encoded = message.translate(table)
    print(encoded)

choicenum = 1
ciphernum = 1
if choicenum == 1 and ciphernum == 1:
    Caear_shift_en(shift,message)
elif choicenum == 2 and ciphernum == 1:
    Caear_shift_de(shift,message)
