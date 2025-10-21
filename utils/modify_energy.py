from pydub import AudioSegment
from pydub.playback import play
import os
import random


FILES = os.listdir("train_audio/1")

counter = 0
for sound in FILES:
    try:
        sound = os.path.join("train_audio/1", sound)
        sound = AudioSegment.from_file(sound, format="wav")

        random_db = random.randint(-10, 10)
        sound = sound + random_db

        # combined = gunfire.overlay(crowd)

        # play(combined)

        sound.export(f"train_audio_3/1/combined_3_{counter}.wav", format="wav")
        counter += 1
        print("Processed file:", counter)

    except Exception as e:
        print("Error processing file:", e)