import datetime
import os

import matplotlib.pyplot as plt

try:
    from database import read_today
except ImportError:
    from .database import read_today


def graph(data_file_path: str) -> str:
    '''
    graph plot and save to image file.

    Args:
        data_file_path (str): database file path.

    Returns:
        str: generated image file path.
    '''
    today_data = read_today(data_file_path)

    temps = []
    hu = []

    jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    now = datetime.datetime.now(jst)

    directory = 'graph_image'
    # if directory not found it create directory.
    if not os.path.isdir(directory):
        os.makedirs(directory)
    image_file_path = os.path.join(directory, f'{now.strftime(r"%Y%m%d")}.png')

    # Sort by date.
    sorted_data = sorted(today_data, key=lambda x: x['date'])

    for element in sorted_data:
        temps.append(element['temp'])
        hu.append(element['hu'])

    # graph plot
    fig = plt.figure(figsize=[6.4, 4.8])
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    # line color
    ax1.plot(temps, color='blue')
    ax2.plot(hu, color='orange')

    # lavel of y
    ax1.set_ylabel('Temperature ($^\circ$C)')
    ax2.set_ylabel('Humidity (%)')

    ax1.grid(True)
    ax1.set_xlabel('date')
    ax1.tick_params(labelbottom=False, bottom=False)
    ax2.tick_params(labelbottom=False, bottom=False)
    plt.title(f'Graph of changes in room temperature and humidity on {now.strftime(r"%m/%d")}')

    plt.savefig(image_file_path)

    return image_file_path
