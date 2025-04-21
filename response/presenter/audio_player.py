from queue import Queue
from threading import Thread
from time import sleep
import sounddevice as sd


class AudioPlayer(Thread):
    PLAYER_SAMPLE_RATE = 24000

    def __init__(self):
        super().__init__()
        self.playlist_queue = Queue()

    def run(self):
      print("Read for reproduction...")
      while True:
          if self.playlist_queue.empty():
              sleep(0.1)
              continue

          audio = self.playlist_queue.get()
          sd.play(audio, samplerate=self.PLAYER_SAMPLE_RATE)
          sd.wait()

    def add_audio(self, audio):
        self.playlist_queue.put(audio)