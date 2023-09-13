

import subprocess
import os
# def download_vid_mul():
#     #, encoding="utf-8"
#     with open("C:\\Users\\shade\OneDrive\\00_source\\testCode\\007_settings\\yt-dlp\\yt.downlist", "r") as f1:
#         lines = f1.readlines()
#     for line in lines:
#         if line.find(".bilibili."):
#             cmd = [
#                 'yt-dlp',

#                 '--config-locations', '~\\OneDrive\\00_source\\testCode\\007_settings\yt-dlp\\yt-dlp_bili.conf',
#                 line.strip()  # Stripping the newline character from the URL
#             ]
#             subprocess.run(cmd)


def download_vid_mul():
    # Define the file path in a more portable way
    file_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', '00_source', 'testCode', '007_settings', 'yt-dlp', 'yt.downlist')

    config_location = os.path.join('~', 'OneDrive', '00_source', 'testCode', '007_settings', 'yt-dlp', 'yt-dlp_bili.conf')

    try:
        with open(file_path, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    for line in lines:


        title, ext = get_video_details(line)
        print(f"Title: {title}")
        print(f"File Extension: {ext}")
        if ".bilibili." in line:
            cmd = [
                'yt-dlp',
                '--config-locations', config_location,
                line.strip()  # Stripping the newline character from the URL
            ]
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Subprocess failed with error: {e}")




def get_video_details(url):
    try:
        playlist_title_result = subprocess.run(['yt-dlp', '--get-title', url], capture_output=True, text=True)
        if playlist_title_result.returncode == 0:
            playlist_title = playlist_title_result.stdout.strip()
        else:
            playlist_title = f"Failed to get playlist title: {playlist_title_result.stderr.strip()}"

        file_extension_result = subprocess.run(['yt-dlp', '--get-filename', url], capture_output=True, text=True)
        if file_extension_result.returncode == 0:
            file_extension = file_extension_result.stdout.strip()
        else:
            file_extension = f"Failed to get file extension: {file_extension_result.stderr.strip()}"

        return playlist_title, file_extension
    except Exception as e:
        return f"An error occurred: {e}"



def main():
    download_vid_mul()
if __name__ == "__main__":
    main()