import string
import sys
while 1:
    print('')
    version = input("For yeetish traditional, type 1, for simplified, type 0: ")
    if version == '1':
        input1 = input('enter your original text: ')
        for i, c in enumerate(input1):
            eCount = ord(c)
            yote = ("y") + ("e" * eCount) + ('t')
            sys.stdout.write(yote)
            sys.stdout.flush()
    elif version == '0':
        input2 = input('enter your original text: ')
        if input2.isalnum():
            input3 = input2.lower()
            for i, c in enumerate(input2):
                eCount = ord(c) - 95
                yate = ("y") + ("e" * eCount) + ('t')
                sys.stdout.write(yate)
                sys.stdout.flush()
        else:
            print('that doesnt seem very simplified to me. simplified requires alphanumeric, no spaces')
    else:
        print('i see you are bad at following instructions')
#known issues: numbers break simplified version
