import tkinter, string, sys
from tkinter import *

win = Tk()
def but1():
    print("Button1")
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=1)
b2.grid(row=0, column=3)
b1.configure(command=but1)
win.mainloop()


while 1:
    print('')
    unSimpli = '0'
    version = input("For yeetish traditional, type 1, for simplified, type 0: ")
    if version == '1':
        input1 = input('Enter text: ')
        for i, c in enumerate(input1):
            eCount = ord(c)
            yote = ("y") + ("e" * eCount) + ('t')
            sys.stdout.write(yote)
            sys.stdout.flush()
    elif version == '0':
        input2 = input('Enter alphabetical text: ')
        input3 = input2.split()
        for i in input3:
            input4 = i.lower()
            for i, c in enumerate(input4):
                eCount = ord(c) - 95
                if eCount<1 or eCount>26:
                    if unSimpli == '0':
                        sys.stdout.write('That isn\'t simplified. Try again. ')
                        sys.stdout.flush()
                        unSimpli = '1'
                else:
                    yate = ("y") + ("e" * eCount) + ('t')
                    sys.stdout.write(yate)
                    sys.stdout.flush()
                    
            sys.stdout.write(' ')
            sys.stdout.flush()

    else:
        print('I see you are bad at following instructions')
