import subprocess
import os
import logging
from concurrent.futures import ThreadPoolExecutor

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurable paths
downlist_dir = os.path.join(os.environ['USERPROFILE'], 'OneDrive', '000_gits', 'testCode', '005_video_process', 'yt-dlp', 'downlist')
CONFIG_DIR = os.path.join(os.environ['USERPROFILE'], 'OneDrive', '000_gits', 'testCode', '005_video_process', 'yt-dlp', 'conf')

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
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info(f"Download successful: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess failed with error: {e.stderr}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def download_video_you_get(playlist, url, index, download_folder):
    output_folder = os.path.join(download_folder, playlist, str(index))
    os.makedirs(output_folder, exist_ok=True)
    command = ["you-get",
               '-o', output_folder,
               url.strip(),
               "--debug",
               "--no-proxy"]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Download successful: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to download video: {e.stderr}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def process_file(file):
    playlist = file.split(".")[0]
    file_path = os.path.join(downlist_dir, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return

    for i, line in enumerate(lines, start=1):
        logging.info(f"Start to download {i}: {line.strip()}")
        if ".bilibili." in line:
            download_video_you_get(playlist, line, i, 'bili')
        elif ".youtube." in line:
            download_video_yt_dlp(playlist, line, 'yt-dlp_YouTube.conf', 'YouTube')

def download_video_mul(playlist="list1"):
    with ThreadPoolExecutor() as executor:
        files = [f for f in os.listdir(downlist_dir) if f.endswith(".downlist")]
        if not files:
            logging.info("No downlist files found.")
            return
        executor.map(process_file, files)

def main():
    download_video_mul()

if __name__ == "__main__":
    main()
