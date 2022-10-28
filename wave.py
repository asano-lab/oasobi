import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api
fs, data = wavfile.read(
    '/media/sonoda/1AAA3130AA3109B1/Users/ks687/Music/flac/The_Beatles-1/01.Love_Me_Do.wav')  # load the data
print(fs, data.shape)
a = data.T[0]  # this is a two channel soundtrack, I get the first track

# this is 8-bit track, b is now normalized on [-1,1)
b = [(ele/2**8.)*2-1 for ele in a]

c = fft(b)  # calculate fourier transform (complex numbers list)
print(c)

d = len(c)//2  # you only need half of the fft list (real signal symmetry)

plt.plot(abs(c[:(d-1)]), 'r')
plt.yscale("log")
plt.show()
