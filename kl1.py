class Human:
    '''
    Jest to klasa, która symuluje powstawnie człowieka
    '''

    imie = ""
    wiek = None
    plec = ""

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


czlowiek1 = Human()
czlowiek1.imie = "Adam"
czlowiek1.wiek = 25
czlowiek1.plec = 'm'
czlowiek1.witaj()
czlowiek1.ruszaj()


