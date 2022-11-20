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
    xline = df['w (number)']
    yline = df['x (number)']
    zline = df['y (number)']
    wline = df['z (number)']
    t = df['elapsed (s)']

    return xline, yline, zline, wline, t

def plot_2d_graph(csv_file):

    xline, yline, zline, wline, t = get_data(csv_file,)

    fig, axs = plt.subplots(4)

    axs[0].plot(t, xline, 'red')
    axs[1].plot(t, yline, 'orange')
    axs[2].plot(t, zline, 'blue')
    axs[3].plot(t, wline, 'green')

    axs[0].set_ylabel('W')
    axs[1].set_ylabel('X')
    axs[2].set_ylabel('Y')
    axs[3].set_ylabel('Z')

    plt.show()


test = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T18.59.23.166_D8E078ADF8A4_Quaternion.csv'

plot_2d_graph(test)


