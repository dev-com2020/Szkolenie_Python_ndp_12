lista = [1, 3, 7, 11, 13, 17, 23]
cel = 17

licznik = 0
for i in lista:
    if i == cel:
        print("Znalazłem na pozycji", licznik)
        break
    else:
        if licznik == len(lista) - 1:
            print("Nie znalazłem celu")
    licznik += 1


def szukaj(lista, cel, pozycja):
    if lista[pozycja] == cel:
        print("Znalazłem na pozycji", pozycja)
        return
    elif pozycja == len(lista) - 1:
        print("Nie znalazłem celu")
        return
    szukaj(lista, cel, pozycja + 1)


dane = [1, 3, 7, 'tomek', 11, 'kasia']


def zlicz(lista, pozycja, ilosc):
    if pozycja == len(lista):
        return ilosc
    if type(lista[pozycja]) == int:
        return zlicz(lista, pozycja + 1, ilosc + 1)
    else:
        return zlicz(lista, pozycja + 1, ilosc)


print(zlicz(lista, 0, 0))
print(zlicz(dane, 0, 0))
# szukaj(lista, cel, 0)
