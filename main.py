import pandas as pd
import re

data = pd.read_csv('vacancies.csv').dropna()
tags = data.columns.tolist()

data = data.astype('int32', copy=True, errors='ignore')
if 'premium' in tags:
    data['premium'].replace({0: 'FALSE', 1: 'TRUE'}, inplace=True)
if 'salary_gross' in tags:
    data['salary_gross'].replace({False: 'FALSE', True: 'TRUE'}, inplace=True)
data = data.astype('str')

job_list = data.values.tolist()
for i in range(len(data.columns)):
    for j in range(len(job_list)):
        job_list[j][i] = re.sub('<[^<]+?>', '',job_list[j][i])
        job_list[j][i] = re.sub('\n', ', ',job_list[j][i])
        job_list[j][i] = re.sub('\r', '',job_list[j][i])
        job_list[j][i] = re.sub(r'\s+', ' ',job_list[j][i]).strip()

key = tuple(data.columns)
dictionary = {}
for i in key:
    dictionary[i] = None

for j in range(len(job_list)):
    for i in range(len(tags)):
        dictionary[tags[i]] = job_list[j][i]
        print(f"{key[i]}: {dictionary[tags[i]]} ")
    print()