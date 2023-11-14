
# whisper audio.flac --model medium --language Japanese
import subprocess

import subprocess
import os


def get_subtitles(video_directory=None):
    # Define the directory containing video files
    video_directory = video_directory or os.getcwd()

    # Get all video files in the directory
    video_files = [f for f in os.listdir(
        video_directory) if f.endswith('.mp4')]

    # Iterate over each video file
    for video_file in video_files:
        full_path = os.path.join(video_directory, video_file)
        # Construct the Whisper command with the medium model option
        command = ["whisper", full_path, "--model",
                   "medium", "--language", "zh"]
        # Execute the Whisper command using subprocess
        result = subprocess.run(command)
        if result.returncode == 0:
            print("Conversion was successful")
            return True
        else:
            print("Conversion failed")
            print("Error:", result.stderr.decode('utf-8'))
            return False


def main():
    get_subtitles()


if __name__ == "__main__":
    main()
