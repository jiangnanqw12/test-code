import subprocess

def download_video(url):
    command = ['you-get', url]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print('Download successful')
    else:
        print(f'Download failed with error: {error.decode()}')

download_video("https://www.bilibili.com/video/BV1vt411N7Ti/?spm_id_from=333.999.0.0")