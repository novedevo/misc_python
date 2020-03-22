#import the 'tkinter' module
import tkinter
#create a new window
window = tkinter.Tk()

def ent1(a):
    if a == 1:
        print(1)

#create a label widget called 'lbl'
lbl = tkinter.Label(window, text="For yeetish traditional enter 1, for simplified enter 0")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text='Enter', command = ent1(ent))

lbl.pack()
ent.pack()
btn.pack()

#draw the window, and start the 'application'
window.mainloop()
    
