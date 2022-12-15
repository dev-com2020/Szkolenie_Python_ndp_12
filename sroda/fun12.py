def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2


# kwadrat(5)
# kwa = kwadrat2(5)
# print(next(kwa))
# print(next(kwa))
# print("ddsdsdsdsdsddddsddsd")
# lista = []
# lista.append("23232")
# print(next(kwa))


# print(next(kwa))
# print(next(kwa))


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


def counter2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


# c = counter2()
# print(next(c))
# print(next(c))
# print(next(c))
# print(c.send('OK'))
# print(next(c))
# print(next(c))
# print(c.send('q'))


def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))


for n in print_squares(2, 5):
    print(n)

# c = counter()
# for i in range(5):
#     next(c)
# lista = [next(c), next(c), "Tomek", next(c)]
# print(lista)
