import os
import time

def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))

if __name__ == "__main__":
    add_timestamp_to_filenames()
