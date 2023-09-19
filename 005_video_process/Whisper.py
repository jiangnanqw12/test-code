import whisper
# whisper audio.flac --model medium --language Japanese
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
