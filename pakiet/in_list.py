def szukaj():
    lista = ['V475', 'F987', 'Q143', 'R688']
    search = input('Podaj numer katalogowy: ')
    if search in lista:
        print(search, "został znaleziony na liście")
    else:
        print(search, "nie został znaleziony na liście")
