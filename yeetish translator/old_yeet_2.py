import PySimpleGUI as sg
import sys
import string
from gtts import gTTS
from playsound import playsound

form = sg.FlexForm('Yeet')


layout = [
           [sg.Radio('Simplified', "RADIO1", default=True, key='simp'), sg.Radio('Traditional', "RADIO1", key='trad'), sg.Radio('Reverse', "RADIO1", key='rvrs'), sg.Radio('Text to Speech', "RADIO1", key='yts')],
           [sg.Txt('Text to be translated')],
           [sg.In(size=(80,4), key='text')],
           [sg.Txt('KEEP EASYPRINT WINDOW OPEN')],
           [sg.ReadFormButton('Translate', bind_return_key=True)]]

form.Layout(layout)

def gudPrint(lst):
    finalPrint = ''.join(lst)
    sg.EasyPrint(finalPrint)
    finalPrint = ''

def countEsAndReturn(writ,lst,simple):
    for c in writ:
        print(c)
        print(' ')
        eCount = ord(c)
        if simple:
            eCount = eCount-95
            if (eCount<2 or eCount>27) and unSimpli:
                sg.EasyPrint('That isn\'t simplified. Try again.')
                unsimpli = False
                break
        lst.append(("y") + ("e" * eCount) + ('t'))

while True:
    button, values = form.Read()    #get info from form

    if button is not None:
        unSimpli = True  #variable reset
        yeetList = []
        if values['trad']:
            yeetList.append('yaad') #signifies traditional or simplified
            countEsAndReturn(values['text'],yeetList,False)
            gudPrint(yeetList)

        elif values['simp']:
            yeetList.append('ybbd')
            input3 = values['text'].split()
            for i in input3:
                countEsAndReturn(i.lower(),yeetList,True)
                yeetList.append(' ')
            gudPrint(yeetList)
            
        elif values['rvrs'] == True:
            yeetishRaw = values['text']
            if yeetishRaw.count('a') == 2:
                yeetishRaw = yeetishRaw[4:]
                indieYeet = yeetishRaw.split('y')
                indieYeet.pop(0)       #remove null initial index from array
                newerYeet = []
                for i in indieYeet:
                    if i.count('e') > 1:            #to not parse initial version signifier
                        countable = chr(i.count('e'))
                        newerYeet.append(countable)
                gudPrint(newerYeet)

            elif yeetishRaw.count('b') == 2:
                yeetishRaw = yeetishRaw[4:]
                ##words = yeetishRaw.split()
                newYeet = []    #create variable to store list of unyeeted
                words = [word.split('y') for word in yeetishRaw.split()]
                ##nyewYeet.pop(0)
                ##print(nyewYeet)
                for word in words:
                    #indieYeet = word.split('y')
                    word.pop(0)
                    for y in word:
                        countE = y.count('e')
                        countE = countE + 95
                        newYeet.append(chr(countE))
                    newYeet.append(' ')
                gudPrint(newYeet)
                
        elif values['yts'] == True:
            yeetishRaw = values['text']
            tts = gTTS(yeetishRaw, lang = 'en')
            tts.save('yeet.mp3')
            playsound('yeet.mp3')
            tts = 0
            
        else:       #if version number has no parser
            sg.EasyPrint('I see you are bad at following instructions')

    else:
        break
