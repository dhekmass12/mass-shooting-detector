from pydub import AudioSegment 
from pydub.utils import make_chunks
import os


FILE_NAME = "Crowd Talking.wav"

def divider(file_name):
    myaudio = AudioSegment.from_file(file_name, "wav") 
    chunk_length_ms = 10000 
    chunks = make_chunks(myaudio, chunk_length_ms)
    for i, chunk in enumerate(chunks): 
        chunk_name = 'chunked/' + file_name + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="wav") 

try:
    os.makedirs('chunked') # creating a folder named chunked
except:
    pass

divider(FILE_NAME)