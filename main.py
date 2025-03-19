import yt_dlp
import sys

def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "extract_audio": True,  
        "audio_format": "mp3",  
        "outtmpl": "/home/gor/Desktop/.PastProjects/python/YT_MusicDownloader/temp/%(title)s.mp3",
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = sys.argv[1]
download_audio(video_url)
