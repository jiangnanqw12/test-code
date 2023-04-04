import os
from moviepy.editor import *


def merge_video_and_subtitle():
    # get the current directory path
    current_dir = os.getcwd()

    # iterate through all files in the directory
    for file in os.listdir(current_dir):
        # check if the file is a video file
        if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mkv"):
            # check if there is a subtitle file with the same name
            subtitle_file = os.path.splitext(file)[0] + ".srt"
            if os.path.exists(subtitle_file):
                # create a video clip object from the video file
                video_clip = VideoFileClip(file)

                # create a text clip object from the subtitle file
                subtitle_clip = SubtitleClip(
                    subtitle_file, video_clip.duration)

                # add the subtitle clip to the video clip
                video_with_subtitles = CompositeVideoClip(
                    [video_clip, subtitle_clip.set_position(("center", "bottom"))])

                # specify the output file name and format
                output_file = os.path.splitext(file)[0] + "_with_subtitles.mp4"
                output_path = os.path.join(current_dir, output_file)

                # write the final video file to disk
                video_with_subtitles.write_videofile(
                    output_path, fps=video_clip.fps, codec='libx264', audio_codec='aac')
