from pytube import YouTube
from tkinter import *

def ydownload():
    display.insert(0, "Please wait, the video is being downloaded...")
    link = (urlbox.get())
    ytvdo = YouTube(link)
    ytvdo = ytvdo.streams.get_highest_resolution()
    ytvdo.download(output_path='videos/')
    print("Video has been downloaded.")
    display.insert(1, "The video has been Downloaded successfully.")
    display.insert(2, "path: desktop/Python_Projects/YoutubeDownloader/videos")

root = Tk()
root.geometry("455x335")
root.minsize(455, 335)
root.maxsize(455, 335)

root.title("YT Downloader by Ambar")

lbl = Label(root, text="Youtube Downloader").place(x=5, y=3)

lbl2 = Label(root, text="Display for Messages").place(x=15, y=35)
display = Listbox(root, height=5, width=70)
display.place(x=15, y=55)

url1 = StringVar
lbl1 = Label(root, text="Video URL").place(x=5, y=180)
urlbox = Entry(root, background="white", border=2, relief=SUNKEN, width=30, textvariable=url1, font="Ariel 13 normal")
urlbox.place(x=85, y=180)
downloadbtn = Button(root, text="Download", command=ydownload).place(x=360, y=180)

root.mainloop()