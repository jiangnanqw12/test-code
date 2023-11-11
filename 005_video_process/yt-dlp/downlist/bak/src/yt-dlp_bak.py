import yt_dlp
import os




def download_video1(url):
    ydl_opts=config()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #ydl.list_formats(url.strip())
        ydl.download([url.strip()])
#python ~\OneDrive\00_source\testCode\007_settings\yt-dlp\yt-dlp.py
# Use the function to download a video by providing a video URL as a parameter

def config1():
    ydl_opts = {
        'format': 'flv',
        'outtmpl': '~/YouTube/%(playlist)s/%(title)s.%(ext)s',  # Replace with your actual directory path

        #'writesubtitles': True,  # This option enables the writing of subtitles
        #'allsubtitles': True,    # This option enables downloading of all available subtitles
        # 'subtitleslangs': ['en'],  # Uncomment this line to specify the languages of the subtitles you want to download
        #'skipdownload': True,
        'verbose': True,  # Enables verbose logging
        #'cookies': '~/OneDrive/00_source/testCode/007_settings/yt-dlp/www.youtube.com_cookies.txt',
    }
    return ydl_opts
def download_vid_mul1():
    #, encoding="utf-8"
    with open("C:\\Users\\shade\OneDrive\\00_source\\testCode\\007_settings\\yt-dlp\\yt.downlist", "r") as f1:
        lines = f1.readlines()
    for line in lines:
        download_video(line)
def main():
    download_vid_mul()
if __name__ == "__main__":
    main()