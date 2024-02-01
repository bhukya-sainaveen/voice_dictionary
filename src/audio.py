# audio.py
from pygame import mixer

def play_audio(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.stop()
