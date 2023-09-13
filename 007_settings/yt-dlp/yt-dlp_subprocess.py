

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


def download_vid_mul(playlist="list1"):
    # Define the file path in a more portable way
    file_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', '00_source', 'testCode', '007_settings', 'yt-dlp', 'yt.downlist')

    config_location = os.path.join('~', 'OneDrive', '00_source', 'testCode', '007_settings', 'yt-dlp', 'yt-dlp_bili.conf')

    try:
        with open(file_path, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    for i, line in enumerate(lines, start=1):
        line =line.strip()
        playlist=get_playlist_details(line)
        filename_result = subprocess.run(['yt-dlp', '--get-filename', line], capture_output=True, text=True)
        if filename_result.returncode == 0:
            filename = filename_result.stdout.strip()
        else:
            filename = f"Failed to get file extension: {filename_result.stderr.strip()}"
        filename = f"{str(i).zfill(3)}_{filename}"
        if ".bilibili." in line:
            cmd = [
                'yt-dlp',
                '--config-locations', config_location,
                # Save all videos under YouTube directory in your home directory
                '-o',os.path.expanduser(f'~/bili/{playlist}/{filename}'),
                line.strip()  # Stripping the newline character from the URL
            ]
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Subprocess failed with error: {e}")


def get_playlist_details(url):
    try:
        # Get the playlist details
        result = subprocess.run(['yt-dlp', '--flat-playlist', url], capture_output=True, text=True)

        if result.returncode == 0:
            playlist_details = result.stdout.strip()
            print("Playlist details fetched successfully.")
            return playlist_details
        else:
            error_message = f"Failed to get playlist details: {result.stderr.strip()}"
            print(error_message)
            return error_message

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        return error_message

def get_video_details(url):
    try:
        playlist_title_result = subprocess.run(['yt-dlp', '--get-title', url], capture_output=True, text=True)
        if playlist_title_result.returncode == 0:
            playlist_title = playlist_title_result.stdout.strip()
        else:
            playlist_title = f"Failed to get playlist title: {playlist_title_result.stderr.strip()}"

        filename_result = subprocess.run(['yt-dlp', '--get-filename', url], capture_output=True, text=True)
        if filename_result.returncode == 0:
            filename = filename_result.stdout.strip()
        else:
            filename = f"Failed to get file extension: {filename_result.stderr.strip()}"

        return playlist_title, filename
    except Exception as e:
        return f"An error occurred: {e}"



def main():
    download_vid_mul()
if __name__ == "__main__":
    main()