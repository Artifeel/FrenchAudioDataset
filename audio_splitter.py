import numpy as np 
#import tensorflow_io as tfio 
import tensorflow as tf
import random
import math
import librosa
import soundfile as sf
import sys
import re

filename = sys.argv[1]
audio, sr = librosa.load(filename)
p = re.compile('\/[\w\d-]*\.wav')
m = p.search(filename)
filename = filename[m.start()+1:m.end()]
print(filename)
digits = librosa.effects.split(audio, top_db=18, frame_length=4000)
#digits = [[0,len(audio)]]
print(len(digits))
i=1
pad = 3000
end_prior = 0
try:
    start_next = digits[1][0]
except:
    start_next = len(audio)

for d in digits:

    if (d[0]-pad>=end_prior):
        start=d[0]-pad
    else :
        start=end_prior
    if (d[1]+pad<=start_next):
        end=d[1]+pad
    else :
        end=start_next
    wav_out = audio[start:end]
    wav_out = tf.convert_to_tensor(wav_out.reshape((len(wav_out),1)),dtype=tf.float32)
    wav_out = tf.audio.encode_wav(
          wav_out,
          sr,
          name=None
        )
    print(start,end)
    
    end_prior=d[1]
    if (i+1 < len(digits)):
        start_next=digits[i+1][0]
    else :
        start_next=len(audio)
    tf.io.write_file(f'./test_split/{filename[:-4]}_{i-1}.wav',wav_out)
    i=i+1