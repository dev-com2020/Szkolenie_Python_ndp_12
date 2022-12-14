# def adder(a, b):
#     return a + b
#
# def to_upper(s):
#     return s.upper()

lam1 = lambda a, b=0: a + b
lam2 = lambda s: s.upper()

print(lam1(6))
print(lam2("tomek"))
print(sorted("Tomek", reverse=False, key=str.lower))

things = {'a': 11, 'b': 2, 'c': 0, 'd': 33}
print(sorted(things))
print(sorted(things.values()))
print(sorted(things.items()))
print(sorted(things.items(), key=lambda x: x[1]))

wiek = lambda _: "dziecko" if _ < 10 else ("Nastolatek" if _ < 18 else "Dorosły")
print(wiek(5))
print(wiek(16))
print(wiek(21))

lista = [1, 3, 5, 7, 9]
print(f"Lista: {lista}")
print(f"Zastosowanie map: {list(map(lambda _: _ * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda _: _ > 3, lista))}")
