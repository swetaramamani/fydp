import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
import math

# Python example - Fourier transform using numpy.fft method

import numpy as np

import matplotlib.pyplot as plotter

 

# How many time points are needed i,e., Sampling Frequency

samplingFrequency   = 100;

 

# At what intervals time points are sampled

samplingInterval       = 1 / samplingFrequency;

 

# Begin time period of the signals

beginTime           = 0;

 

# End time period of the signals

endTime             = 10; 

 

# Frequency of the signals

signal1Frequency     = 2;

# signal2Frequency     = 7;

 

# Time points

time        = np.arange(beginTime, endTime, samplingInterval);

 

# Create two sine waves

amplitude1 = np.sin(2*np.pi*signal1Frequency*time)

# amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

 

# Create subplot

figure, axis = plotter.subplots(2)

plotter.subplots_adjust(hspace=0.5)

 

# Time domain representation for sine wave 1

axis[0].set_title('a) Sine Wave with Frequency of 2Hz')

axis[0].plot(time, amplitude1, 'red')

axis[0].set_xlabel('Time elapsed (s)')

axis[0].set_ylabel('Amplitude')

 

 

# Time domain representation for sine wave 2

# axis[1].set_title('Sine wave with a frequency of 7 Hz')

# axis[1].plot(time, amplitude2)

# axis[1].set_xlabel('Time')

# axis[1].set_ylabel('Amplitude')

 

# Add the sine waves

amplitude = amplitude1

 

# Time domain representation of the resultant sine wave

# axis[2].set_title('Sine wave with multiple frequencies')

# axis[2].plot(time, amplitude)

# axis[2].set_xlabel('Time')

# axis[2].set_ylabel('Amplitude')

 

# Frequency domain representation

fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

 

tpCount     = len(amplitude)

values      = np.arange(int(tpCount/2))

timePeriod  = tpCount/samplingFrequency

frequencies = values/timePeriod

 

# Frequency domain representation

axis[1].set_title('b) FFT of Sine Wave')

 

axis[1].plot(frequencies, abs(fourierTransform))

axis[1].set_xlabel('Frequency (Hz)')

axis[1].set_ylabel('Amplitude')

axis[1].set_xlim(0, 10)

 

plotter.show()
# def get_data(csv_file, accelerometer):
#     df = pd.read_csv(csv_file)
#     df.head()

#     if accelerometer:
#         # Accelerometer units
#         units = '(g)'
#     else:
#         # Gyroscope units
#         units = '(deg/s)'

#     # Collecting data from reading CSV
#     xline = df['x-axis ' + units]
#     yline = df['y-axis ' + units]
#     zline = df['z-axis ' + units]
#     t = df['elapsed (s)']

#     return xline, yline, zline, t

# handa1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.55.34.013_D8E078ADF8A4_Accelerometer.csv'

# xline, yline, zline, t = get_data(handa1, accelerometer=True)

# SAMPLE_RATE = 12.5  # Hertz
# DURATION = t[len(t)-1]  # Seconds
# N = SAMPLE_RATE * DURATION

# print(SAMPLE_RATE, DURATION, N, math.ceil(N), len(t))
# np.array(xline)
# yf = rfft(xline.values)
# xf = rfftfreq(len(t), 1 / SAMPLE_RATE)

# plt.plot(xf, np.abs(yf))
# plt.show()