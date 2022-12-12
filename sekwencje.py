lista = ["Hubert", "Monika"]
print(type(lista))
print(lista)
print(lista[0])
print(len(lista))
lista.append(2022)
lista.append(False)
lista.append(36.6)
lista.append(36.6)
lista.append(36.6)
lista.insert(2, True)
lista[3] = 2023
lista.pop(3)
lista.remove(True)
lista.clear()
lista.append(2020)
lista.append(2022)
lista.append(2023)
lista.append(2014)
lista.sort()
lista.reverse()
print(lista)
lista2 = [12, 13, 145, 668]
wynik = lista + lista2
print(wynik * 2)

names = ["Tomek", "Adam", ['Hubert', 'Paweł']]
print(names[2][0])
