import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium[:10][['region', '1']])
# print(kostium.index)
# print(kostium.region.is_unique)
# kostium.set_index('region', inplace=True)
# kostium.to_excel('ttt.xlsx')
# print(kostium.loc['Arizona'])
# kostium.loc["Arizona", "1"] = "Batman"
# kostium.loc[3, "1"] = "Batman"
# print(kostium)
# print(kostium.iloc[3, 2])

# for i, zaw in kostium.iterrows():
#     if zaw['1'] == 'Rabbit':
#         print(zaw['region'])

# print(kostium['1'] == 'Rabbit')
# print(kostium[kostium['1'] == 'Rabbit'])
# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Dinosaur')])
# print(kostium[(kostium['1'] == 'Rabbit') & (kostium['4'] == 'Dinosaur')])

kostium['Nowa'] = "brak"
kostium.loc[kostium['1'] == 'Doll', 'Nowa'] = "jest"
# print(kostium.rename(columns={"1": 'Pierwsze_miejsce'}))
kostium['Złączone'] = kostium['2'] + " / " + kostium['3']

# kostium.to_excel("ttt.xlsx")