from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f'Tu {self.gatunek}, startuje i lecę z prędkością {self.szybkosc}')

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print(f'Tu {self.gatunek}, startuje i rozpoczynam polowanie!!!')

    def wydajOdglos(self):
        print("PIIIIIIII....")


class Kura(Ptak):

    def __init__(self, gatunek, jaja):
        super().__init__(gatunek, 0)
        self.ilosc_jaj = jaja

    def lataj(self):
        print(f'Tu {self.gatunek}, ja nie latam :)')

    def wydajOdglos(self):
        print("kokokok")


class Mutant(Kura, Orzel, Ptak):
    def gryz(self):
        print("Atakuje!!!")

    def wydajOdglos(self):
        print("grrrr")


ptak1 = Orzel('orzeł', 100)
ptak1.lataj()
ptak1.poluj()
ptak1.wydajOdglos()

ptak2 = Kura('kura', 1)
ptak2.lataj()
ptak2.wydajOdglos()

print(Mutant.mro())

mutant = Mutant('mutant', 0)
mutant.lataj()
mutant.wydajOdglos()
