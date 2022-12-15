class Ptak:

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f'Tu {self.gatunek}, startuje i lecę z prędkością {self.szybkosc}')

    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print(f'Tu {self.gatunek}, startuje i rozpoczynam polowanie!!!')

    def wydajOdglos(self):
        print("PIIIIIIII....")


class Kura(Ptak):
    def lataj(self):
        print(f'Tu {self.gatunek}, ja nie latam :)')


class Mutant(Kura, Orzel, Ptak):
    def gryz(self):
        print("Atakuje!!!")


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

