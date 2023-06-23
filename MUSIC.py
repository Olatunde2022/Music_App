import tkinter as tk
import os
from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
import pygame 
from pygame import mixer

canvas = tk.Tk()
canvas.title ("Music Player")
canvas.geometry("600x450")
canvas.config(bg= "black")
label=tk.Label(canvas, text="Music Player", font=("sudo",15, "bold"), fg="#F9F6EE", bg="#190b20").pack(side= "top")

rootpath = "C://Users/USER/Desktop/music"
pattern = "*.mp3"
mixer.init()

def play_prev():
    next_song =Playlist.curselection()
    next_song = next_song[0] -  1
    next_song_name = Playlist.get(next_song)
    label=Label(canvas, text="Now Playing: "+ next_song_name, font=("ds-digital",11), fg="#F9F6EE", bg="#190b20").place(x=70, y=300)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    Playlist.select_clear(0, "end")
    Playlist.activate(next_song)
    Playlist.select_set(next_song)

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    label=Label(canvas, text="Now Playing: "+ Music_Name, font=("ds-digital",11), fg="#F9F6EE", bg="#190b20").place(x=70, y=300)

def stop():
    mixer.music.stop()
    Playlist.select_clear("active")

def pause_song():
    global paused
    paused= True
    mixer.music.pause()
def play_next():
    next_song =Playlist.curselection()
    next_song = next_song[0] + 1
    next_song_name = Playlist.get(next_song)
    label=Label(canvas, text="Now Playing: "+ next_song_name, font=("ds-digital",11), fg="#F9F6EE", bg="#190b20").place(x=70, y=300)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    Playlist.select_clear(0, "end")
    Playlist.activate(next_song)
    Playlist.select_set(next_song)

current_volume = float(0.5)

def increase_volume():
    try:
        global current_volume
        if current_volume >=1:
            volume_label.config(fg="green", text="Volume : Max",font=("times new roman",15,"bold"))            
            return
        current_volume= current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text = "Volume : " +str(current_volume),font=("times new roman",15,"bold"))
    except  Exception as e:
        print(e)
        label.config(fg="red", text= "Track hasn't been selected yet ")

def reduce_volume():
    try:
        global current_volume
        if current_volume <=0:
            volume_label.config(fg="green", text="Volume : Muted")
            return
        current_volume= current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text = "Volume : " +str(current_volume))
    except  Exception as e:
        print(e)
        label.config(fg="red", text= "Track hasn't been selected yet ")

    #Define palyer control image
prev_img = PhotoImage(file= "prev1.png")
stop_img = PhotoImage(file= "stop1.png")
play_img = PhotoImage(file= "play11.png")
pause_img = PhotoImage(file= "pause1.png")
next_img = PhotoImage(file= "next1.png")
bg_img = PhotoImage(file= "bg1.png")

label= Label(canvas, image=bg_img).place(x=0, y= 30)
volume_label = Label(canvas,font=("Calibri",12),fg="#F9F6EE", bg="#190b20")
volume_label.pack(side= "bottom")

Frame_Music = Frame(canvas, bd=2, relief = RIDGE)
Frame_Music.place(x=18, y=40, width=580, height=250)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",15), bg="#333333", fg="cyan", selectbackground="#190b20", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

 #Buttons
Button(canvas, text="Add Music", width=8, height=1, font=('sans',10,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=18, y=13)
PrevButton= tk.Button(canvas, text="Prev", image= prev_img, bg= "black", borderwidth = 0, command=play_prev).place(x=120, y=350)
Button(canvas, image= play_img,text= "Play", bg="#0f1a2b", bd=0, command=Play_Music).place(x=185, y=350)
stopButton= tk.Button(canvas, text="Stop", image= stop_img, bg= 'black', borderwidth = 0, command= stop).place(x=250, y=350)
pauseButton= tk.Button(canvas, text="Pause", image= pause_img, bg= "black", borderwidth = 0, command=pause_song).place(x=315, y=350)
nextButton= tk.Button(canvas, text="Prev", image= next_img, bg= "black", borderwidth = 0, command= play_next).place(x=380, y=350)
volumeButton = tk.Button(canvas,   text= "Vol +", font=("ds-digital",12), fg="#F9F6EE", bg="#190b20", borderwidth= 0, command= increase_volume).place(x=500, y=330)
volumeButton = tk.Button(canvas,   text= "Vol -", font=("ds-digital",12), fg="#F9F6EE", bg="#190b20", borderwidth= 0, command=reduce_volume).place(x=20, y=330)

canvas.mainloop()