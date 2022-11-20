import pandas as pd
import matplotlib.pyplot as plt

colours = ['#84AAFF','#1e90ff', '#1b82e6', '#1873cc', '#1565b3', '#125699', '#0f4880', '#0c3a66', '#092b4d', '#061d33', '#011D5B']
# colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'grey', 'brown', 'black']

def split(list_x, list_y, list_z, chunk_size):

  max_length = max(len(list_x), len(list_y), len(list_z))

  for i in range(0, max_length, chunk_size):
    yield list_x[i:i + chunk_size], list_y[i:i + chunk_size], list_z[i:i + chunk_size]

def get_data(csv_file):
    df = pd.read_csv(csv_file)
    df.head()

    # Collecting data from reading CSV
    xline = df['pitch (deg)']
    yline = df['roll (deg)']
    zline = df['yaw (deg)']
    wline = df['heading (deg)']
    t = df['elapsed (s)']

    return xline, yline, zline, wline, t

def plot_2d_graph(csv_file):

    xline, yline, zline, wline, t = get_data(csv_file,)

    fig, axs = plt.subplots(3)
    fig.suptitle('Euler Angles Test Shoulder Abduction/Adduction')

    axs[0].plot(t, xline, 'red')
    axs[1].plot(t, yline, 'orange')
    axs[2].plot(t, zline, 'blue')
    # axs[3].plot(t, wline, 'green')

    axs[0].set_ylabel('Pitch (deg)')
    axs[1].set_ylabel('Roll (deg)')
    axs[2].set_ylabel('Yaw (deg)')
    # axs[3].set_ylabel('Heading (deg)')
    axs[2].set_xlabel('Time Elapsed (s)')

    plt.show()

tes = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.14.16.294_D8E078ADF8A4_EulerAngles.csv'
test2 = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.29.52.997_D8E078ADF8A4_EulerAngles.csv'
spin = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.39.31.777_D8E078ADF8A4_EulerAngles.csv'
up = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.48.23.520_D8E078ADF8A4_EulerAngles.csv'
laptop = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.55.36.660_D8E078ADF8A4_EulerAngles.csv'

lop = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T19.23.17.472_D8E078ADF8A4_EulerAngles.csv'
crazy = '/Users/swetaramamani/Downloads/Elodie_2022-11-17T15.02.31.690_D8E078ADF8A4_EulerAngles.csv'

yes = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T11.19.49.169_D8E078ADF8A4_EulerAngles.csv'

plot_2d_graph(lop)


