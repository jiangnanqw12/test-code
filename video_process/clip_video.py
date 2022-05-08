import os
from moviepy.editor import*
image_list = ["flv", "mp4"]
path = os.getcwd()
begin_time = [0, 0, 1.0]
end_time = [0, 0, 3.0]
output_file_name = "前期对线狗熊.mp4"


def split_video_fix_range(path4video):

    for (dirpath, dirnames, filenames) in os.walk(path4video):
        if filenames != []:
            for filename in filenames:
                filenamelist = filename.split(".")
                if(filenamelist[-1] in image_list):
                    print("in")
                    video = CompositeVideoClip([VideoFileClip(dirpath + "/"+filename
                                                              ).subclip(t_start=(begin_time[0], begin_time[1], begin_time[2]), t_end=(end_time[0], end_time[1], end_time[2]))])
                    video.write_videofile(output_file_name)


split_video_fix_range(path)
