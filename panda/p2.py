import pandas as pd

imiona = pd.read_excel('imiona.xlsx')
# print(imiona)

imiona2 = pd.read_excel('imiona.xlsx', sheet_name='Wynik', header=1)
# print(imiona2)

imiona3 = pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None)
imiona3.columns = ['Imie', "Nazwisko", 'Wynik']
# print(imiona3)

imiona4 = pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names=['Imie', "Nazwisko", 'Wynik'])
print(imiona4)
