# klasa książka telefoniczna, która umożliwi dodanie numeru telefonu wraz z nazwą
# będzie także zawierać metodę, która zapiszę jej działanie (numery i nazwy) w pliku (dowolny) z with open
import os


class Ksiazka:
    '''
    Jest to klasa, która symuluje dodanie rekordu do książki telefonicznej
    '''

    def __init__(self, nazwa, nr_tel):
        self.nazwa = nazwa
        self.nr_tel = nr_tel

    def dodaj_rekord(self):
        ksiazka.append({self.nazwa, self.nr_tel})
        # print({self.nazwa, self.nr_tel})


ksiazka = []

print("Witaj !!!")
print("Program doda kolejny wpis do książki telefonicznej.")

imie = input('Podaj imię lub nazwę posiadacza nr. telefonu: ')
numer = input('Podaj numer telefonu posiadacza nr. telefonu: ')
wpis = Ksiazka(imie, numer)
wpis.dodaj_rekord()

if os.path.isfile("ksiażka_tel.txt") == True:
    with open('ksiażka_tel.txt', 'a') as plik:
        plik.write(str(ksiazka))
else:
    with open('ksiażka_tel.txt', 'w') as plik:
        plik.write(str(ksiazka))

    with open('ksiażka_tel.txt', 'r') as plik:
        print("Twoja książka telefoniczna zawiera następujące wpisy:", plik.read())
