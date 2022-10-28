import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api
import numpy as np

# load the data
fs, data = wavfile.read(
    '/media/sonoda/1AAA3130AA3109B1/Users/ks687/Music/flac/The_Beatles-1/01.Love_Me_Do.wav')
print(fs, data.shape)
a = data.T[0]  # this is a two channel soundtrack, I get the first track

# this is 8-bit track, b is now normalized on [-1,1)
b = [(ele/2**8.)*2-1 for ele in a]

# calculate fourier transform (complex numbers list)
c = fft(b)
print(c)

# you only need half of the fft list (real signal symmetry)
d = len(c) / 2

TH = fs / 2.0

d = int(d * TH / (fs / 2.0))

fq = np.linspace(0, TH, d - 1)

plt.plot(fq, abs(c[:(d-1)]))
plt.yscale("log")
plt.xscale("log")
plt.grid(which="both")
plt.show()
