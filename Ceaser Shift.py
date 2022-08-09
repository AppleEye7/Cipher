#Caesar shift
import string
shift = 2
message = "hello there person"

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
encoded = message.translate(table)
print(encoded)
