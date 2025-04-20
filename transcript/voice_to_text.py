import whisper


class VoiceToText:
    MODEL = 'base'
    DEFAULT_LANGUAGE = 'pt'

    def __init__(self):
        self.model = whisper.load_model(self.MODEL)

    def transcribe(self, audio_frames):
        return self.model.transcribe(audio_frames, language=self.DEFAULT_LANGUAGE)
