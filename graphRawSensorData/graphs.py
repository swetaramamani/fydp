import pandas as pd
import matplotlib.pyplot as plt

colours = ['#84AAFF','#1e90ff', '#1b82e6', '#1873cc', '#1565b3', '#125699', '#0f4880', '#0c3a66', '#092b4d', '#061d33', '#011D5B']
# colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'grey', 'brown', 'black']

def split(list_x, list_y, list_z, chunk_size):

  max_length = max(len(list_x), len(list_y), len(list_z))

  for i in range(0, max_length, chunk_size):
    yield list_x[i:i + chunk_size], list_y[i:i + chunk_size], list_z[i:i + chunk_size]

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

def normalize_data(xline, yline, zline):

    range_x = max(xline) - min(xline)
    range_y = max(yline) - min(yline)
    range_z = max(zline) - min(zline)

    x_normalized = (xline - min(xline))/range_x
    y_normalized = (yline - min(yline))/range_y
    z_normalized = (zline - min(zline))/range_z
    
    return x_normalized, y_normalized, z_normalized

def plot_3d_graph(csv_file, accelerometer, chunk_size):

    xline, yline, zline, t = get_data(csv_file, accelerometer)

    # Split each array into equal chucks based on time (eg. first 5 seconds is light red)
    colour_chunks =list(split(xline, yline, zline, chunk_size))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # Plot each chunk with time gradient on the same 3D graph
    for i in range(len(colour_chunks)):
        ax.plot3D(colour_chunks[i][0], colour_chunks[i][1], colour_chunks[i][2], colours[i])

    # Shor graph and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set axes ranges
    # ax.set_xlim(-1,1)
    # ax.set_ylim(-1,1)
    # ax.set_zlim(-1,1)
    plt.show()

def plot_2d_graph(csv_file, accelerometer):

    xline, yline, zline, t = get_data(csv_file, accelerometer)
    x_normalized, y_normalized, z_normalized = normalize_data(xline, yline, zline)

    fig, axs = plt.subplots(3)
    if accelerometer:
        fig.suptitle('Accelerometer Data from Table Test')
        axs[0].set_ylabel('X (g)')
        axs[1].set_ylabel('Y (g)')
        axs[2].set_ylabel('Z (g)')
    else:
        fig.suptitle('Gyroscope SNR Testing (Hand): Subject 1, Trial 1')
        axs[0].set_ylabel('X (deg/s)')
        axs[1].set_ylabel('Y (deg/s)')
        axs[2].set_ylabel('Z (deg/s)')

    axs[0].plot(t, xline, 'red')
    axs[1].plot(t, yline, 'green')
    axs[2].plot(t, zline, 'blue')
    axs[2].set_xlabel('Time (s)')
    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

    # axs[0].set_ylim(-1.5,1.5)
    # axs[1].set_ylim(-1.5,1.5)
    # axs[2].set_ylim(-1.5,1.5)

    plt.show()


graph_name1 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.58.21.576_E62D46F1F0F5_Accelerometer.csv'
graph_name2 = '//Users/swetaramamani/Downloads/Den 1_2022-10-25T14.49.57.271_E62D46F1F0F5_Accelerometer.csv'
graph_name3 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.30.53.139_E62D46F1F0F5_Gyroscope.csv'
graph_name4 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.30.53.139_E62D46F1F0F5_Accelerometer.csv'
graph5 = '//Users/swetaramamani/Downloads/Elodie_2022-10-26T14.23.30.692_D8E078ADF8A4_Accelerometer.csv'
# plot_3d_graph(graph_name2, accelerometer=True, chunk_size=40)

table1acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.25.54.911_D8E078ADF8A4_Accelerometer.csv'
table1gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.25.54.911_D8E078ADF8A4_Gyroscope.csv'

table2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.26.45.881_D8E078ADF8A4_Accelerometer.csv'
table2gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.26.45.881_D8E078ADF8A4_Gyroscope.csv'

table3acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.27.40.361_D8E078ADF8A4_Accelerometer.csv'
table3gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.27.40.361_D8E078ADF8A4_Gyroscope.csv'

emmastanding1acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T10.27.40.361_D8E078ADF8A4_Accelerometer.csv'
emmastanding1gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.02.18.763_D8E078ADF8A4_Gyroscope.csv'

emmastanding2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.03.24.114_D8E078ADF8A4_Accelerometer.csv'
emmastanding2gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.03.24.114_D8E078ADF8A4_Gyroscope.csv'

nooshstanding1acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.13.06.354_D8E078ADF8A4_Accelerometer.csv'
nooshstanding1gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.13.06.354_D8E078ADF8A4_Gyroscope.csv'

nooshstanding2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.14.26.867_D8E078ADF8A4_Accelerometer.csv'
nooshstanding2gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.14.26.867_D8E078ADF8A4_Gyroscope.csv'

lodstanding1acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.19.16.533_D8E078ADF8A4_Accelerometer.csv'
lodstanding1gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.19.16.533_D8E078ADF8A4_Gyroscope.csv'

lodstanding2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.20.25.215_D8E078ADF8A4_Accelerometer.csv'
lodstanding2gyr = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.20.25.215_D8E078ADF8A4_Gyroscope.csv'

forarma = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.23.23.435_D8E078ADF8A4_Accelerometer.csv'
forarmg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.23.23.435_D8E078ADF8A4_Gyroscope.csv'

handa = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.17.43.005_D8E078ADF8A4_Accelerometer.csv'
handg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.17.43.005_D8E078ADF8A4_Gyroscope.csv'

handa1 = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T17.55.34.013_D8E078ADF8A4_Accelerometer.csv'

tablea = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.13.45.876_D8E078ADF8A4_Accelerometer.csv'
tableg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T16.13.45.876_D8E078ADF8A4_Gyroscope.csv'

laptopa = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T20.46.31.713_D8E078ADF8A4_Accelerometer.csv'
laptopg = '/Users/swetaramamani/Downloads/Elodie_2022-11-14T20.46.31.713_D8E078ADF8A4_Gyroscope.csv'

handsweta4beatsa = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T15.53.53.186_D8E078ADF8A4_Accelerometer.csv'
handsweta4beatsg = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T15.53.53.186_D8E078ADF8A4_Gyroscope.csv'

handsweta4beats2a = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T17.11.37.187_D8E078ADF8A4_Accelerometer.csv'
handswetabeats2g = '/Users/swetaramamani/Downloads/Elodie_2022-11-15T17.11.37.187_D8E078ADF8A4_Gyroscope.csv'

table100a = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.38.05.023_D8E078ADF8A4_Accelerometer.csv'
table100g = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.38.05.023_D8E078ADF8A4_Gyroscope.csv'

hand100a = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.44.49.453_D8E078ADF8A4_Accelerometer.csv'
hand100g = '/Users/swetaramamani/Downloads/Elodie_2022-11-18T10.44.49.453_D8E078ADF8A4_Gyroscope.csv'

plot_2d_graph(hand100a, accelerometer=True)


