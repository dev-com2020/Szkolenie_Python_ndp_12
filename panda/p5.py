import pandas as pd


def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return False


# films = pd.read_csv('film.csv',
#                     sep=";",
#                     encoding="ISO-8859-1",
#                     skiprows=[1],
#                     dtype={'Length': 'float64'},
#                     converters={'Awards': zamien}
#                     )

films = pd.read_csv('film.csv',
                    sep=";",
                    encoding="ISO-8859-1",
                    skiprows=[1],
                    dtype={'Length': 'float64'},
                    converters={'Awards': lambda x: True if x == 'Yes' else False}
                    )
# print(films.groupby('Year').count())
# print(films.groupby('Year').Popularity.mean())
# print(films.groupby(['Year', 'Subject']).Length.mean())
# print(films.groupby('Year').agg({'Length': ['min', 'max'], 'Popularity': ['min', 'max']}))
print(films[(films['Year'] >= 1980) & (films['Year'] <= 1990)].groupby('Year').Length.mean())
