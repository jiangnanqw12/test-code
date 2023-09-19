import ffmpeg
import os
# ffmpeg -i *.mp4 -vcodec libx264 -crf 23 -preset slower output/*.mp4


import ffmpeg
from pathlib import Path
import subprocess


def convert_video(input_file, output_file, crf=23, preset='slower'):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        output_file
    ]

    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Conversion was successful")
        return True
    else:
        print("Conversion failed")
        print("Error:", result.stderr.decode('utf-8'))
        return False


def mp4_process(path=None):
    # If path is None, get the current directory
    path = Path(path) if path else Path.cwd()

    output_dir = path / "output"
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Use glob to get all .mp4 files
    files_mp4 = list(path.glob("*.mp4"))

    for input_file in files_mp4:
        output_file = output_dir / input_file.name
        convert_video(input_file, output_file)
        # ffmpeg.input(str(input_file)).output(str(output_file), vcodec='libx264', crf=23, preset='slower').run()


def main():
    mp4_process()


if __name__ == "__main__":
    main()
