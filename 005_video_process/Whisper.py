import whisper
#whisper audio.flac --model medium --language Japanese
model = whisper.load_model("medium")
result = model.transcribe("audio.mp3")
with open("test", "w", encoding="utf-8") as f1:
    f1.write(result)