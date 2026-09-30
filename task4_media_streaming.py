class Media:
    def __init__(self, title):
        self.title = title
    def play(self):
        print(f"Playing media: {self.title}")
class Audio(Media):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
    def play(self):
        print(f"Playing Audio: {self.title} - {self.duration} minutes")
class Podcast(Audio):
    def __init__(self, title, duration, host):
        super().__init__(title, duration)
        self.host = host
    def play(self):
        print(f"Playing Podcast: {self.title} hosted by {self.host}")
media = Media("Python Basics")
audio = Audio("Relaxing Music", 4)
Podcast = Podcast("AI Today", 30, "John")
media_list = [media, audio, Podcast]
for media in media_list:
    media.play()