# file-name: pdf_download.py
__author__ = 'rxread'
import requests
from bs4 import BeautifulSoup
import os


def download_file(url, index, folder):
    download_dir = '.\\' + folder + '\\' + \
        '{:02}'.format(index) + url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(download_dir, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return download_dir


def from_page(folder):
    root_link = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-notes/'
    r = requests.get(root_link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html5lib")
        index = 1
        print("\n=============== {0:10} ===============\n".format(
            'Start Downloading'))
        for link in soup.find_all('a'):
            new_link = 'https://ocw.mit.edu' + link.get('href')
            if new_link.endswith('.pdf'):
                download_dir = download_file(new_link, index, folder)
                print("Dowloading: {0:30} ==>  {0:30}".format(
                    new_link.split('/')[-1], download_dir))
                index += 1
        print("\n=============== {0:10} ===============\n".format(
            'Download Finished'))
        print('Totally %d files have been downloaded.')
    else:
        print("ERRORS occur !!!")
