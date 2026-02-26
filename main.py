import yt_dlp
import tkinter as tk
from tkinter import ttk
import os

def download_mp3(url):
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def start_window():
    root = tk.Tk()
    root.title("Youtube to MP3")
    root.geometry("500x300")

    url = ttk.Entry(root, width=30)
    url.pack(pady=10)

    label = tk.Label(root, text="Enter in a valid Youtube URL.")
    label.pack(pady=20)
    
    def on_button_click():
        #label.config(text=url.get())
        download_mp3(url.get())

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=10)

    root.mainloop()

start_window()