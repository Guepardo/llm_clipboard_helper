from threading import Thread
import pyaudio
import webrtcvad
import numpy as np


class VoiceRecorder(Thread):
    CHUNK_DURATION_MS = 30  # cada frame analisado tem 30ms
    RATE = 16000
    CHANNELS = 1
    FORMAT = pyaudio.paInt16
    CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)  # 480 samples para 30ms
    # 0 (menos sensível) a 3 (mais sensível)
    HUMAN_VOICE_DETECTOR_SENSIBILITY = 0

    def __init__(self):
        super().__init__()
        self.recorder = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
        self.human_voice_detector = webrtcvad.Vad(
            self.HUMAN_VOICE_DETECTOR_SENSIBILITY)
        self._recording = True

    def run(self):
        print(self.CHUNK_SIZE)
        self.stream = self.recorder.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK_SIZE
        )

        while (self._recording):
            frame = self.stream.read(
                self.CHUNK_SIZE, exception_on_overflow=False)

            if self.human_voice_detector.is_speech(frame, self.RATE):
                self.frames.append(frame)

    def stop(self):
        self._recording = False
        self._try_close_recorder()
        self._try_close_stream()
        return self._audio_bytes_regularize()

    def _try_close_recorder(self):
        try:
            if self.recorder:
                self.recorder.terminate()
        except Exception as e:
            # print(f"Erro: {e}")
            pass

    def _try_close_stream(self):
        try:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
        except Exception as e:
            # print(f"Erro: {e}")
            pass

    def _audio_bytes_regularize(self):
        audio_bytes = b''.join(self.frames)
        # Regularize audio for whisper
        return np.frombuffer(audio_bytes, np.int16).astype(np.float32) / 32768.0
