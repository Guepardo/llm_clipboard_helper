
import numpy as np
import sounddevice as sd

def beep(freq=1000, duration=0.2, samplerate=44100):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    sd.play(wave, samplerate)
    sd.wait()
