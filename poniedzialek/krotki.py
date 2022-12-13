dane = ('G6473', 232, True)
dane2 = 'G6473', 232, True
dane3 = 'G6473',
print(dane)
print(dane2[0:2])
print(dane3)
liczby = 12, 22, 35, 99, 299
print(liczby)
l1, l2, *l3 = liczby
print(l1)
print(l2)
l3.append(1233)
print(l3)
liczby2 = 12, 22, 35, 99, 299
nowa_lista = list(liczby2)
nowa_lista.reverse()
nowa_lista.append("Tomek")
print(nowa_lista)
liczby2 = tuple(nowa_lista)
print(liczby2)


