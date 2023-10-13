

import subprocess
import os

# Configurable paths
downlist_dir = os.path.join(os.environ['USERPROFILE'], 'OneDrive',
                            '00_source', 'testCode', '005_video_process', 'yt-dlp', 'list')
CONFIG_DIR = os.path.join(os.environ['USERPROFILE'], 'OneDrive',
                          '00_source', 'testCode', '005_video_process', 'yt-dlp', 'conf')


def download_video(playlist, line, config_file, download_folder):
    config_location = os.path.join(CONFIG_DIR, config_file)
    cmd = [
        'yt-dlp',
        '--config-location', config_location,
        '-o', os.path.expanduser(
            f'~/{download_folder}/{playlist}/%(autonumber)s_%(title)s-[%(id)s]-.%(ext)s'),
        line.strip()
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with error: {e}")


def download_video_mul(playlist="list1"):
    for file in os.listdir(downlist_dir):
        if file.endswith(".downlist"):
            print(f"Downloading from {file}")
            playlist = file.split(".")[0]

            file_path = os.path.join(downlist_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f1:
                    lines = f1.readlines()
            except FileNotFoundError:
                print(f"File not found: {file_path}")
                return
    for i, line in enumerate(lines, start=1):
        print(f"Start to download {i}: {line.strip()}")
        if ".bilibili." in line:
            download_video(playlist, line, 'yt-dlp_bili.conf', 'bili')
        elif ".youtube." in line:
            download_video(playlist, line, 'yt-dlp_YouTube.conf', 'YouTube')


def download_vid_mul(playlist="list1"):
    # Define the file path in a more portable way
    downlist_dir = os.path.join(os.environ['USERPROFILE'], 'OneDrive',
                                '00_source', 'testCode', '005_video_process', 'yt-dlp', 'list')
    for file in os.listdir(downlist_dir):
        if file.endswith(".downlist"):
            print(f"Downloading from {file}")
            playlist = file.split(".")[0]

            file_path = os.path.join(downlist_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f1:
                    lines = f1.readlines()
            except FileNotFoundError:
                print(f"File not found: {file_path}")
                return

            for i, line in enumerate(lines, start=1):
                line = line.strip()
                print(f"start to download {i}: {line}")

                if ".bilibili." in line:
                    config_location_bili = os.path.join(
                        '~', 'OneDrive', '00_source', 'testCode', '005_video_process', 'yt-dlp', 'conf', 'yt-dlp_bili.conf')
                    cmd = [
                        'yt-dlp',
                        '--config-locations', config_location_bili,
                        # Save all videos under YouTube directory in your home directory
                        '-o', os.path.expanduser(
                            f'~/bili/{playlist}/%(autonumber)s_%(title)s-[%(id)s]-.%(ext)s'),
                        line.strip()  # Stripping the newline character from the URL
                    ]
                    try:
                        subprocess.run(
                            cmd, check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Subprocess failed with error: {e}")
                elif ".youtube." in line:
                    config_location_YouTube = os.path.join(
                        '~', 'OneDrive', '00_source', 'testCode', '005_video_process', 'yt-dlp', 'conf', 'yt-dlp_YouTube.conf')
                    cmd = [
                        'yt-dlp',
                        '--config-locations', config_location_YouTube,
                        # Save all videos under YouTube directory in your home directory
                        '-o', os.path.expanduser(
                            f'~/YouTube//{playlist}/%(autonumber)s_%(title)s-[%(id)s]-.%(ext)s'),
                        line.strip()  # Stripping the newline character from the URL
                    ]
                    try:
                        subprocess.run(
                            cmd, check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Subprocess failed with error: {e}")


def get_playlist_details(url):
    try:
        # Get the playlist details
        result = subprocess.run(
            ['yt-dlp', '--flat-playlist', url], capture_output=True, text=True)

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
        playlist_title_result = subprocess.run(
            ['yt-dlp', '--get-title', url], capture_output=True, text=True)
        if playlist_title_result.returncode == 0:
            playlist_title = playlist_title_result.stdout.strip()
        else:
            playlist_title = f"Failed to get playlist title: {playlist_title_result.stderr.strip()}"

        filename_result = subprocess.run(
            ['yt-dlp', '--get-filename', url], capture_output=True, text=True)
        if filename_result.returncode == 0:
            filename = filename_result.stdout.strip()
        else:
            filename = f"Failed to get file extension: {filename_result.stderr.strip()}"

        return playlist_title, filename
    except Exception as e:
        return f"An error occurred: {e}"


def main():
    download_video_mul()


if __name__ == "__main__":
    main()
