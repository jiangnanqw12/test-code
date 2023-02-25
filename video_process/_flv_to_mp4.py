from moviepy.editor import *
import os
def _flv_to_mp4(input_file, output_file):
    """
    将FLV格式视频转换为MP4格式视频

    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :return: 无返回值
    """
    # 使用moviepy库将FLV格式视频转换为MP4格式视频
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec='libx264')

if __name__ == '__main__':
    for filename in os.listdir():
        if filename.endswith('.flv'):
            _flv_to_mp4(filename, filename[:-4] + '.mp4')
            os.remove(filename)

