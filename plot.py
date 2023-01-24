import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./database/netflix_titles.csv')
print("Before:")
print(data[['type','release_year']])

data = data.loc[data['release_year'].isin([*range(2015, 2020)]), ['type',
'release_year']].copy()
data.dropna(inplace=True)
data['release_year'] = data['release_year'].astype('int')
print("After:")
print(data)




cross_tab_prop = pd.crosstab(index=data['release_year'],
                             columns=data['type'],
                             normalize="index")

cross_tab = pd.crosstab(index=data['release_year'],
                        columns=data['type'])


data = pd.read_csv('./database/treatment.csv', index_col=0)

# print(data.index)
# print(data.columns)
# cross_tab_prop = pd.crosstab(index=data.index,
#                              columns=data.columns,
#                              normalize="index")

# cross_tab = pd.crosstab(index=data.index,
#                         columns=data.columns)

# print(cross_tab_prop)
cross_tab_prop.plot(kind='bar', 
                    stacked=True, 
                    colormap='tab10', 
                    figsize=(10, 6))

plt.legend(loc="lower left", ncol=2)
plt.xlabel("Release Year")
plt.ylabel("Proportion")

for n, x in enumerate([*cross_tab.index.values]):
    for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
                                   cross_tab_prop.loc[x].cumsum()):

        plt.text(x=n - 0.17,
                 y=y_loc,
                 s=f'{np.round(proportion * 100, 1)}%', 
                 color="black",
                 fontsize=12,
                 fontweight="bold")

plt.show()