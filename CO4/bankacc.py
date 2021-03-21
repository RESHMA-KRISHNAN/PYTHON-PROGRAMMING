class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def dump(self):
        print("Name:",self.name,"No:", self.no,"Balance:", self.balance)
      


a1 = AccountP('John Olsson', '19371554951', 20000)

a1.deposit(1000)

a1.withdraw(4000)
a1.withdraw(3500)
a1.dump()
print(a1.balance)       
print(a1.get_balance())      
