import bankaccount

start_bal = float(input('Podaj wysokość salda: '))
savings = bankaccount.BankAccount(start_bal)

pay = float(input('Jaką kwotę chcesz wpłacić? '))
print('Wpłacam środki...')
savings.deposit(pay)
print(savings)


cash = float(input('Jaką kwotę chcesz wypłacić? '))
print("Ta kwota zostanie odjęta od salda!")
pin = savings.pin(cash)
print(savings)

