from moviepy.editor import *
import os

# specify the path of the video and subtitle files
video_path = "path/to/video.mp4"
subtitle_path = "path/to/subtitle.srt"

# create a video clip object from the video file
video_clip = VideoFileClip(video_path)

# create a text clip object from the subtitle file
subtitle_clip = SubtitleClip(subtitle_path, video_clip.duration)

# add the subtitle clip to the video clip
video_with_subtitles = CompositeVideoClip(
    [video_clip, subtitle_clip.set_position(("center", "bottom"))])

# specify the output file name and format
output_path = "path/to/output.mp4"

# write the final video file to disk
video_with_subtitles.write_videofile(
    output_path, fps=video_clip.fps, codec='libx264', audio_codec='aac')
