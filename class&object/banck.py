class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def witdraw(self, amount): 
        if amount < self.min_withdraw:
            print(f'you can withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'bank gorib eto taka nay {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your mony: {amount}')
            print(f'your balance after withdraw {self.get_balance()}')
brac = bank(15000)
brac.witdraw(20)
brac.witdraw(300000)
brac.witdraw(300)

dbbl = bank(4000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())
dbbl.witdraw(2000)
