# lista = []
#
# for numer in range(1999, 2022):
#     # print(numer)
#     lista.append(numer)
#     print(f"Iteracja {numer}, Działam dzięki range")
#
# print(lista)

x = [numer for numer in range(1999, 2022)]
print(x)

slownik = {1: "Azor", 2: "Reksio", 3: "Fafik"}
print({wartosc: klucz for klucz, wartosc in slownik.items()})

kwadrat = [i ** 2 for i in range(1, 11)]
print(kwadrat)
