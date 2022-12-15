def funk(a, b=0, *args):
    print(a)
    print(b)
    print(args)


def funk2(a, /, b=0, *args, **kwargs):
    print("Liczba przekazanych argumentów", len(kwargs))
    print(kwargs)
    print(args)
    print(a, b)
    for key, value in kwargs.items():
        print("Klucz:", key, "Wartość", value)


funk2(4)
funk2(5, a=1)
funk2(3, a=1, b=3)
funk2(2, a=1, v=22, b=222)
funk2(543, 4322, 434, a=1, v=22, d=222)
# funk(21)
# funk(21, 333)
# funk(5, 22, 33, 668)
# funk(5, 22, 33, "Tomek")
