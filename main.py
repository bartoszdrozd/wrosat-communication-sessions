import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv('Facility-Facility1-To-Satellite-SSO590_Access.csv', index_col='Access')

# date_format = '4 Aug 2021 13:38:39.198'

# #one fuction to show data about specific access
durationList= list(range(50,550,50))
itemIndex = [0,0,0,0,0,0,0,0,0,0]

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

y_pos = np.arange(len(itemIndex))
plt.bar(y_pos, itemIndex, align='center', alpha=0.5)
plt.xticks(y_pos, durationList)
plt.ylabel('No of accesses')
plt.ylabel('Sec')
plt.title('Access Duration')
plt.show()

#second function to show data about time in beetween two consequetive accesses

def AccessCalc(date_utcg):
	m = re.serach('', date_utcg)
