import pandas as pd
import statistics

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

def print_statistics(csv_file, accelerometer):

    xline, yline, zline, t = get_data(csv_file, accelerometer)

    x_stddev = statistics.stdev(xline)
    x_mean = statistics.mean(xline)
    x_median = statistics.median(xline)
    x_variance = statistics.variance(xline)

    y_stddev = statistics.stdev(yline)
    y_mean = statistics.mean(yline)
    y_median = statistics.median(yline)
    y_variance = statistics.variance(yline)

    z_stddev = statistics.stdev(zline)
    z_mean = statistics.mean(zline)
    z_median = statistics.median(zline)
    z_variance = statistics.variance(zline)

    print("Here's the statistical information about movement in the X direction:")
    print(f"Standard Deviation: {x_stddev}, Variance: {x_variance}, Mean: {x_mean}, Median: {x_median}")

    print("Here's the statistical information about movement in the Y direction:")
    print(f"Standard Deviation: {y_stddev}, Variance: {y_variance}, Mean: {y_mean}, Median: {y_median}")

    print("Here's the statistical information about movement in the Z direction:")
    print(f"Standard Deviation: {z_stddev}, Variance: {z_variance}, Mean: {z_mean}, Median: {z_median}")

def multiple_files(csv_files):
    for csv_file in csv_files:
        print_statistics(csv_file, accelerometer=True)

lodstanding2acc = '/Users/swetaramamani/Downloads/Elodie_2022-10-28T11.20.25.215_D8E078ADF8A4_Accelerometer.csv'
print_statistics(lodstanding2acc, accelerometer=True)