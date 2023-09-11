import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select Video Files"
        self.select_button["command"] = self.select_files
        self.select_button.pack(side="top")

    def select_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=(("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*")))

        for file_path in file_paths:
            self.convert_to_gif(file_path)

    def convert_to_gif(self, file_path):
        clip = VideoFileClip(file_path)
        gif_path = os.path.splitext(file_path)[0] + '.gif'
        clip.write_gif(gif_path, fps=clip.fps)  # Maintain original video's fps in gif

root = tk.Tk()
app = Application(master=root)
app.mainloop()