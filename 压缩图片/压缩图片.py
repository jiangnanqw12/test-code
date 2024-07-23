from PIL import Image
import os
def compress_image(input_path, output_path, quality=40):
    image = Image.open(input_path)
    image.save(output_path, 'JPEG', quality=quality)
files=os.listdir()
quality=40
for file in files:
    if file.endswith(".jpg"):
        file_basename=os.path.basename(file)
        compress_image(file, f'{file_basename}_{quality}.jpg')
