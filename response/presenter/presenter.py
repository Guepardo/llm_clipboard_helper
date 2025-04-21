import subprocess
from queue import Queue
from threading import Thread

from response.presenter.audio_player import AudioPlayer
from response.presenter.formatter import Formatter
from response.presenter.speech_generator import SpeechGenerator

class Presenter(Thread):

    def __init__(self):
        super().__init__()
        self.playlist_queue = Queue()
        self.formatter = Formatter()
        self.audio_reader = AudioPlayer()
        self.speech_generator = SpeechGenerator()

        self.audio_reader.start()

    def present(self, response):
        print(response)
        self.__display_present(response)
        self.__narrate(response)

    def __display_present(self, response):
        subprocess.run(['notify-send', 'Resposta', response, '-t', '10000'])

    def __narrate(self, response):
        response = self.formatter.format(response)
        audios = self.speech_generator.generate_audio_from_text(
            response)

        for audio in audios:
            self.audio_reader.add_audio(audio)
