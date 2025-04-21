
import numpy as np
import sounddevice as sd

def beep(freq=1000, duration=0.2, samplerate=44100):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    sd.play(wave, samplerate)
    sd.wait()

def in_groups_of(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]
