import os
from moviepy.editor import*
image_list = ["flv", "mp4"]
path = os.getcwd()
begin_time = [0, 0, 1]
end_time = [0, 0, 2]
output_file_name = "前期对线狗熊"
# filenamelist[-2][19:28]


def split_video_fix_range(path4video):

    for (dirpath, dirnames, filenames) in os.walk(path4video):
        if filenames != []:
            for filename in filenames:
                filenamelist = filename.split(".")
                if(filenamelist[-1] in image_list):
                    print("in")
                    video = CompositeVideoClip([VideoFileClip(dirpath + "/"+filename
                                                              ).subclip(t_start=(begin_time[0], begin_time[1], begin_time[2]), t_end=(end_time[0], end_time[1], end_time[2]))])
                    for i in range(len(filenamelist[-2])):
                        if filenamelist[-2][i] == "年":
                            if filenamelist[-2][i-4:i] == "2022":
                                video.write_videofile(
                                    output_file_name+filenamelist[-2][i-5:i+5]+".mp4")
                            else:
                                print(filenamelist[-2][i-4:i])


split_video_fix_range(path)
