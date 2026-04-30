import openwakeword
from playsound import playsound
import config

#init with the config
model = openwakeword.Model(wakeword_models=[config.MODEL_PATH])
print("Listening for LIKE...")
