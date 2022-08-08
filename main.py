#Caesar shift
import string
shift = 2
message = "hello there persom"

choice = int(input("1.encode\n2.decode\n"))
if choice == 1:
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encoded = message.translate(table)
    print(encoded)
else:
    print("hi")
