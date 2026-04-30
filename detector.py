import openwakeword
import pyaudio
import numpy as np
from playsound import playsound
import config

#init model and mic
model = openwakeword.Model(wakeword_models=[config.MODEL_PATH])
mic_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1280)

print("listening for filler words...")

while True:
    # read audio and get prediction score
    data = np.frombuffer(mic_stream.read(1280, exception_on_overflow=False), dtype=np.int16)
    prediction = model.predict(data)
    
    # trigger the sound if the score is above the threshold
    if list(prediction.values())[0] > config.THRESHOLD:
        print("like detected...")
        playsound(config.AUDIO_PATH)
        model.reset()  # clears mem to not loop
