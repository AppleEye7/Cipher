#Caesar shift
import string
shift = 2
message = "hello there persom"

choice = int(input("Welcome to cipher\nWhat do you want to do?\n(please chose corresponding number)\n1.Encode\n2.Decode\n3.Quit\n"))
if choice == 1:
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encoded = message.translate(table)
    print(encoded)
else:
    print("___")
