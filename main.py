import yt_dlp
import sys

print(__file__)

def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "extract_audio": True,  
        "audio_format": "mp3",  
        "outtmpl": f"{path}/temp/%(title)s.mp3",
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = sys.argv[1]
path = sys.argv[2]
download_audio(video_url)
