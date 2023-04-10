from moviepy.editor import *
import os
import argparse


def convert_vid(input_file, output_file):
    """
    将FLV格式视频转换为MP4格式视频

    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :return: 无返回值
    """
    # 使用moviepy库将FLV格式视频转换为MP4格式视频
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec='libx264')


def video_convertor(input_extension, output_extension):
    """
    将指定格式的视频转换为指定格式的视频

    :param input_extension: 输入文件格式
    :param output_extension: 输出文件格式
    :return: 无返回值
    """
    for filename in os.listdir():
        if filename.endswith(input_extension):
            n = len(input_extension)
            convert_vid(filename, filename[:-n] + output_extension)


def _flv_2_mp4():
    for filename in os.listdir():
        if filename.endswith('.flv'):
            convert_vid(filename, filename[:-4] + '.mp4')
            # os.remove(filename)


def _webm_2_mp4():
    for filename in os.listdir():
        if filename.endswith('.webm'):
            convert_vid(filename, filename[:-4] + '.mp4')


def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-f2m', '--flv2mp4',
                        action='store_true', help='call flv2mp4')
    parser.add_argument('-w2m', '--webm2mp4',
                        action='store_true', help='call webm2mp4')
    parser.add_argument('-i', '--input_extension', type=str, default=r'flv',
                        help='input extension')
    parser.add_argument('-o', '--output_extension', type=str, default=r'mp4',
                        help='output extension')
    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.flv2mp4:
        _flv_2_mp4()
    elif args.webm2mp4:
        _webm_2_mp4()
    elif args.input_extension and args.output_extension:
        video_convertor(args.input_extension, args.output_extension)

    else:
        print("Invalid argument")


if __name__ == '__main__':
    main()
