import pandas as pd

films = pd.read_csv('film.csv',
                    sep=";",
                    encoding="ISO-8859-1",
                    skiprows=[1],
                    )
print(films)