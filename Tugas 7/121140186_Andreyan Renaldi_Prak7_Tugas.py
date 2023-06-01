import tkinter as tk
import pygame
from tkinter import filedialog

class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        
        self.playlist = []
        self.current_index = 0
        
        self.playing = False
        self.select() 
        self.window.mainloop()
    
    def select(self):
        select_button = tk.Button(self.window, text="Select Music", command=self.pilih_musik)
        select_button.pack()
        
        self.current_music_label = tk.Label(self.window, text="Current Music: ")
        self.current_music_label.pack()
        
        play_button = tk.Button(self.window, text="Play", command=self.play)
        play_button.pack()
        
        stop_button = tk.Button(self.window, text="Stop", command=self.stop)
        stop_button.pack()
        
    def pilih_musik(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
    
    def play(self):
        if self.playlist and not self.playing:
            pygame.init()
            pygame.mixer.init()
            
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            
            self.playing = True
            self.update_judul()
    
    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
    
    def update_judul(self):
        current_music = self.playlist[self.current_index]
        self.current_music_label.config(text="Current Music: " + current_music)
    
if __name__ == "__main__":
    MusicPlayer()
