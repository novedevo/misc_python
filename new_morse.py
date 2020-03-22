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

DURATION_DICT = {'.':1, '-':3}

random_length = 20
pitch = 550
speed = 16
farnspeed = 8

speed = 1/(speed/1000)
farnspeed = 1/(farnspeed/1000)

def string_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def alpha_to_morse(stri):
    output = [pure_alpha_to_morse(word) for word in stri.upper().split()]
    print(output)

    for word in output:
        for letter in word:
            for c in letter:
                winsound.Beep(pitch, int(DURATION_DICT[c]*speed))
                time.sleep(.001*speed)
            time.sleep(.003*farnspeed)
        time.sleep(.007*farnspeed)

def pure_alpha_to_morse(strin):
    lst = []
    for c in strin:
        try:
            lst.append(MORSE_CODE_DICT[c])
        except KeyError:
            print('you put a bad character, try again boi')
            break
    return lst

def random_morse():
    while True:
        raw = string_generator(random_length)
        #print(raw)
        lst = []
        for c in raw:
            morse_letter = MORSE_CODE_DICT[c]
            print(morse_letter)
            for d in morse_letter:
                winsound.Beep(pitch, int(DURATION_DICT[d]*speed))
            while True:
                if input().upper() == c:
                    print('yes')
                    break
                else:
                    print('no')
                    for d in morse_letter:
                        winsound.Beep(550, int(DURATION_DICT[d]*speed))
                    continue
        if input('type anything for break'): break
        else: continue

while True:
    typ = input('what type; 0 for alpha to morse, 1 for morse to alpha, 2 for random morse: ')

    if typ == '0':
        alpha_to_morse(input('input string: '))
        
    elif typ == '1':
        pass #temp, in progress but i really dont care about this feature so itll never happen

    elif typ == '2':
        random_morse()
