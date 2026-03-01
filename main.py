import yt_dlp
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

def download_mp3(url):
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

    label = tk.Label(root, text="Enter in a valid Youtube URL.", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    url = ttk.Entry(top_frame, width=30)
    url.grid(row=0, column=0, padx=5)

    def folder_button_click():
        folder_path = filedialog.askdirectory(title="Select a folder")
        if folder_path:
            global download_folder
            download_folder = folder_path

    folder_button = tk.Button(top_frame, text="Download Folder", command=folder_button_click)
    folder_button.grid(row=0, column=1)

    def on_button_click():
        download_mp3(url.get())

    button = tk.Button(root, text="Download", command=on_button_click)
    button.pack(pady=10)

    root.mainloop()

start_window()