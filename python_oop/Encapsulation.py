class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #public attribute
        self._branch = 'mirpur' #protected
        self.__balance= initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

rathat = Bank('mondol', 10000)

print(rathat.holder_name)
rathat.deposit(400000)
print(rathat.get_balance())
# print(rathat._branch)

# print(dir(rathat))
# print(rathat._Bank__balance)