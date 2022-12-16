# class Human:
#     '''
#     Jest to klasa, która symuluje powstawnie człowieka
#     '''
#
#     imie = ""
#     wiek = None
#     plec = ""
#
#     def witaj(self):
#         '''
#         Metoda która symuluje powitanie
#         :return: imię człowieka
#         '''
#         print("Cześć, mam na imię", self.imie)
#
#     def ruszaj(self):
#         if self.plec == 'k':
#             print("Ruszyłam w podróż!")
#         else:
#             print('Ruszyłem w podróz!')

class Human:
    '''
    Jest to klasa, która symuluje powstawnie człowieka
    '''

    def __init__(self, imie, wiek=0, plec=''):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def witaj(self):
        '''
        Metoda która symuluje powitanie
        :return: imię człowieka
        '''
        print("Cześć, mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w podróż!")
        else:
            print('Ruszyłem w podróz!')


czlowiek1 = Human("Adam", 25, 'm')
# czlowiek1.imie = "Adam"
# czlowiek1.wiek = 25
# czlowiek1.plec = 'm'
czlowiek1.witaj()
czlowiek1.ruszaj()
print()
czlowiek2 = Human("Ewa", 22, 'k')
# czlowiek2.imie = "Ewa"
# czlowiek2.wiek = 22
# czlowiek2.plec = 'k'
czlowiek2.witaj()
czlowiek2.ruszaj()
print()
czlowiek3 = Human("Andrzej")
# czlowiek2.imie = "Ewa"
print(czlowiek3.wiek)
czlowiek3.plec = 'm'
czlowiek3.witaj()
czlowiek3.ruszaj()

lista = [czlowiek3.wiek, czlowiek2.wiek, czlowiek1.wiek]
print(lista)
