import subprocess


def split_video(video_path, start_time, duration, output_file):
    """
    Split video using ffmpeg with re-encoding.

    :param video_path: Path to the input video file.
    :param start_time: Start time in 'hh:mm:ss' format.
    :param duration: Duration of the segment in 'hh:mm:ss' format.
    :param output_file: Name of the output file.
    """

    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-ss', start_time,
        '-t', duration,
        '-c:v', 'libx264',  # Force video re-encoding using libx264
        '-c:a', 'aac',      # Force audio re-encoding using aac
        '-strict', 'experimental',
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Segment saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error splitting video: {e}")


if __name__ == '__main__':
    video_path = "002_How Ultrasonic Energy Impacts Tissue.mp4"
    start_time = "00:02:12"
    duration = "00:00:9"
    output_file = "Vessel sealing process.mp4"

    split_video(video_path, start_time, duration, output_file)
