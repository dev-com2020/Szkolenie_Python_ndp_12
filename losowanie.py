import random

k6 = random.randint(1, 6)
print("Wynik rzutu kością:", k6)

lista = ["Tomek", "Ania", "Krzysiek", "Mikołaj", "Albert"]
loteria = random.choice(lista)
print(loteria)

liczba = random.random()
print(liczba * 1000)
print(liczba * 100)
print(liczba * 10)