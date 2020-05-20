class AudioFile:
    def __init__(self, filename: str):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File format")
        self.filename = filename


class MP3(AudioFile):
    ext = ".mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = ".wav"

    def play(self):
        print("playing {} as mp3".format(self.filename))


m = MP3("hello.mp3")
m.play()

w = WavFile("hello.wav")
w.play()

x = WavFile("hjdbjvhdf")

