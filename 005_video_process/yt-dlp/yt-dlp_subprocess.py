

import subprocess
import os

# Configurable paths
downlist_dir = os.path.join(os.environ['USERPROFILE'], 'OneDrive',
                            '000_gits', 'testCode', '005_video_process', 'yt-dlp', 'downlist')
CONFIG_DIR = os.path.join(os.environ['USERPROFILE'], 'OneDrive',
                          '000_gits', 'testCode', '005_video_process', 'yt-dlp', 'conf')


def download_video_yt_dlp(playlist, line, config_file, download_folder):
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


def download_video_you_get(playlist, url, index, download_folder):
    output_folder = os.path.join(download_folder, playlist, str(index))
    os.makedirs(output_folder, exist_ok=True)
    command = ["you-get",
               '-o', output_folder,
               url.strip(),
               "--debug",
               "--no-proxy"]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to download video: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


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
            download_video_you_get(playlist, line, i, 'bili')
            # download_video_yt_dlp(
            #     playlist, line, 'yt-dlp_bili.conf', 'bili')
        elif ".youtube." in line:
            download_video_yt_dlp(
                playlist, line, 'yt-dlp_YouTube.conf', 'YouTube')


def main():
    download_video_mul()


if __name__ == "__main__":
    main()
