import winsound, random, time, string, itertools

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'
                    } 

SECONDARY_DICT = { '.':1, '-':3}

def string_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def alpha_to_morse(string):
    output = []

    for word in string.upper().split():
        new = []
        for c in word:
            try:
                new.append(MORSE_CODE_DICT[c])
            except KeyError:
                new.append(c)
        output.append(new)

    print(output)

    for word in output:
        for letter in word:
            for c in letter:
                winsound.Beep(550, int(SECONDARY_DICT[c]*speed))
                time.sleep(.001*speed)
            time.sleep(.003*farnspeed)
        time.sleep(.007*farnspeed)

def random_morse():
    while True:
        raw = string_generator(20)
        #print(raw)
        lst = []
        for c in raw:
            #print(c)
            a = MORSE_CODE_DICT[c]
            print(a)
            for i in a:
                winsound.Beep(550, int(SECONDARY_DICT[i]*speed))
            #time.sleep(.003*farnspeed)
            while True:
                if input().upper() == c:
                    print('yes')
                    break
                else:
                    print('no')
                    for i in a:
                        winsound.Beep(550, int(SECONDARY_DICT[i]*speed))
                    #time.sleep(.003*farnspeed)
                    continue
        if input('type anything for break'): break
        else: continue

speed = 16
farnspeed = 8

speed = 1/(speed/1000)
farnspeed = 1/(farnspeed/1000)

while True:

    output = []

    typ = input('what type; 0 for alpha to morse, 1 for morse to alpha, 2 for random morse: ')

    if typ == '0':
        alpha_to_morse(input('input string: '))
        
    elif typ == '1':
        pass

    elif typ == '2':
        random_morse()
