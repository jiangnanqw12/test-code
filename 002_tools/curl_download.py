import subprocess
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# List of allowed extensions
ALLOWED_EXTENSIONS = ['.c', '.h', '.csv', '.py', '.db', '.zip', '.html', '.png',
                      '.jpg', '.pdf', '.vtt', '.srt', '-360p.mp4']


def download_file(url, local_path, base_path=None):
    download_file_curl(url, local_path, base_path)
    # download_file_requests(url, local_path, base_path)


def download_file_curl(url, local_path, base_path=None):
    try:
        decoded_url = urllib.parse.unquote(url)  # First, decode the URL
        encoded_url = urllib.parse.quote(
            decoded_url, safe=':/')  # Then, encode it properly
        # if extension_filter(url):
        subprocess.run(['curl', '-o', local_path, '-L', '-v',
                        '-k', '-A', 'Mozilla/5.0', encoded_url], check=True)
    except subprocess.CalledProcessError as e:
        if base_path == None:
            base_path = os.getcwd()
        file_log = os.path.join(base_path, 'log.txt')
        if os.path.exists(file_log):
            with open(file_log, 'r', encoding="utf-8") as f:
                content = f.read()
        else:
            content = ''
        with open(file_log, 'w', encoding="utf-8") as f:
            f.write(content + f"Error downloading {url}: {e}\n")
        print(f"Error downloading {url}: {e}")


def download_file_requests(url, local_path, base_path=None):
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
    except subprocess.CalledProcessError as e:
        if base_path == None:
            base_path = os.getcwd()
        file_log = os.path.join(base_path, 'log.txt')
        if os.path.exists(file_log):
            with open(file_log, 'r', encoding="utf-8") as f:
                content = f.read()
        else:
            content = ''
        with open(file_log, 'w', encoding="utf-8") as f:
            f.write(content + f"Error downloading {url}: {e}\n")
        print(f"Error downloading {url}: {e}")


def is_valid_link(href):
    # Check if the link is valid

    return href and not href.startswith('?') and not href.startswith('/') and not href.startswith('../')


def extension_filter(url):
    return url and any(url.endswith(ext) for ext in ALLOWED_EXTENSIONS)


def download_from_url(base_url, target_directory, visited_urls=set()):
    if base_url in visited_urls:
        return
    visited_urls.add(base_url)

    response = requests.get(base_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if is_valid_link(href):
            href = urllib.parse.unquote(href)
            download_url = urllib.parse.urljoin(base_url, href)
            if href.endswith('/'):
                # If the link is a directory, recursively call this function
                download_from_url(download_url, os.path.join(
                    target_directory, href), visited_urls)
            else:
                local_file_path = os.path.join(target_directory, href)
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                download_from_url(download_url, local_file_path)


def main():
    base_url = r'https://cdn.cs50.net/2022/fall/'  # Replace with your URL
    # Replace with your desired local directory
    target_directory = os.getcwd()

    download_from_url(base_url, target_directory)


if __name__ == "__main__":
    main()
