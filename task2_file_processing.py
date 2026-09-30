class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
    def process(self):
        print("Processing file")
class TextFile(FileProcessor):
    def process(self):
        print(f"Processing text file: {self.filename}")
class ImageFile(FileProcessor):
    def process(self):
        print(f"Processing image file: {self.filename}")
class AudioFile(FileProcessor):
    def process(self):
        print(f"Processing audio file: {self.filename}")
text = TextFile("notes.txt")
image = ImageFile("photo.jpg")
audio = AudioFile("song.mp3")

files = [text, image, audio]
for file in files:
    file.process()