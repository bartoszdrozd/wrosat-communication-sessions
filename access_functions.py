import numpy as np
import time
import calendar
import matplotlib.pyplot as plt


def access_times(df, itemIndex, durationList, file_name):
    # one fuction to show data about accesses in one specific csv file
    # improve that loop so it automatically sets limit value
    for i in range(1, len(df)):
        if df['Duration (sec)'][i] < 50:
            itemIndex[0] += 1
        elif df['Duration (sec)'][i] < 100:
            itemIndex[1] += 1
        elif df['Duration (sec)'][i] < 150:
            itemIndex[2] += 1
        elif df['Duration (sec)'][i] < 200:
            itemIndex[3] += 1
        elif df['Duration (sec)'][i] < 250:
            itemIndex[4] += 1
        elif df['Duration (sec)'][i] < 300:
            itemIndex[5] += 1
        elif df['Duration (sec)'][i] < 350:
            itemIndex[6] += 1
        elif df['Duration (sec)'][i] < 400:
            itemIndex[7] += 1
        elif df['Duration (sec)'][i] < 450:
            itemIndex[8] += 1
        elif df['Duration (sec)'][i] < 500:
            itemIndex[9] += 1
        elif df['Duration (sec)'][i] < 550:
            itemIndex[10] += 1

    # with open(f'{file_name}.txt', 'w+') as file:
    # 	#file.write(f"Max access time: {max_value}\n")
    # 	file.write(f"Median of access times: {df['Duration (sec)'].median()}\n")
    # 	file.write(f"Mean access time: {df['Duration (sec)'].mean()}")

    y_pos = np.arange(len(itemIndex))
    plt.bar(y_pos, itemIndex, align='center', alpha=0.5)
    plt.xticks(y_pos, durationList)
    plt.ylabel('No of accesses')
    plt.xlabel('Sec')
    plt.title('Access Duration')
    plt.savefig(f'figures/{file_name}.png')


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

    plt.ylabel('Time in between accesses [seconds]')
    plt.xlabel('Time')
    plt.title(f'Length of radio silence for {file_name}')
    plt.scatter(date_list, window_list)
    plt.savefig(f'figures/length_of_silence_for_{file_name}.png')
