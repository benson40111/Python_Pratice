# -*- coding: utf-8 -*-
import numpy as np
import sys
import wave
import matplotlib.pyplot as plt

x2 = np.arange(0, 360)
y2 = np.sin(x2 * np.pi / 180)
#a = int(input("a = ? \n"))
#b = int(input("b = ? \n"))
"""for x in range(0, 100):
    y = a * x + b
    plt.plot(x, y, "ro")
    plt.subplot(211)"""
x1 = x2
y1 = np.cos(x1 * np.pi / 180)
plt.subplot(212)
plt.plot(x2, y2, lw = 5)
plt.subplot(211)
plt.plot(x1, y1, lw = 3)

plt.show()

"""f = wave.open(r"test1.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

plt.subplot(211) 
plt.plot(time, wave_data[0])
plt.subplot(212) 
plt.plot(time, wave_data[1], c="g")
plt.show()"""
