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
    writer.writerow([3, 'Arnold', "Warszawa"])
    writer.writerow([3, 'Hubert'])
    writer.writerow([3, '', 'Kielce'])

with open('dane3.csv', 'w', newline="") as file:
    names = ['name', 'score']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    writer.writerow({'name': 'Tomek', 'score': 4564})
    writer.writerow({'name': 'Jacek', 'score': 1564})
    writer.writerow({'name': 'Agata', 'score': 2364})

