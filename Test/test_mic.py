# test_mic.py
import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    if status:
        print(status)
    volume = np.linalg.norm(indata) * 10
    print("volume:", volume)

with sd.InputStream(device=3, channels=1, samplerate=16000, callback=callback):
    print("Listening...")
    while True:
        pass
