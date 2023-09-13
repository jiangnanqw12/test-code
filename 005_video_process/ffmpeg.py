import ffmpeg
import os
#ffmpeg -i *.mp4 -vcodec libx264 -crf 23 -preset slower output/*.mp4

def mp4_process(path=None):
    if path is None:
        path=os.getcwd()

    files_mp4 = [f for f in os.listdir(path) if os.path.isfile(
                os.path.join(path, f)) and (f.endswith(".mp4"))]
    for file in files_mp4:
        input_file = os.path.join(path,file)
        output_file = os.path.join(path,"output",file)
        ffmpeg.input(input_file).output(output_file, vcodec='libx264', crf=23, preset='slower').run()

def main():
    mp4_process()

if __name__ == "__main__":
    main()