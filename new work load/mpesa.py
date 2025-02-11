from abc import ABC, abstractmethod
# encapsulation

class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        print(f"Attempting to withdraw {amount} from account of {self.holder_name} with balance of {self.balance} ")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrawn {amount} from account of {self.holder_name}, new balance of {self.holder_name} is {self.balance}")
        else:
            print('Insufficient balance. In other words, you cannot withdraw.')

    def check_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.holder_name

# Inheritance

class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id,holder_name,balance)
        self.phone_number = phone_number

# Polymorphism

class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        pass

class Deposit_Transaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)

class Withdraw_Transaction(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)

# Abstraction
class Payment_System(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class Mpesa_Payment_System(Payment_System):
    def process_payment(self, amount):
        print(f"Processing Mpesa payment of {amount}")

# example usage

mpesa = Mpesa_Payment_System()
account1 = Customer(1,"Yahya Mohamed", 400, 717172557)
deposit = Deposit_Transaction(1000)
withdraw = Withdraw_Transaction(210)

deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of Mpesa account holder {account1.get_account_holder()} is: " 
      f"{account1.check_balance()}")

account2 = Customer(2, "Yorgv Mikelovic", 49930003, 694999499999 )
deposit1 = Deposit_Transaction(1000500)
withdraw1 = Withdraw_Transaction(2100000)

deposit1.execute(account2)
withdraw1.execute(account2)
print(f"The balance of account holder {account2.get_account_holder()} is: " 
      f"{account2.check_balance()}")

