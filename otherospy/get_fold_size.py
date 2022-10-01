import os


def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            print(f)
    return 1.0*size/1024


print(getFileSize("."))
