class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit (self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


Bank = BankAccount("Jeff" , 0)
print('Type out "deposit" or "withdraw" if you want to deposit or withdraw your money. ')
Select = input()
print('Select an amount: ')
amount = int(input())


if Select == 'deposit':
    Bank.deposit(amount)
    print("Your new balance is: ", Bank.get_balance())

elif Select == 'withdraw':
     Bank.withdraw(amount)
     if Bank.get_balance() > 0 :
       print("Your new balance is: ", Bank.get_balance())
     else:
       print("You dont have enough funds in your account for this amount.")

else:
    print("Invalid input")