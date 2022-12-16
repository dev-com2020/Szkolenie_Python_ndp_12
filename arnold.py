import csv


class KsiazkaTel:
    Telefon = ""
    Nazwa = ""

    def __init__(self, telefon, nazwa):
        self.Telefon = telefon
        self.Nazwa = nazwa

    def wyslij(self):
        return self.Telefon, self.Nazwa


lista = []

while True:
    name = str(input("podaj nazwe:"))
    print(f"Podałeś:", name)
    numer = str(input("Podaj numer:"))
    user = KsiazkaTel(numer, name)
    lista.append(user)
    warunek = ord(input("Czy chcesz dodać kolejny t/n :"))
    if warunek == 78 or warunek == 110:
        break

warunek = ord(input("Czy chcesz zapisać książkę do pliku t/n :"))
if warunek == 84 or warunek == 116:
    with open('ksiazka.csv', 'w', newline="") as file:
        names = ['Telefon', 'Nazwa']
        writer = csv.DictWriter(file, fieldnames=names)
        writer.writeheader()
        writer = csv.writer(file)
        for pozycja in lista:
            row = pozycja.wyslij()
            writer.writerow(row)
