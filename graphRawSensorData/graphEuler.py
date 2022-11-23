import pandas as pd
import matplotlib.pyplot as plt

colours = ['#84AAFF','#1e90ff', '#1b82e6', '#1873cc', '#1565b3', '#125699', '#0f4880', '#0c3a66', '#092b4d', '#061d33', '#011D5B']
# colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'grey', 'brown', 'black']
FLUCTUATION_ANGLE = 90
def compensate_for_fluctuations(xline, yline, zline):
    for idx, x in enumerate(xline):
        if idx == 0:
            xline[idx] = 0 # Force the first angle to be zero
        else:
            if abs(x) - abs(xline[idx - 1]) >= FLUCTUATION_ANGLE:
                xline[idx] = xline[idx - 1]

    for idx, y in enumerate(yline):
        if idx == 0:
            yline[idx] = 0 # Force the first angle to be zero
        else:
            if abs(y) - abs(yline[idx - 1]) >= FLUCTUATION_ANGLE:
                yline[idx] = yline[idx - 1]

    for idx, z in enumerate(zline):

        if idx == 0:
            zline[idx] = 0 # Force the first angle to be zero
        else:
            if abs(z) - abs(zline[idx - 1]) >= FLUCTUATION_ANGLE:
                zline[idx] = zline[idx - 1]
    
    return xline, yline, zline


def get_data(csv_file):
    df = pd.read_csv(csv_file)
    df.head()

    # Collecting data from reading CSV
    xline = df['pitch (deg)']
    yline = df['roll (deg)']
    zline = df['yaw (deg)']
    wline = df['heading (deg)']
    t = df['elapsed (s)']

    xline, yline, zline = compensate_for_fluctuations(xline, yline, zline)

    return xline, yline, zline, wline, t

def plot_2d_graph(csv_file):

    xline, yline, zline, wline, t = get_data(csv_file,)

    fig, axs = plt.subplots(3)
    fig.suptitle('Eulers Angles Data for Calibration (Y up)')

    axs[2].plot(t, xline, 'red')
    axs[1].plot(t, yline, 'orange')
    axs[0].plot(t, zline, 'blue')
    # axs[3].plot(t, wline, 'green')

    axs[1].set_ylabel('Roll (deg)')
    axs[2].set_ylabel('Pitch (deg)')
    axs[0].set_ylabel('Yaw (deg)')
    # axs[3].set_ylabel('Heading (deg)')
    axs[2].set_xlabel('Time Elapsed (s)')

    # axs[0].set_xlim(40, 50)
    # axs[1].set_xlim(40, 50)
    # axs[2].set_xlim(40, 50)

    plt.show()

tes = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.14.16.294_D8E078ADF8A4_EulerAngles.csv'
test2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.29.52.997_D8E078ADF8A4_EulerAngles.csv'
spin = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.39.31.777_D8E078ADF8A4_EulerAngles.csv'
up = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.48.23.520_D8E078ADF8A4_EulerAngles.csv'
laptop = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.55.36.660_D8E078ADF8A4_EulerAngles.csv'

lop = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T19.23.17.472_D8E078ADF8A4_EulerAngles.csv'
crazy = '/Users/swetaramamani/Downloads/Elodie_2022-11-17T15.02.31.690_D8E078ADF8A4_EulerAngles.csv'

yes = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T11.19.49.169_D8E078ADF8A4_EulerAngles.csv'

lodcalib = '/Users/swetaramamani/Downloads/Elodie_2022-11-20T16.16.53.598_D8E078ADF8A4_EulerAngles.csv'
lodangle_x = '/Users/swetaramamani/Downloads/angle_x_calib.csv'
lodangle_y = '/Users/swetaramamani/Downloads/angle_y_calib.csv'
lodangle_x_2 = '/Users/swetaramamani/Downloads/angle_x_calib_2.csv'

lod = '/Users/swetaramamani/Downloads/22_angles_y_mid_short.csv'
plot_2d_graph(lod)


