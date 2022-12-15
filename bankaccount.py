class BankAccount:
    '''
    symulacja konta w banku
    '''

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def __withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Zbyt mała ilość środków!')

    def pin(self, amount):
        pin = int(input("Podaj pin:"))
        if pin == 4455:
            self.__withdraw(amount)
        else:
            print("Zły PIN!")

    def get_balance(self):
        return self.__balance
