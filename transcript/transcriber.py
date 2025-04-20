from transcript.voice_recorder import VoiceRecorder
from transcript.voice_to_text import VoiceToText


class Transcriber:
    def __init__(self):
        self.voice_to_text = VoiceToText()
        self.voice_recorder = None
        self.is_transcribing = False

    def listen(self):
        self.is_transcribing = True
        self._start_voice_recorder()

    def stop_listen(self):
        self.is_transcribing = False
        if not self.voice_recorder:
            return

        frames = self.voice_recorder.stop()
        return self.voice_to_text.transcribe(frames)

    def _start_voice_recorder(self):
        self.voice_recorder = VoiceRecorder()
        self.voice_recorder.start()
