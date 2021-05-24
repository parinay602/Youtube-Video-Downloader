
# from tkinter import *
# from pytube import YouTube

# root=Tk()
# root.geometry('500x300')
# root.resizable(0,0)
# root.title("Parinay Panwar - youtube downloader")
# Label(root,text = 'Youtube Video Downloader', font='arial 20 bold').pack()
from pytube import Youtube

save_path= "~/Desktop/"
link=input("Please enter the video link: ")
try:
    print("Trying to connect to the server....")
    yt=Youtube(link)
except:
    print("Connection Error")
    
mp4files=yt.filter('mp4')
print(mp4files)
