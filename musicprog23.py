 # -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:38:37 2023

@author: shiva
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("425x300")
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # # # Load and display the background image
        img = Image.open("blkmsc.jpg")
        img = img.resize((500, 500), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(img)
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower()  # place the background label behind all other widgets

        
        # Create label for displaying the current playing file
        self.current_file_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.current_file_label.place(x=10, y=100)
        
        # Create buttons
        self.play_button = ttk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.place(x=125, y=150)
        
        
        self.pause_button = ttk.Button(self.master, text="Pause", command=self.pause_music)
        self.pause_button.place(x=225, y=150)
        
        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.place(x=325, y=150)
        
        self.browse_button = ttk.Button(self.master, text="Browse", command=self.browse_file)
        self.browse_button.place(x=25, y=150)
        
        self.previous_button = ttk.Button(self.master, text="Previous", command=self.previous_song)
        self.previous_button.place(x=75, y=200)
        
        self.next_button = ttk.Button(self.master, text="Next", command=self.next_song)
        self.next_button.place(x=175, y=200)
        
        
        self.view_queue_button = ttk.Button(self.master, text="View Queue", command=self.view_song_queue)
        self.view_queue_button.place(x=275, y=200)
        
        # Create volume control
        self.volume_slider = ttk.Scale(self.master, from_=0, to=1, orient=tk.HORIZONTAL, length=200, command=self.change_volume)
        self.volume_slider.set(0.5)
        self.volume_slider.place(x=125, y=250)
        
        # Initialize music file path, music queue, and current song index
        self.music_file_path = ""
        self.music_queue = []
        self.current_song_index = 0
    
        
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.music_queue.append(file_path)
            self.current_song_index = len(self.music_queue) - 1
            self.current_file_label.config(text=self.music_queue[self.current_song_index])
    
    def play_music(self):
        if self.music_file_path:
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play()
        elif self.music_queue:
            self.music_file_path = self.music_queue[self.current_song_index]
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play()
            self.current_file_label.config(text=self.music_file_path)
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_file_path = ""
    
    def previous_song(self):
        if len(self.music_queue) > 1:
            self.current_song_index -= 1
            if self.current_song_index < 0:
                self.current_song_index = len(self.music_queue) - 1
            self.music_file_path = self.music_queue[self.current_song_index]
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play()
            self.current_file_label.config(text=self.music_file_path)
           
    def next_song(self):
        if len(self.music_queue) > 1:
            self.current_song_index += 1
            if self.current_song_index >= len(self.music_queue):
                self.current_song_index = 0
            self.music_file_path = self.music_queue[self.current_song_index]
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play()
            self.current_file_label.config(text=self.music_file_path)
    
    def change_volume(self, event):
        pygame.mixer.music.set_volume(self.volume_slider.get())
        

    def view_song_queue(self):
        queue_window = tk.Toplevel(self.master)
        queue_window.title("Music Queue")
        queue_window.geometry("300x300")
        
        queue_label = tk.Label(queue_window, text="Music Queue", font=("Helvetica", 14))
        queue_label.pack(pady=10)
        
        if self.music_queue:
            for i, file_path in enumerate(self.music_queue):
                file_label = tk.Label(queue_window, text=f"{i+1}. {file_path}")
                file_label.pack()
        else:
            no_songs_label = tk.Label(queue_window, text="No songs in queue")
            no_songs_label.pack(pady=50)
                
    def create_view_queue_button(self):
        self.view_queue_button = ttk.Button(self.master, text="View Queue", command=self.view_queue)
        self.view_queue_button.place(x=25, y=200)

    
    
root = tk.Tk()
root.configure(bg="black")
root.resizable(False,False)
music_player = MusicPlayer(root)
root.mainloop()
