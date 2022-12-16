# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except TypeError:
#         return 0
#     except ValueError:
#         return 1

# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         return 0

def mnozenie(a, b):
    try:
        wynik = int(a) * int(b)
    except Exception as e:
        plik = open('../dane/error.log', 'a')
        plik.write(str(e.args))
        return 1
    else:
        return wynik
    finally:
        print(lista)


lista = []
lista.append(mnozenie('20', '34'))
lista.append(mnozenie(20, 34))
lista.append(mnozenie(20, None))
lista.append(mnozenie('a', 'tomek'))

print("Reszta programu...")

