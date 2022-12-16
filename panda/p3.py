import pandas as pd

miasta = pd.read_csv('worldcities.csv')
# print(miasta[10:20])
# print(miasta.head())
# print(miasta.tail())
# print(miasta[5:500:15])
# miasta[5:500:15][['city', 'iso2', 'capital']].to_excel('test3.xlsx')
print(miasta.info())
print(miasta.describe())
miasta.id.describe().to_csv('tt.csv')
