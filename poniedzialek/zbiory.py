names = {'IBM', 'SPACEX', 'HPE'}
names.add('IBM')
names.add('CAT')
names.add('HPE')
print(names)

lista = [5, 7, 3, 4, 9, 5, 7, 9]
lista2 = [5, 7, 3, 2]
zbior = set(lista)
zbior2 = set(lista2)
print(zbior)
print(zbior2)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
print(zbior.intersection(zbior2))
