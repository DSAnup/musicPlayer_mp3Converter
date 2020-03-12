import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3
root = Tk()
root.minsize(300, 300)

listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root, textvariable = v, width = 35)

index = 0

def playsong(event):
    global index
    print(index)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()



def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    # return songname

def updatelabel():
    global index
    # global songname
    v.set(listofsongs[index])
    # return songname

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            # realdir = os.path.realpath(files)
            # audio = ID3(realdir)
            # realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
            print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    # pygame.mixer.music.play()


directorychooser()

label = Label(root, text ="Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()
# realnames.reverse()

for items in listofsongs:
    listbox.insert(0, items)

# realnames.reverse()
listofsongs.reverse()

nextbutton = Button(root, text = 'Next Song')
nextbutton.pack()

prebutton = Button(root, text="Previous Song")
prebutton.pack()

playbutton = Button(root, text="Play Song")
playbutton.pack()

stopbutton = Button(root, text="Stop Song")
stopbutton.pack()

nextbutton.bind("<Button-1>", nextsong)
prebutton.bind("<Button-1>", prevsong)
playbutton.bind("<Button-1>", playsong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()

root.mainloop()