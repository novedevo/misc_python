"""Converts from natural language to yeetish, e.g.(simplified) a=yeet, b=yeeet,
c=yeeeet, etc. Also has funtionality for traditional, which includes the entire
UTF-8 charset, reverse translation, and text to speech through google translate api.
"""

import sys
import string
import PySimpleGUI as sg
from gtts import gTTS
from playsound import playsound

form = sg.FlexForm('Yeet')

layout = [
           [
               sg.Radio('Simplified', "RADIO1", default=True, key='simp'),
               sg.Radio('Traditional', "RADIO1", key='trad'),
               sg.Radio('Reverse', "RADIO1", key='rvrs'),
               sg.Radio('Text to Speech (alpha)', "RADIO1", key='yts')
           ],
           
           [sg.Txt('Text to be translated')],
           [sg.In(size=(80,4), key='text')],
           [sg.Txt('KEEP EASYPRINT WINDOW OPEN')],
           [sg.ReadFormButton('Translate', bind_return_key=True)]
         ]

form.Layout(layout)

def gudPrint(lst):
    """Succintly prints a string from a list to the EasyPrint module"""
    finalPrint = ''.join(lst)
    sg.EasyPrint(finalPrint)
    #finalPrint = ''

def countEsAndReturn(writ,lst,simple):
    """Appends a yeet with corresponding e's to the string"""
    for c in writ:
        print(c)
        print(' ')
        eCount = ord(c)
        if simple:
            eCount = eCount-95
            if (eCount<2 or eCount>27) and unSimpli:
                sg.EasyPrint("That isn't simplified. Try again.")
                unsimpli = False
                break
        lst.append(("y") + ("e" * eCount) + ('t'))

while True:
    button, values = form.Read()
    #get info from form

    if button is not None:
        unSimpli = True  #variable reset
        yeetList = []
        if values['trad']:
            yeetList.append('yaad')    #to signify traditional
            countEsAndReturn(values['text'],yeetList,False)
            gudPrint(yeetList)

        elif values['simp']:
            yeetList.append('ybbd')    #to signify simplified
            input3 = values['text'].split()
            for i in input3:
                countEsAndReturn(i.lower(),yeetList,True)
                yeetList.append(' ')
            gudPrint(yeetList)
            
        elif values['rvrs'] == True:
            yeetishRaw = values['text']
            if yeetishRaw.count('a') == 2:
                yeetishRaw.split[4:]('y').pop(0)
                newerYeet = [chr(i.count('e')) for i in yeetishRaw if i.count('e')>1]
                gudPrint(newerYeet)

            elif yeetishRaw.count('b') == 2:
                newYeet = []          #create variable to store list of unyeeted
                words = [word.split('y') for word in yeetishRaw[4:].split()]
                for word in words:
                    word.pop(0)
                    newYeet.append(''.join([chr(y.count('e')+95) for y in word]))
                    newYeet.append(' ')
                newYeet.pop()
                gudPrint(newYeet)
                
        elif values['yts'] == True:          ####EXPERIMENTAL, ALPHA, PARTIALLY BROKEN
            yeetishRaw = values['text']
            tts = gTTS(yeetishRaw, lang = 'en')
            tts.save('yeet.mp3')
            playsound('yeet.mp3')
            tts = 0
            
        else:         #if version number has no parser
            sg.EasyPrint('I see you are bad at following instructions')

    else:
        break
