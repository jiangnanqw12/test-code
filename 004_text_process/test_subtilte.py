import os
path = os.getcwd()

for root, dirs, files in os.walk(path):
    for file in files:
        filenamelist = file.split(sep=".")
        if filenamelist[-1] == "srt":
            if filenamelist[-2] == "en":
                os.rename(os.path.join(root, file), os.path.join(
                    root, filenamelist[0] + ".srt"))
            elif filenamelist[-2] == "zh":
                pass
            elif filenamelist[-2] in ["es-419", "ta", "my", "te", "ka", "cs", "no", "ar", "hi", "pt-BR", "th", "az", "bg", "ko", "es", "et", "fr", "de", "it", "ja", "nl", "pl", "pt", "ru", "sv", "tr", "uk", "vi"]:
                os.remove(os.path.join(root, file))
