from tkinter import *
from gtts import gTTS
from playsound import playsound

root=Tk()
root.geometry ("350x300")
root.configure(bg='ghost white')
root.title("DataFlair - Text to Speech")

Label(root,text="Text to Speech",font="arial 20 bold",bg="white smoke").pack()
Label(root,text="DataFlair",font="arial 15 bold",bg="white smoke",width="20").pack(side=BOTTOM)

Msg=StringVar()
Label(root,text="Enter Text",font="arial 15 bold",bg="white smoke").place(x=20,y=60)

entry_field=Entry(root,textvariable=Msg,width="50")
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message=entry_field.get()
    speech=gTTS(text=Message)
    speech.save("DataFlair.mp3")
    playsound("DataFlair.mp3")
def Exit():
    root.destroy()
def Reset():
    Msg.set("")

Button(root,text="Play",font="arial 15 bold",command=Text_to_speech,width="4").place(x=25,y=140)
Button(root,text="Exit",font="arial 15 bold",command=Exit,width="4").place(x=100,y=140)
Button(root,text="RESET",font="arial 15 bold",command=Reset,width="6").place(x=175,y=140)

root.mainloop()
