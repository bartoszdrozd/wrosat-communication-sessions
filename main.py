import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv('Facility-Facility1-To-Satellite-SSO470_Access.csv', index_col='Access')
print(df)
print(len(df))
df.describe()

# date_format = '4 Aug 2021 13:38:39.198'

# #one fuction to show data about specific access

itemIndex = {50: 0, 100: 0, 150: 0, 200: 0, 250: 0, 300: 0, 350: 0, 400: 0, 450: 0, 500: 0}
durationList = []
for i in range(1, len(df)):
	if df['Duration (sec)'][i] < 50:
		itemIndex[50] += 1
	elif df['Duration (sec)'][i] < 100:
		itemIndex[100] += 1
	elif df['Duration (sec)'][i] < 150:
		itemIndex[150] += 1
	elif df['Duration (sec)'][i] < 200:
		itemIndex[200] += 1
	elif df['Duration (sec)'][i] < 250:
		itemIndex[250] += 1
	elif df['Duration (sec)'][i] < 300:
		itemIndex[300] += 1
	elif df['Duration (sec)'][i] < 350:
		itemIndex[350] += 1
	elif df['Duration (sec)'][i] < 400:
		itemIndex[400] += 1
	elif df['Duration (sec)'][i] < 450:
		itemIndex[450] += 1
	elif df['Duration (sec)'][i] < 500:
		itemIndex[500] += 1
		
#  # duration = accessStopTimesEpSec[i] - accessStartTimesEpSec[i]
#  # durationList.append(duration)
#  # itemIndex.append(i + 1)
# y_pos = np.arange(len(df))
# plt.bar(y_pos, durationList, align='center', alpha=0.5)
# plt.xticks(y_pos, itemIndex)
# plt.ylabel('Sec')
# plt.title('Access Duration')
# plt.show()

print(itemIndex)

#second function to show data about time in beetween two consequetive accesses

def AccessCalc(date_utcg):
	m = re.serach('', date_utcg)
