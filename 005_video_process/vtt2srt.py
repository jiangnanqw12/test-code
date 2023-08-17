import subprocess
import os

# 输入文件路径、名称、格式
input_file_path = input('输入文件路径：').replace('"', '')
input_file_name = input_file_path.split('\\')[-1]
input_file_format = input_file_name.split('.')[-1]
print('输入字幕文件格式为：' + input_file_format)
# 输出文件格式、路径
output_file_format = input(
    '请输入需转成的文件格式，FFmpeg支持的常见字幕格式：\nvtt\nsrt\nsub/idx\nass/ssa\nsami\nmov\ndvb\nttml\ntxt\nrealtext\n')
output_file_path = input_file_path.replace(
    input_file_format, output_file_format)
# 转换命令
subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path])
