class Pracownik:

    def __init__(self, imie):
        self.imie = imie

    def show(self):
        print(f"Pracownik o imieniu {self.imie}")

    @staticmethod
    def spiewaj(x):
        print(f"Śpiewam {x}")

