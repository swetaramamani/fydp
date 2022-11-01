from typing import List
import pandas as pd
import matplotlib.pyplot as plt

def get_data(csv_files, accelerometer):
    trial_data = []
    for csv_file in csv_files:
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
        
        trial_data.append([xline, yline, zline, t])

    return trial_data

def average_data(trial_data):
    # Only average until the minimum trial time
    # min_t = trial_data[0][3]
    # for trial in trial_data:
    #     if trial[3] < min_t:
    #         min_t = trial[3]

    # Averaged data
    x_summed = 0
    y_summed = 0
    z_summed = 0
    t_summed = 0
    for trial in trial_data:
        x_summed = x_summed + trial[0]
        y_summed = y_summed + trial[1]
        z_summed = z_summed + trial[2]
        t_summed = t_summed + trial[3]

    x_averaged = x_summed/len(trial_data)
    y_averaged = y_summed/len(trial_data)
    z_averaged = z_summed/len(trial_data)
    t_averaged = t_summed/len(trial_data)

    return x_averaged, y_averaged, z_averaged, t_averaged

def plot_2d_graph(csv_files, accelerometer):

    trial_data = get_data(csv_files, accelerometer)
    x_averaged, y_averaged, z_averaged, t = average_data(trial_data)

    fig, axs = plt.subplots(3)
    if accelerometer:
        fig.suptitle('Averaged Accelerometer Data')
        axs[0].set_ylabel('X (g)')
        axs[1].set_ylabel('Y (g)')
        axs[2].set_ylabel('Z (g)')
    else:
        fig.suptitle('Averaged Gyroscope Data')
        axs[0].set_ylabel('X (deg/s)')
        axs[1].set_ylabel('Y (deg/s)')
        axs[2].set_ylabel('Z (deg/s)')

    axs[0].plot(t, x_averaged, 'red')
    axs[1].plot(t, y_averaged, 'yellow')
    axs[2].plot(t, z_averaged, 'blue')
    axs[2].set_xlabel('Time (s)')
    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

    plt.show()  

lodstanding1acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.19.16.533_D8E078ADF8A4_Accelerometer.csv'
lodstanding1gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.19.16.533_D8E078ADF8A4_Gyroscope.csv'

lodstanding2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.20.25.215_D8E078ADF8A4_Accelerometer.csv'
lodstanding2gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.20.25.215_D8E078ADF8A4_Gyroscope.csv'

plot_2d_graph(csv_files=[lodstanding1acc, lodstanding2acc], accelerometer=True)