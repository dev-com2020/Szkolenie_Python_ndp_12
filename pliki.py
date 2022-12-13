# plik = open('dane.txt', 'r')  # odczyt
# plik2 = open('dane.txt', 'w')  # nadpisanie
# plik3 = open('dane.txt', 'a')  # dopisanie
#
# plik.close()
# plik2.close()
# plik3.close()

# lista = []
# for i in range(1, 11, 2):
#     lista.append(i)
#
# with open('dane.txt', 'w') as plik:
#     plik.write(str(lista))
#
# with open('dane2.txt', 'a') as plik:
#     plik.write("Coś..")

lista = []
with open('dane.txt', 'r') as plik:
    lista.append(plik.read())

print(lista)