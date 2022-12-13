# from poniedzialek.wprowadzanie2 import wiek, imie
#
# print("Tutaj plik start...")
# lista = []
# slownik = {}
# lista.append(wiek)
# lista.append(imie)
# slownik[imie] = int(wiek)
# print(lista)
# print(slownik)

from pakiet import *

#
# slownik = in_list.szukaj()
# slownik['T748'] = 'książka'
# print(slownik)

liczba1 = 5
liczba2 = 1

dodaj = in_list.odejmowanie(liczba1, liczba2)
print(f'Wynik odejmowania: {dodaj}')

dodaj = in_list.odejmowanie(liczba2)
print(f'Wynik odejmowania: {dodaj}')

dodaj = in_list.odejmowanie()
print(f'Wynik odejmowania: {dodaj}')

dodaj = in_list.odejmowanie(a=liczba1, b=liczba2)
print(f'Wynik odejmowania: {dodaj}')

dodaj = in_list.odejmowanie(b=liczba2)
print(f'Wynik odejmowania: {dodaj}')

dodaj = in_list.odejmowanie(2, b=liczba2)
print(f'Wynik odejmowania: {dodaj}')
