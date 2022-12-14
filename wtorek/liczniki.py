# licznik = 0
# warunek = int(input('Podaj ilość iteracji'))
# while licznik < warunek:
#     print(licznik)
#     licznik += 1

# lista = [4, 56, 33, 53, 11, 432]
#
# for i in lista:
#     print(i)

# napis = "Python jest spoko!"
# for i in napis:
#     print(i)

lista = []

for numer in range(1999, 2022):
    # print(numer)
    lista.append(numer)
    print(f"Iteracja {numer}, Działam dzięki range")

print(lista)