def szukaj():
    lista = ['V475', 'F987', 'Q143', 'R688']
    search = input('Podaj numer katalogowy: ')
    if search in lista:
        return dict({search: "został znaleziony na liście"})
    else:
        print(search, "nie został znaleziony na liście")


def odejmowanie(a=0, b=0):
    wynik = a - b
    return wynik
