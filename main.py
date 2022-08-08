#Caesar shift
import string
shift = 2
message = "hello there"
class Caesar_shift(shift, message):

    def encode(shift, message):
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)
        encoded = message.translate(table)
        return(encoded)


cipher = Caesar_shift(shift)
print(cipher.encode(message))
