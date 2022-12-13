keep_going = 't'

while keep_going == 't':
    sales = float(input('Podaj wielkość sprzedaży: '))
    comm_rate = float(input('Podaj wysokość premii: '))
    commission = sales * comm_rate
    print('Premia wynosi', format(commission, '.2f'), 'zł')
    keep_going = input('Czy chcesz obliczyć kolejną premie?(jeśli tak, wpisz "t")')
print("Obliczono premię.")
