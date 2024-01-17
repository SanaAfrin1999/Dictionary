from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

#  SEARCH BUTTON
def search():
    data = json.load(open('data.json'))
    word = enterwordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textarea.delete(1.0, END)
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')

    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
        if res == True:
            enterwordEntry.delete(0, END)
            enterwordEntry.insert(END, close_match)
            meaning = data[close_match]
            textarea.delete(1.0, END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', "The word doesnt exist, Please double check it.")
            enterwordEntry.delete(0, END)
            textarea.delete(1.0, END)

    else:
        messagebox.showinfo('Information', "The word doesnt exist")
        enterwordEntry.delete(0, END)
        textarea.delete(1.0, END)



#CLEAR BUTTON

def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0, END)

#EXIT BUTTON

def exit():
    res = messagebox.askyesno("Confirm", "Do you want to exit")
    if res == True:
        root.destroy()
    else:
        pass

#SEARCH MIC BUTTON
def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()


#MEANING MIC BUTTON

def meaningaudio():
    engine.say(textarea.get(1.0, END))
    engine.runAndWait()

####################################################################################################################


root = Tk()
root.geometry("612x612+100+30")
root.title("TALKING DICTIONARY")
root.resizable(0, 0)
bgimage = PhotoImage(file='dict.png')
bglable = Label(root, image=bgimage)
bglable.place(x=0, y=0)

enterwordlable = Label(root, text="ENTER WORD", font=('castellar', 29, 'bold'),
                       fg='brown', bg='whitesmoke')
enterwordlable.place(x=300, y=20)

enterwordEntry = Entry(root, font='arial 23 bold', justify=CENTER, bd=8, relief=GROOVE)
enterwordEntry.place(x=240, y=80)

searchimage = PhotoImage(file='search2.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                      command=search)
searchButton.place(x=320, y=150)

micimage = PhotoImage(file='mic3.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=wordaudio)
micButton.place(x=420, y=153)

meaninglable = Label(root, text="MEANING", font=('castellar', 29, 'bold'),
                     fg='brown', bg='whitesmoke')
meaninglable.place(x=300, y=240)

textarea = Text(root, width=48, height=8, font='arial 12 bold', bd=8, relief=GROOVE, )
textarea.place(x=150, y=300)

audioimage = PhotoImage(file='mic3.png')
audioButton = Button(root, image=audioimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=meaningaudio)
audioButton.place(x=250, y=500)

clearimage = PhotoImage(file='delete.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=clear)
clearButton.place(x=350, y=500)

exitimage = PhotoImage(file='exit2.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=exit)
exitButton.place(x=450, y=500)


def enter_function(event):
    searchButton.invoke()


root.bind('<Return>', enter_function)

root.mainloop()
