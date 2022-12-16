import pandas as pd

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})


def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'

def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return False




df.Wynik = df.Wynik.apply(sprawdz)
print(df)
