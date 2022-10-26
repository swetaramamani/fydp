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

    fig, axs = plt.subplots(3)
    if accelerometer:
        fig.suptitle('Accelerometer Data from ' + csv_file[32:49])
        axs[0].set_ylabel('X (m/s)')
        axs[1].set_ylabel('Y (m/s)')
        axs[2].set_ylabel('Z (m/s)')
    else:
        fig.suptitle('Gyroscope Data from ' + csv_file[31:47])
        axs[0].set_ylabel('X (deg/s)')
        axs[1].set_ylabel('Y (deg/s)')
        axs[2].set_ylabel('Z (deg/s)')

    axs[0].plot(t, xline, 'red')
    axs[1].plot(t, yline, 'yellow')
    axs[2].plot(t, zline, 'blue')
    axs[2].set_xlabel('Time (s)')
    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

    plt.show()


graph_name1 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.58.21.576_E62D46F1F0F5_Accelerometer.csv'
graph_name2 = '//Users/swetaramamani/Downloads/Den 1_2022-10-25T14.49.57.271_E62D46F1F0F5_Accelerometer.csv'
graph_name3 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.30.53.139_E62D46F1F0F5_Gyroscope.csv'
graph_name4 = '/Users/swetaramamani/Downloads/Den 1_2022-10-25T14.30.53.139_E62D46F1F0F5_Accelerometer.csv'
graph5 = '//Users/swetaramamani/Downloads/Elodie_2022-10-26T14.23.30.692_D8E078ADF8A4_Accelerometer.csv'
# plot_3d_graph(graph_name2, accelerometer=True, chunk_size=40)
plot_2d_graph(graph5, accelerometer=True)


