import pandas as pd
import numpy as np
import re

df = pd.read_csv('Facility-Facility1-To-Satellite-SSO470_Access.csv')
print(df)


format = '4 Aug 2021 13:38:39.198'

def convert_date(date_utcg):
	m = re.serach('', date_utcg)
