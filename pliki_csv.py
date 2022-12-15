import csv

lista = []

with open('dane.csv') as file:
    reader = csv.reader(file)
    for i in reader:
        lista.append(i)

lista[1][1] = "tomek"

with open('dane2.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lista)
