# klasa książka telefoniczna, która umożliwi dodanie numeru telefonu wraz z nazwą
# będzie także zawierać metodę która zapiszę jej działanie (numery i nazwy) w pliku

import pandas as pd


class Telefoniczna:
    '''
    Jest to klasa, która symuluje zapisywanie danych do ksiazki telefonicznej
    '''

    def __init__(self, imie, nazwisko, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def nazwa1(self):
        '''
        Metoda która symuluje zapisanie
        :return: imienia człowieka
        '''
        print("Wpisuje imię: ", self.imie)

    def nazwa2(self):
        '''
        Metoda która symuluje zapisanie
        :return: nazwiska człowieka
        '''
        print("Wpisuje nazwisko: ", self.nazwisko)

    def telefon(self):
        '''
        Metoda która symuluje zapisanie
        :return: numer człowieka
        '''
        print("Wpisuje numer: ", self.numer)


osoba1 = Telefoniczna("Adam", "Mada", "505596664")
osoba1.nazwa1()
osoba1.nazwa2()
osoba1.telefon()
print()

file_name = "Ksiazka_Telefoniczna.txt"
with open(file_name, 'a') as f:
    f.write("Adam, Mada, 505596664")
with open(file_name, 'r') as f:
    print(f.read())

# df = pd.DataFrame(data, columns=['imie', 'nazwisko' , 'numer']).fillna (0)

# data = pd.DataFrame(df)
# data.to_csv('Ksiazka.csv', index=False)
