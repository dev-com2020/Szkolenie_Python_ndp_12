import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium[:10][['region', '1']])
# print(kostium.index)
# print(kostium.region.is_unique)
# kostium.set_index('region', inplace=True)
# kostium.to_excel('ttt.xlsx')
# print(kostium.loc['Arizona'])
# kostium.loc["Arizona", "1"] = "Batman"
kostium.loc[3, "1"] = "Batman"
print(kostium)
print(kostium.iloc[3, 2])
