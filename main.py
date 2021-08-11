import os
import pandas as pd
import numpy as np
import time
import calendar
import re
import matplotlib.pyplot as plt

# ------- Prepare full automation with report creation --------- 
# pathName = os.getcwd()

# numFiles = []
# fileNames = os.listdir(pathName)
# for fileNames in fileNames:
#     if fileNames.endswith(".csv"):
#         numFiles.append(fileNames)

file_to_search = 'Facility-Facility1-To-Satellite-SSO650_Access.csv'
df = pd.read_csv(file_to_search, index_col='Access')
file_name = re.search('[A-Z]{3}\d{0,3}',file_to_search).group(0)
column = df['Duration (sec)']
max_value = int(column.max())
durationList= list(range(50,max_value+50,50))
itemIndex = [0] * len(durationList)
min_access = df

#one fuction to show data about accesses in one specific csv file
#improve that loop so it automatically sets limit value 
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

with open(f'{file_name}.txt', 'w+') as file:
	file.write(f"Max access time: {max_value}\n")
	file.write(f"Median of access times: {df['Duration (sec)'].median()}\n")
	file.write(f"Mean access time: {df['Duration (sec)'].mean()}")

y_pos = np.arange(len(itemIndex))
plt.bar(y_pos, itemIndex, align='center', alpha=0.5)
plt.xticks(y_pos, durationList)
plt.ylabel('No of accesses')
plt.xlabel('Sec')
plt.title('Access Duration')
plt.savefig(f'{file_name}.png')

#second function to show data about time in beetween two consequetive accesses
# date_format = '4 Aug 2021 13:38:39.198'
# calendar.timegm(time.strptime(date_format, '%e %b %Y  %H:%M:%S.%f'))

def AccessCalc(df):
	window_list = []
	time_ranges = [0,0,0,0,0]
	times = [5400,27900,33425,36200,41775]
	for i in range(1, len(df)):
		if df['Stop Time (UTCG)'][i] and df['Start Time (UTCG)'][i+1]:
			access_end = calendar.timegm(time.strptime(df['Stop Time (UTCG)'][i], '%d %b %Y  %H:%M:%S.%f'))
			next_access_start = calendar.timegm(time.strptime(df['Start Time (UTCG)'][i+1], '%d %b %Y  %H:%M:%S.%f'))
			window_time = next_access_start - access_end
			window_list.append(window_time)
			if 5200 < window_time < 5600:
				time_ranges[0] += 1
			elif 27800 < window_time < 28000:
				time_ranges[1] += 1
			elif 33400 < window_time < 33450:
				time_ranges[2] += 1
			elif 36100 < window_time < 36300:
				time_ranges[3] += 1
			elif 41700 < window_time < 41850:
				time_ranges[4] += 1
		else:
			return

	y_pos2 = np.arange(len(time_ranges))
	plt.bar(y_pos2, time_ranges, align='center')
	plt.xticks(y_pos2, times)
	plt.show()
	print(window_list)

AccessCalc(df)
