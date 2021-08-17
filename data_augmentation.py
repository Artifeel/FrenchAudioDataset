import numpy as np 
#import tensorflow_io as tfio 
import tensorflow as tf
import matplotlib.pyplot as plt
from IPython import display
import random
import math
import librosa
import soundfile as sf
import re

def aleaGauss(sigma):
    U1 = random.random()
    U2 = random.random()
    return sigma*math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)

file = open('list.txt', "r")
# utilisez readline() pour lire la première ligne
line = file.readline()
while line:
    filename_wav = './original/'+line[:-1]
    #print(filename_wav)
    f = line[:-1]
    p = re.compile('_[\w]*_')
    m = p.search(f)

    # ------------ Adding Noise to the Original audio ------------
    file_contents = tf.io.read_file(filename_wav)
    wav, sample_rate = tf.audio.decode_wav(
          file_contents,
          desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    #print(wav)
    wav_list = np.asarray(wav.numpy())
    # print(wav)
    sigma = 0.02*random.random()
    for k in range(0,len(wav_list)) :
        wav_list[k] = wav_list[k] + aleaGauss(sigma)
    # print(wav)
    wav_list = wav_list.reshape((len(wav_list),1))
    bruited_content = tf.convert_to_tensor(value = wav_list, dtype=tf.float32)
    #print(bruited_content)
    bruited_wav = tf.audio.encode_wav(
          bruited_content,
          sample_rate,
          name=None
        )
    tf.io.write_file(('./bruit/'+f[0:m.end()-1]+'Bruit'+f[m.end()-1:len(f)]),bruited_wav)
    # ------------ Repitching the Original audio ------------
    n_step_down = (-1)*(abs(int(aleaGauss(3.5)))+1)
    #print(n_step_down)
    n_step_up = abs(int(aleaGauss(3.5)))+1
    #print(n_step_up)
    audio, sr = librosa.load(filename_wav)
    audio_down = librosa.effects.pitch_shift(audio,sr, n_steps =n_step_down)
    audio_up = librosa.effects.pitch_shift(audio,sr, n_steps = n_step_up)
    audio_down = tf.convert_to_tensor(audio_down.reshape((len(audio_down),1)),dtype=tf.float32)
    audio_up = tf.convert_to_tensor(audio_up.reshape((len(audio_up),1)),dtype=tf.float32)
    audio_down_wav = tf.audio.encode_wav(
          audio_down,
          sr,
          name=None
        )
    audio_up_wav = tf.audio.encode_wav(
          audio_up,
          sr,
          name=None
        )
    
    tf.io.write_file('./shift_down/'+f[0:m.end()-1]+'Down'+f[m.end()-1:len(f)],audio_down_wav)
    tf.io.write_file('./shift_up/'+f[0:m.end()-1]+'Up'+f[m.end()-1:len(f)],audio_up_wav)
    # ------------ Time Shifting ------------
    n_timesh = abs(int(aleaGauss(2)))+3
    n_timesh_bis = abs(int(aleaGauss(2)))+4
    buffer = 1 * sr
    #print(len(audio))
    padding = np.zeros(int(buffer/n_timesh))
    block_bis = audio[int(buffer/n_timesh_bis) : len(audio)]
    audio = np.concatenate((padding,audio), axis = 0)
    samples_total = len(audio)
    #print(len(audio))
    #check if the buffer is not exceeding total samples 
    if buffer > (samples_total):
      buffer = samples_total

    block = audio[0 : buffer]

    # Write  second segment
    wav_out = tf.convert_to_tensor(block.reshape((len(block),1)),dtype=tf.float32)
    wav_out = tf.audio.encode_wav(
      wav_out,
      sr,
      name=None
    )

    wav_out_bis = tf.convert_to_tensor(block_bis.reshape((len(block_bis),1)),dtype=tf.float32)
    wav_out_bis = tf.audio.encode_wav(
    wav_out_bis,
    sr,
    name=None
    )

    tf.io.write_file('./time_shift/'+f[0:m.end()-1]+'Decal'+f[m.end()-1:len(f)],wav_out)
    tf.io.write_file('./time_shift/'+f[0:m.end()-1]+'Early'+f[m.end()-1:len(f)],wav_out_bis)
    # utilisez readline() pour lire la ligne suivante
    line = file.readline()

file.close()
