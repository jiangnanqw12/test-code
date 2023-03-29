from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os

# specify the path of the video and subtitle files
video_path = "3d vector field example - Multivariable calculus - Khan Academy.mp4"
subtitle_path = "3d vector field example - Multivariable calculus - Khan Academy.srt"

# create a video clip object from the video file
video_clip = VideoFileClip(video_path)

# create a text clip object from the subtitle file
subtitle = SubtitlesClip(subtitle_path)

# add the subtitle clip to the video clip
video_with_subtitles = CompositeVideoClip(
    [video_clip, subtitle.set_position(("center", "bottom"))])

# specify the output file name and format
output_path = "output.mp4"

# write the final video file to disk
video_with_subtitles.write_videofile(
    output_path, fps=video_clip.fps, codec='libx264', audio_codec='aac')
