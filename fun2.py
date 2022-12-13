# a = 5

def globalna():
    global a
    a = 1
    b = 2
    return a + b

def nie_globalna():
    global c
    c = 3
    return a + c

print(f'Wynik dodawania1: {globalna()}')
print(f'Wynik dodawania2: {nie_globalna()}')
print(f"zmienna a: {a}")
print(f"zmienna c: {c}")
