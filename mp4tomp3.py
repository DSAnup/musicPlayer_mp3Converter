import os
import pygame
from tkinter.filedialog import askdirectory
import moviepy.editor as mp
from tkinter import *


root = Tk()
root.minsize(300, 300)

listofsongs = []
index = 0

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp4"):

            listofsongs.append(files)
            print(files)

directorychooser()
for song in listofsongs:
    clip = mp.VideoFileClip(song)
    s = re.sub(r'\.mp4$', '', song)
    clip.audio.write_audiofile(s+'.mp3')
root.mainloop()