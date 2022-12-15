class BankAccount:
    '''
    symulacja konta w banku
    '''

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Zbyt mała ilość środków!')

    def get_balance(self):
        return self.balance
