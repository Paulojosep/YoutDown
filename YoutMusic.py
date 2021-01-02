from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import os
import shutil

def get_mp3():
    url = input("Entre com o link do YouTube: ") # O Link do video do YouTube
    output = input("Qual formato voce quer (mav/mp3)?: ")  #Formatação
    print("Convertendo...")

    mp4 = YouTube(url).streams.get_highest_resolution().download('../../../Downloads')
    mp3 = mp4.split(".mp4", 1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()


get_mp3()
