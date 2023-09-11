import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '~/YouTube/%(playlist)s/%(title)s.%(ext)s',  # Replace with your actual directory path

        'writesubtitles': True,  # This option enables the writing of subtitles
        'allsubtitles': True,    # This option enables downloading of all available subtitles
        # 'subtitleslangs': ['en'],  # Uncomment this line to specify the languages of the subtitles you want to download
        #'skipdownload': True,
        'verbose': True,  # Enables verbose logging
        'cookies': '~/OneDrive/00_source/testCode/007_settings/yt-dlp/www.youtube.com_cookies.txt',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
#python ~\OneDrive\00_source\testCode\007_settings\yt-dlp\yt-dlp.py
# Use the function to download a video by providing a video URL as a parameter
download_video('https://www.youtube.com/watch?v=__0nZuG4sTw&list=PLn8PRpmsu08pSpYcLLkfXcYlcs5judk0d&ab_channel=MATLAB')
