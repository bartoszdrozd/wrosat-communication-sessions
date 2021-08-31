import numpy as np
import time
import calendar
import matplotlib.pyplot as plt


def access_times(df, item_index, duration_list, file_name):
    # one fuction to show data about accesses in one specific csv file
    # improve that loop so it automatically sets limit value
    for i in range(1, len(df)):
        if df['Duration (sec)'][i] < 50:
            item_index[0] += 1
        elif df['Duration (sec)'][i] < 100:
            item_index[1] += 1
        elif df['Duration (sec)'][i] < 150:
            item_index[2] += 1
        elif df['Duration (sec)'][i] < 200:
            item_index[3] += 1
        elif df['Duration (sec)'][i] < 250:
            item_index[4] += 1
        elif df['Duration (sec)'][i] < 300:
            item_index[5] += 1
        elif df['Duration (sec)'][i] < 350:
            item_index[6] += 1
        elif df['Duration (sec)'][i] < 400:
            item_index[7] += 1
        elif df['Duration (sec)'][i] < 450:
            item_index[8] += 1
        elif df['Duration (sec)'][i] < 500:
            item_index[9] += 1
        elif df['Duration (sec)'][i] < 550:
            item_index[10] += 1

    # with open(f'{file_name}.txt', 'w+') as file:
    # 	#file.write(f"Max access time: {max_value}\n")
    # 	file.write(f"Median of access times: {df['Duration (sec)'].median()}\n")
    # 	file.write(f"Mean access time: {df['Duration (sec)'].mean()}")

    y_pos = np.arange(len(item_index))
    plt.figure(0)
    plt.bar(y_pos, item_index, align='center', alpha=0.5)
    plt.xticks(y_pos, duration_list)
    plt.ylabel('Liczba dostępów')
    plt.xlabel('Czas[s]')
    plt.title(f'Długość sesji komunikacyjnych dla {file_name}')
    plt.savefig(f'figures/{file_name}.png')
    plt.clf()


def access_calculation(df, file_name):
    """second function to show data about time in beetween two consequetive accesses
    date_format = '4 Aug 2021 13:38:39.198'
    calendar.timegm(time.strptime(date_format, '%e %b %Y  %H:%M:%S.%f'))"""
    window_list = []
    date_list = []
    for i in range(1, len(df)):
        if df['Stop Time (UTCG)'][i] and df['Start Time (UTCG)'][i + 1]:
            access_end = calendar.timegm(time.strptime(df['Stop Time (UTCG)'][i], '%d %b %Y  %H:%M:%S.%f'))
            next_access_start = calendar.timegm(time.strptime(df['Start Time (UTCG)'][i + 1], '%d %b %Y  %H:%M:%S.%f'))
            window_time = next_access_start - access_end
            window_list.append(window_time)
            date_list.append(df['Stop Time (UTCG)'][i])

    plt.figure()
    plt.ylabel(f'Długość przerwy radiowej dla {file_name}[s]')
    plt.xlabel('Czas od rozpoczęcia misji')
    plt.title(f'Długość przerw radiowych dla {file_name}')
    plt.scatter(date_list, window_list)
    plt.savefig(f'figures/length_of_silence_for_{file_name}.png')
    plt.clf()
