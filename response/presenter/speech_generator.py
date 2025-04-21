from kokoro import KPipeline


class SpeechGenerator:
    VOICE_TYPE = 'pf_dora'
    LANG_CODE = 'p'

    def __init__(self):
        self.speech_engine = KPipeline(lang_code=self.LANG_CODE)

    def generate_audio_from_text(self, response):
        generator = self.__create_generator(response)

        for i, (gs, ps, audio) in enumerate(generator):
            print("Generating audio...")
            yield audio

    def __create_generator(self, response):
        return self.speech_engine(
            text=response,
            voice=self.VOICE_TYPE,
            speed=1,
            split_pattern=r'\n+'
        )