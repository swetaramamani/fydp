import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq

ACC_SAMPLE_RATE = 12.5 #Hertz

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

    np.array(yline_s)
    y_fft_s = rfft(yline_s.values)

    np.array(zline_s)
    z_fft_s = rfft(zline_s.values)

    np.array(xline_n)
    x_fft_n = rfft(xline_n.values)

    np.array(yline_n)
    y_fft_n = rfft(yline_n.values)

    np.array(zline_n)
    z_fft_n = rfft(zline_n.values)
    
    return x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n

def plot_2d_graph(csv_file_s, csv_file_n, accelerometer):

    xline_s, yline_s, zline_s, t_s = get_data(csv_file_s, accelerometer)
    xline_n, yline_n, zline_n, t_n = get_data(csv_file_n, accelerometer)
    x_fft_s, y_fft_s, z_fft_s, x_fft_n, y_fft_n, z_fft_n = get_fft(xline_s, yline_s, zline_s, xline_n, yline_n, zline_n)
    frequencies = rfftfreq(len(t_s), 1 / ACC_SAMPLE_RATE)

    fig, axs = plt.subplots(3)
    if accelerometer:
        fig.suptitle('FFT Accelerometer Data')
        axs[0].set_ylabel('X (dB)')
        axs[1].set_ylabel('Y (dB)')
        axs[2].set_ylabel('Z (dB)')
    else:
        fig.suptitle('FFT Gyroscope Data')
        axs[0].set_ylabel('X (dB)')
        axs[1].set_ylabel('Y (dB)')
        axs[2].set_ylabel('Z (dB)')

    axs[0].plot(frequencies, np.abs(x_fft_s), 'red')
    axs[1].plot(frequencies, np.abs(y_fft_s), 'yellow')
    axs[2].plot(frequencies, np.abs(z_fft_s), 'blue')

    axs[2].set_xlabel('Frequency (Hz)')
    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

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

plot_2d_graph(handg, tableg, accelerometer=False)