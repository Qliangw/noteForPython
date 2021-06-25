"""
sine.py

Generates a sine wave and saves it n WAVE file format.

Author: Mahesh Venkitachalam
"""

import numpy as np
import math
import wave

s_rate = 44100
n_samples = s_rate * 5
x = np.arange(n_samples) / float(s_rate)
vals = np.sin(2.0*math.pi*146.83*x)
# data = np.array(vals * 32767, 'int16').tostring() # tostring该方法已弃用
data = np.array(vals * 32767, 'int16').tobytes()
file = wave.open('sine146_83.wav', 'wb')
file.setparams((1, 2, s_rate, n_samples, 'NONE', 'uncompressed'))
file.writeframes(data)
file.close()
