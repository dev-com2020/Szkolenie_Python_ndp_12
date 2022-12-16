import csv

class Dane:
    def __init__(self, numer, nazwa):
        self.numer = int(numer)
        self.nazwa = str(nazwa)


numer = input('podaj numer')
nazwa = input('podaj nazwę')

ListaTelefo = [numer, nazwa]

with open('ListaTelefo.csv', 'w', newline='') as file:
    writer = csv.writer(file, str(ListaTelefo))
print(ListaTelefo)
