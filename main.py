
while True:
    choicenum = int(input("Welcome to cipher\nWhat do you want to do?\n"
                          "(please chose corresponding number)\n1.Encode\n2.Decode\n3.Quit\n"))
    if choicenum == 1:
        choice = "encode"
    elif choicenum == 2:
        choice = "decode"
    elif choicenum == 3:
        break
    ciphernum = int(input("Chose the cipher you would like to use to {} your message\n"
                          "(please chose corresponding number)\n1.Caesar Shift\n2.Pigpen\n3.Phonetic Alphabet\n4.Quit\n5.Home\n".format(choice)))
    if ciphernum == 1:
        cipher = "Caesar Shift"
    elif ciphernum == 2:
        cipher = "Pigpen"
    elif ciphernum == 3:
        cipher = "Phonetic Alphabet"
    elif ciphernum == 4:
        break
    elif ciphernum == 5:
        continue
    message = int(input("You chose {} to {} your message\nEnter message without using numbers (ei one,three)\n"
                        "(Chose corresponding number if needed)\n1.Quit \n2.Home\n".format(cipher choice)))
    if message =
