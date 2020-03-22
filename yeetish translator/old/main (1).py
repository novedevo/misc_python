import string
while 1:

    version = input("For yeetish traditional, type 1, for simplified, type 0: ")
    if version == '1':
        input1 = input('enter your original text: ')
        for i, c in enumerate(input1):
            eCount = ord(c)
            yote = ("y") + ("e" * eCount) + ('t')
            print(yote)
    elif version == '0':
        input2 = input('enter your original text: ')
        if input2.isalnum():
            input3 = input2.lower()
            for i, c in enumerate(input2):
                eCount = ord(input3) - 95
                yate = ("y") + ("e" * eCount) + ('t')
                print(yate)
        else:
            print('that doesnt seem very simplified to me')
    else:
        print('i see you are bad at following instructions')
#known issues: numbers break simplified version