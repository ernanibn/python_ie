import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data = pd.read_csv('./database/netflix_titles.csv', sep=';')

# data = data.loc[data['release_year'].isin([*range(2016, 2020)]), ['type', 'release_year']].copy()
# data.dropna(inplace=True)
# data['release_year'] = data['release_year'].astype('int')
# data

# cross_tab_prop = pd.crosstab(index=data['release_year'],
#                              columns=data['type'],
#                              normalize="index")
# cross_tab_prop


file_name = './database/netflix_titles.xlsx'
sheet = 'netflix_titles'

df = pd.read_excel(io=file_name, sheet_name=sheet)


df.to_csv('netflix_titles.csv', encoding='utf-8', index=False)