import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks

ACC_SAMPLE_RATE = 100 #Hertz
GYR_SAMPLE_RATE = 100 #Hz

def get_data(csv_file, accelerometer):
    df = pd.read_csv(csv_file)
    df.head()

    if accelerometer:
        # Accelerometer units
        units = '(g)'
    else:
        # Gyroscope units
        units = '(deg/s)'

    # Collecting data from reading CSV
    xline = df['x-axis ' + units]
    yline = df['y-axis ' + units]
    zline = df['z-axis ' + units]
    t = df['elapsed (s)']

    return xline, yline, zline, t

def get_fft(xline_s, yline_s, zline_s, xline_n, yline_n, zline_n):
    
    np.array(xline_s)
    x_fft_s = rfft(xline_s.values)
    x_fft_s = np.abs(x_fft_s)

    np.array(yline_s)
    y_fft_s = rfft(yline_s.values)
    y_fft_s = np.abs(y_fft_s)

    np.array(zline_s)
    z_fft_s = rfft(zline_s.values)
    z_fft_s = np.abs(z_fft_s)

    np.array(xline_n)
    x_fft_n = rfft(xline_n.values)
    x_fft_n = np.abs(x_fft_n)

    np.array(yline_n)
    y_fft_n = rfft(yline_n.values)
    y_fft_n = np.abs(y_fft_n)

    np.array(zline_n)
    z_fft_n = rfft(zline_n.values)
    z_fft_n = np.abs(z_fft_n)
    

    return x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n


def get_snr(x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n):

    if len(x_fft_s) > len(x_fft_n):
        print("signal", len(x_fft_s), len(x_fft_n))
        x_fft_s = x_fft_s[0:len(x_fft_n)]
        y_fft_s = y_fft_s[0:len(y_fft_n)]
        z_fft_s = z_fft_s[0:len(z_fft_n)]

    if len(x_fft_n) > len(x_fft_s):
        print("noise", len(x_fft_s), len(x_fft_n))
        x_fft_n = x_fft_n[0:len(x_fft_s)]
        y_fft_n = y_fft_n[0:len(y_fft_s)]
        z_fft_n = z_fft_n[0:len(z_fft_s)]
   
    x_snr = 10*np.log(x_fft_s/x_fft_n)
    y_snr = 10*np.log(y_fft_s/y_fft_n)
    z_snr = 10*np.log(z_fft_s/z_fft_n)

    return x_snr, y_snr, z_snr

def plot_2d_graph(csv_file_s, csv_file_n, accelerometer):

    xline_s, yline_s, zline_s, t_s = get_data(csv_file_s, accelerometer)
    xline_n, yline_n, zline_n, t_n = get_data(csv_file_n, accelerometer)
    x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n = get_fft(xline_s, yline_s, zline_s, xline_n, yline_n, zline_n)

    if accelerometer:
        frequencies = rfftfreq(len(t_s), 1 / ACC_SAMPLE_RATE)
    else:
        frequencies = rfftfreq(len(t_s), 1 / GYR_SAMPLE_RATE)
    # x_snr, y_snr, z_snr = get_snr(x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n)

    # if len(t_n) > len(t_s):
    #     t_n = t_s

    fig, axs = plt.subplots(3)
    if accelerometer:
        fig.suptitle('Accelerometer FFT SNR Testing (Hand): Subject 1, Trial 1')
        axs[0].set_ylabel('X Amplitude (g)')
        axs[1].set_ylabel('Y Amplitude (g)')
        axs[2].set_ylabel('Z Amplitude (g)')
    else:
        fig.suptitle('Gyroscope FFT SNR Testing (Hand): Subject 1, Trial 1')
        axs[0].set_ylabel('X Amplitude (deg/s)')
        axs[1].set_ylabel('Y Amplitude (deg/s)')
        axs[2].set_ylabel('Z Amplitude (deg/s)')

    axs[0].plot(frequencies, x_fft_s, 'red')
    axs[1].plot(frequencies, y_fft_s, 'yellow')
    axs[2].plot(frequencies, z_fft_s, 'blue')

    print("FIND PEAKS")
    peaks = find_peaks(x_fft_s, height = 50)
    dominant_peak_index = peaks[0][0]
    x_snr = 10*np.log(x_fft_s[dominant_peak_index]/x_fft_n[dominant_peak_index])
    print("Dominant Frequency for X", frequencies[peaks[0][0]])
    print("SNR at Dominant Frequency for X", x_snr)

    peaks = find_peaks(z_fft_s, height = 50)
    dominant_peak_index = peaks[0][0]
    z_snr = 10*np.log(z_fft_s[dominant_peak_index]/z_fft_n[dominant_peak_index])
    print("Dominant Frequency for Z", frequencies[peaks[0][0]])
    print("SNR at Dominant Frequency for Z", z_snr)

    print("FROM MAX VALUE")
    index_max = np.argmax(x_fft_s)
    print("Max value X", x_fft_s[index_max])
    print("Dominant Frequency for X MAX", frequencies[index_max])
    x_snr_max = 10*np.log(x_fft_s[index_max]/x_fft_n[index_max])
    print("SNR at Dominant Frequency for X based on MAX", x_snr_max)

    print("Max value Y", y_fft_s[index_max])
    print("Dominant Frequency for Y MAX", frequencies[index_max])
    y_snr_max = 10*np.log(y_fft_s[index_max]/y_fft_n[index_max])
    print("SNR at Dominant Frequency for X based on MAX", y_snr_max)

    index_max = np.argmax(z_fft_s)
    print("Max value Z", z_fft_s[index_max])
    print("Dominant Frequency for Z MAX", frequencies[index_max])
    z_snr_max = 10*np.log(z_fft_s[index_max]/z_fft_n[index_max])
    print("SNR at Dominant Frequency for Z based on MAX", z_snr_max)

    axs[2].set_xlabel('Frequency (Hz)')
    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

    axs[0].set_xlim(0,15)
    axs[1].set_xlim(0,15)
    axs[2].set_xlim(0,15)

    plt.show()  

tablea = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.13.45.876_D8E078ADF8A4_Accelerometer.csv'
tableg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.13.45.876_D8E078ADF8A4_Gyroscope.csv'

forarma = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.23.23.435_D8E078ADF8A4_Accelerometer.csv'
forarmg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.23.23.435_D8E078ADF8A4_Gyroscope.csv'

outerarma = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.50.32.537_D8E078ADF8A4_Accelerometer.csv'
outerarmg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.50.32.537_D8E078ADF8A4_Gyroscope.csv'

handa = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.17.43.005_D8E078ADF8A4_Accelerometer.csv'
handg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.17.43.005_D8E078ADF8A4_Gyroscope.csv'

handa1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.55.34.013_D8E078ADF8A4_Accelerometer.csv'

handsweta4beatsa = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T15.53.53.186_D8E078ADF8A4_Accelerometer.csv'
handsweta4beatsg = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T15.53.53.186_D8E078ADF8A4_Gyroscope.csv'

handsweta4beats2a = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T17.11.37.187_D8E078ADF8A4_Accelerometer.csv'
handswetabeats2g = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T17.11.37.187_D8E078ADF8A4_Gyroscope.csv'

table100a = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.38.05.023_D8E078ADF8A4_Accelerometer.csv'
table100g = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.38.05.023_D8E078ADF8A4_Gyroscope.csv'

hand100a = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.44.49.453_D8E078ADF8A4_Accelerometer.csv'
hand100g = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.44.49.453_D8E078ADF8A4_Gyroscope.csv'

hand100g2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.53.02.014_D8E078ADF8A4_Gyroscope.csv'

hand3g = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.55.56.792_D8E078ADF8A4_Gyroscope.csv'

handlod1g = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.01.18.796_D8E078ADF8A4_Gyroscope.csv'
handlod2g = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.08.11.710_D8E078ADF8A4_Gyroscope.csv'

swetahand1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.10.50.703_D8E078ADF8A4_Gyroscope.csv'

lodhand1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.20.25.776_D8E078ADF8A4_Gyroscope.csv'
lodhand2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.23.46.024_D8E078ADF8A4_Gyroscope.csv'

lodinarm1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.32.25.980_D8E078ADF8A4_Gyroscope.csv'
lodinarm2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.36.10.646_D8E078ADF8A4_Gyroscope.csv'

lodforout1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T13.55.22.416_D8E078ADF8A4_Gyroscope.csv'
lodforout2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.00.07.891_D8E078ADF8A4_Gyroscope.csv'

lodupin1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.08.18.620_D8E078ADF8A4_Gyroscope.csv'
lodupin2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.11.36.996_D8E078ADF8A4_Gyroscope.csv'

lodoutup1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.20.54.691_D8E078ADF8A4_Gyroscope.csv'
lodoutup2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.23.44.204_D8E078ADF8A4_Gyroscope.csv'

swetahand2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.30.52.661_D8E078ADF8A4_Gyroscope.csv'

swetainfor1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.34.35.868_D8E078ADF8A4_Gyroscope.csv'
swetainfor2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.37.15.974_D8E078ADF8A4_Gyroscope.csv'

swetainup1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.41.44.569_D8E078ADF8A4_Gyroscope.csv'
swetainup2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.44.53.024_D8E078ADF8A4_Gyroscope.csv'

swetaforout1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.49.47.328_D8E078ADF8A4_Gyroscope.csv'
swetaforout2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.52.31.307_D8E078ADF8A4_Gyroscope.csv'

swetaoutup2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.56.46.036_D8E078ADF8A4_Gyroscope.csv'
swetaoutup1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T14.59.00.851_D8E078ADF8A4_Gyroscope.csv'
swetaoutup2yes = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T15.04.00.917_D8E078ADF8A4_Gyroscope.csv'

lotupout3 = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T15.08.44.025_D8E078ADF8A4_Gyroscope.csv'
lodupout = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T15.11.54.198_D8E078ADF8A4_Gyroscope.csv'
plot_2d_graph(lodupout, table100g, accelerometer=False)