import pandas as pd



file_name = './database/netflix_titles.xlsx'
sheet = 'netflix_titles'

df = pd.read_excel(io=file_name, sheet_name=sheet)


df.to_csv('netflix_titles.csv', encoding='utf-8', index=False)